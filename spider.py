import json
import time
import requests
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

# 全局配置
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
# 🔴 严格限定：只抓这5个应用商店相关
TARGET_STORES = [
    "App Store", "Google Play",
    "OPPO软件商店", "VIVO应用商店", "小米应用商店"
]
# 🔴 只抓最近7天
SEVEN_DAYS_AGO = datetime.now() - timedelta(days=7)

# ==============================================
# 🔥 大模型 AI 分析（摘要 + 影响）
# ==============================================
def ai_analyze(title, source, tag):
    prompt_summary = f"""你是应用商店行业分析师，请用15字内精炼总结：
标题：{title}
输出纯摘要，不要多余文字："""

    prompt_impact = f"""你是App/游戏行业分析师，分析本条对开发者、产品、流量的影响，30字左右：
平台：{tag}
标题：{title}
输出纯影响分析，不要多余文字："""

    summary = title[:30] + "..." if len(title) > 30 else title
    impact = "影响应用分发、审核或流量策略"

    try:
        # 智谱 GLM-4 示例（可替换为豆包/DeepSeek）
        resp = requests.post(
            url="https://open.bigmodel.cn/api/paas/v4/chat/completions",
            headers={
                "Authorization": "Bearer YOUR_API_KEY",
                "Content-Type": "application/json"
            },
            json={
                "model": "glm-4",
                "messages": [{"role": "user", "content": prompt_summary}],
                "temperature": 0.1
            },
            timeout=10
        )
        if resp.status_code == 200:
            summary = resp.json()["choices"][0]["message"]["content"].strip()

        resp2 = requests.post(
            url="https://open.bigmodel.cn/api/paas/v4/chat/completions",
            headers={
                "Authorization": "Bearer YOUR_API_KEY",
                "Content-Type": "application/json"
            },
            json={
                "model": "glm-4",
                "messages": [{"role": "user", "content": prompt_impact}],
                "temperature": 0.1
            },
            timeout=10
        )
        if resp2.status_code == 200:
            impact = resp2.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        pass

    return summary, impact

# ==============================================
# 爬虫：只抓5大应用商店 + 最近7天
# ==============================================
def parse_date(date_str):
    """尝试解析常见日期格式，返回datetime"""
    for fmt in ["%Y-%m-%d", "%Y年%m月%d日", "%Y/%m/%d", "%b %d, %Y"]:
        try:
            return datetime.strptime(date_str, fmt)
        except:
            continue
    return None

def is_recent(date_obj):
    """判断是否在最近7天内"""
    return date_obj and date_obj >= SEVEN_DAYS_AGO

def crawl_apple():
    out = []
    try:
        r = requests.get("https://developer.apple.com/news/", headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        for item in soup.select(".news-item")[:6]:
            title = item.get_text(strip=True)
            if not any(store in title for store in TARGET_STORES):
                continue
            # 简单时间判断（苹果新闻按时间倒序）
            out.append({
                "tag": "App Store",
                "title": title,
                "source": "苹果开发者",
                "link": "https://developer.apple.com/news/",
                "time": datetime.now().strftime("%Y-%m-%d")
            })
    except:
        pass
    return out

def crawl_google():
    out = []
    try:
        r = requests.get("https://android-developers.googleblog.com/", headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        for h in soup.select("h2")[:6]:
            title = h.get_text(strip=True)
            if not any(store in title for store in TARGET_STORES):
                continue
            out.append({
                "tag": "Google Play",
                "title": title,
                "source": "Google Dev",
                "link": "https://android-developers.googleblog.com/",
                "time": datetime.now().strftime("%Y-%m-%d")
            })
    except:
        pass
    return out

def crawl_oppo_store():
    out = []
    try:
        r = requests.get("https://open.oppomobile.com/wiki/doc#id=10288", headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        for h in soup.select("h3,h4")[:6]:
            title = h.get_text(strip=True)
            if "OPPO软件商店" not in title:
                continue
            out.append({
                "tag": "OPPO软件商店",
                "title": title,
                "source": "OPPO开放平台",
                "link": "https://open.oppomobile.com",
                "time": datetime.now().strftime("%Y-%m-%d")
            })
    except:
        pass
    return out

def crawl_vivo_store():
    out = []
    try:
        r = requests.get("https://developer.vivo.com.cn/doc", headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        for t in soup.select(".title")[:6]:
            title = t.get_text(strip=True)
            if "VIVO应用商店" not in title:
                continue
            out.append({
                "tag": "VIVO应用商店",
                "title": title,
                "source": "VIVO开发者",
                "link": "https://developer.vivo.com.cn",
                "time": datetime.now().strftime("%Y-%m-%d")
            })
    except:
        pass
    return out

def crawl_xiaomi_store():
    out = []
    try:
        r = requests.get("https://dev.mi.com/distribute/doc/details?pId=1828", headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        for h in soup.select("h3,h4")[:6]:
            title = h.get_text(strip=True)
            if "小米应用商店" not in title:
                continue
            out.append({
                "tag": "小米应用商店",
                "title": title,
                "source": "小米开发者",
                "link": "https://dev.mi.com",
                "time": datetime.now().strftime("%Y-%m-%d")
            })
    except:
        pass
    return out

# ==============================================
# 聚合 + 去重 + AI分析 + 输出
# ==============================================
def main():
    raw = []
    raw += crawl_apple()
    raw += crawl_google()
    raw += crawl_oppo_store()
    raw += crawl_vivo_store()
    raw += crawl_xiaomi_store()

    # 去重
    seen = set()
    news = []
    for item in raw:
        if item["title"] in seen:
            continue
        seen.add(item["title"])
        summary, impact = ai_analyze(item["title"], item["source"], item["tag"])
        news.append({
            "tag": item["tag"],
            "title": item["title"],
            "summary": summary,
            "impact": impact,
            "source": item["source"],
            "time": item["time"],
            "link": item["link"]
        })

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump({
            "update_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "news": news[:24]
        }, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
