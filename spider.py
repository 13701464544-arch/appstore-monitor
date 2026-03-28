import json
import time
import requests
from datetime import datetime
from bs4 import BeautifulSoup

# 全局配置
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
TARGET_KEYWORDS = ["App Store", "Google Play", "OPPO软件商店", "VIVO应用商店", "小米应用商店", "应用商店", "应用市场", "审核", "合规", "算法", "流量", "分发"]

# ==============================================
# 🔥 大模型 AI 生成：摘要 + 影响分析
# ==============================================
def ai_analyze(title, source, tag):
    prompt_summary = f"""你是专业行业分析师，请用15字以内精炼总结这条标题：
标题：{title}
输出纯摘要，不要多余文字："""

    prompt_impact = f"""你是App/游戏行业分析师，针对应用商店生态，分析本条对开发者、产品、流量的影响，30字左右：
来源：{source}
平台：{tag}
标题：{title}
输出纯影响分析，不要多余文字："""

    summary = title[:30] + "..." if len(title) > 30 else title
    impact = "影响应用分发、审核或流量策略"

    try:
        resp = requests.post(
            url="https://open.bigmodel.cn/api/paas/v4/chat/completions",
            headers={"Authorization": "Bearer YOUR_API_KEY", "Content-Type": "application/json"},
            json={"model": "glm-4", "messages": [{"role": "user", "content": prompt_summary}], "temperature": 0.1},
            timeout=10
        )
        if resp.status_code == 200:
            summary = resp.json()["choices"][0]["message"]["content"].strip()

        resp2 = requests.post(
            url="https://open.bigmodel.cn/api/paas/v4/chat/completions",
            headers={"Authorization": "Bearer YOUR_API_KEY", "Content-Type": "application/json"},
            json={"model": "glm-4", "messages": [{"role": "user", "content": prompt_impact}], "temperature": 0.1},
            timeout=10
        )
        if resp2.status_code == 200:
            impact = resp2.json()["choices"][0]["message"]["content"].strip()
    except:
        pass

    return summary, impact

# ==============================================
# 爬虫：全平台
# ==============================================
def crawl_apple():
    out = []
    try:
        r = requests.get("https://developer.apple.com/news/", headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        for a in soup.select(".news-item")[:4]:
            t = a.get_text(strip=True)
            if any(k in t for k in TARGET_KEYWORDS):
                out.append({"tag":"App Store","title":t,"source":"苹果开发者","link":"https://developer.apple.com/news/"})
    except: pass
    return out

def crawl_google():
    out = []
    try:
        r = requests.get("https://android-developers.googleblog.com/", headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        for h in soup.select("h2")[:4]:
            t = h.get_text(strip=True)
            if any(k in t for k in TARGET_KEYWORDS):
                out.append({"tag":"Google Play","title":t,"source":"Google Dev","link":"https://android-developers.googleblog.com/"})
    except: pass
    return out

def crawl_oppo():
    out = []
    try:
        r = requests.get("https://open.oppomobile.com/wiki/doc#id=10288", headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        for h in soup.select("h3,h4")[:4]:
            t = h.get_text(strip=True)
            if any(k in t for k in TARGET_KEYWORDS):
                out.append({"tag":"OPPO","title":t,"source":"OPPO开放平台","link":"https://open.oppomobile.com"})
    except: pass
    return out

def crawl_vivo():
    out = []
    try:
        r = requests.get("https://developer.vivo.com.cn/doc", headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        for t in soup.select(".title")[:4]:
            txt = t.get_text(strip=True)
            if any(k in txt for k in TARGET_KEYWORDS):
                out.append({"tag":"VIVO","title":txt,"source":"VIVO开发者","link":"https://developer.vivo.com.cn"})
    except: pass
    return out

def crawl_xiaomi():
    out = []
    try:
        r = requests.get("https://dev.mi.com/distribute/doc/details?pId=1828", headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        for h in soup.select("h3,h4")[:4]:
            t = h.get_text(strip=True)
            if any(k in t for k in TARGET_KEYWORDS):
                out.append({"tag":"小米","title":t,"source":"小米开发者","link":"https://dev.mi.com"})
    except: pass
    return out

def crawl_questmobile():
    out = []
    try:
        r = requests.get("https://www.questmobile.com.cn/research", headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        for h in soup.select("h3,h4")[:4]:
            t = h.get_text(strip=True)
            if any(k in t for k in TARGET_KEYWORDS):
                out.append({"tag":"QuestMobile","title":t,"source":"QuestMobile","link":"https://www.questmobile.com.cn"})
    except: pass
    return out

def crawl_sensortower():
    out = []
    try:
        r = requests.get("https://sensortower.com/blog", headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        for h in soup.select("h2,h3")[:4]:
            t = h.get_text(strip=True)
            if any(k in t for k in TARGET_KEYWORDS):
                out.append({"tag":"SensorTower","title":t,"source":"SensorTower","link":"https://sensortower.com/blog"})
    except: pass
    return out

def crawl_wechat_mp():
    out = []
    try:
        r = requests.get("https://weixin.sogou.com/weixin?type=2&query=App Store 应用商店", headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        for h in soup.select("h3")[:4]:
            t = h.get_text(strip=True)
            if any(k in t for k in TARGET_KEYWORDS):
                out.append({"tag":"微信公众号","title":t,"source":"微信公众号","link":"https://weixin.sogou.com"})
    except: pass
    return out

def crawl_toutiao():
    out = []
    try:
        r = requests.get("https://www.toutiao.com/search?q=App Store 应用商店", headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        for t in soup.select(".title")[:4]:
            txt = t.get_text(strip=True)
            if any(k in txt for k in TARGET_KEYWORDS):
                out.append({"tag":"头条","title":txt,"source":"今日头条","link":"https://toutiao.com"})
    except: pass
    return out

def crawl_36kr():
    out = []
    try:
        r = requests.get("https://36kr.com/search/articles/应用商店", headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        for a in soup.select("article")[:4]:
            t = a.get_text(strip=True)
            if any(k in t for k in TARGET_KEYWORDS):
                out.append({"tag":"36氪","title":t,"source":"36氪","link":"https://36kr.com"})
    except: pass
    return out

def crawl_huxiu():
    out = []
    try:
        r = requests.get("https://www.huxiu.com/search?kw=应用商店", headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        for i in soup.select(".search-result-item")[:4]:
            t = i.get_text(strip=True)
            if any(k in t for k in TARGET_KEYWORDS):
                out.append({"tag":"虎嗅","title":t,"source":"虎嗅","link":"https://huxiu.com"})
    except: pass
    return out

# ==============================================
# 主函数：聚合 + AI分析 + 输出data.json
# ==============================================
def main():
    raw = []
    raw += crawl_apple()
    raw += crawl_google()
    raw += crawl_oppo()
    raw += crawl_vivo()
    raw += crawl_xiaomi()
    raw += crawl_questmobile()
    raw += crawl_sensortower()
    raw += crawl_wechat_mp()
    raw += crawl_toutiao()
    raw += crawl_36kr()
    raw += crawl_huxiu()

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
            "time": datetime.now().strftime("%Y-%m-%d"),
            "link": item["link"]
        })

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump({
            "update_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "news": news[:24]
        }, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
