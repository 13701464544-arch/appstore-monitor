import json
import time
import requests
from datetime import datetime
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
TARGETS = ["App Store", "Google Play", "OPPO", "VIVO", "小米", "应用市场", "应用商店"]

# ------------------------------
# AI 摘要 & 影响分析（本地规则强AI）
# ------------------------------
def ai_summary(title, source):
    return f"【{source}】{title[:30]}..." if len(title) > 30 else f"【{source}】{title}"

def ai_impact(tag, title):
    if tag in ["App Store", "Google Play"]:
        return "影响全球应用分发规则、审核标准、流量权重与合规要求"
    if tag in ["OPPO", "VIVO", "小米"]:
        return "影响国内安卓分发、审核策略、自然流量与合规排查"
    if tag in ["QuestMobile", "SensorTower"]:
        return "影响行业趋势判断、用户大盘、投放策略与产品优先级"
    if tag in ["微信公众号", "头条"]:
        return "影响行业认知、舆情走向与渠道策略判断"
    return "影响应用上架、流量分发或行业趋势判断"

# ------------------------------
# 1. 官方商店爬虫
# ------------------------------
def crawl_apple():
    out = []
    try:
        r = requests.get("https://developer.apple.com/news/", headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        for a in soup.select(".news-item")[:4]:
            t = a.get_text(strip=True)
            if any(k in t for k in TARGETS):
                out.append({"tag":"App Store","title":t,"source":"苹果开发者","link":"https://developer.apple.com/news/"})
    except: pass
    return out

def crawl_google():
    out = []
    try:
        r = requests.get("https://android-developers.googleblog.com/", headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        for p in soup.select("h2")[:4]:
            t = p.get_text(strip=True)
            if any(k in t for k in TARGETS):
                out.append({"tag":"Google Play","title":t,"source":"Google Dev","link":"https://android-developers.googleblog.com/"})
    except: pass
    return out

def crawl_oppo():
    out = []
    try:
        r = requests.get("https://open.oppomobile.com/wiki/doc#id=10288", headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        for i in soup.select("h3,h4")[:4]:
            t = i.get_text(strip=True)
            if any(k in t for k in TARGETS):
                out.append({"tag":"OPPO","title":t,"source":"OPPO开放平台","link":"https://open.oppomobile.com"})
    except: pass
    return out

def crawl_vivo():
    out = []
    try:
        r = requests.get("https://developer.vivo.com.cn/doc", headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        for i in soup.select(".title")[:4]:
            t = i.get_text(strip=True)
            if any(k in t for k in TARGETS):
                out.append({"tag":"VIVO","title":t,"source":"VIVO开发者","link":"https://developer.vivo.com.cn"})
    except: pass
    return out

def crawl_xiaomi():
    out = []
    try:
        r = requests.get("https://dev.mi.com/distribute/doc/details?pId=1828", headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        for i in soup.select("h3,h4")[:4]:
            t = i.get_text(strip=True)
            if any(k in t for k in TARGETS):
                out.append({"tag":"小米","title":t,"source":"小米开发者","link":"https://dev.mi.com"})
    except: pass
    return out

# ------------------------------
# 2. 新增：QuestMobile / SensorTower
# ------------------------------
def crawl_questmobile():
    out = []
    try:
        r = requests.get("https://www.questmobile.com.cn/research", headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        for i in soup.select("h3,h4")[:4]:
            t = i.get_text(strip=True)
            if any(k in t for k in TARGETS):
                out.append({"tag":"QuestMobile","title":t,"source":"QuestMobile","link":"https://www.questmobile.com.cn"})
    except: pass
    return out

def crawl_sensortower():
    out = []
    try:
        r = requests.get("https://sensortower.com/blog", headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        for i in soup.select("h2,h3")[:4]:
            t = i.get_text(strip=True)
            if any(k in t for k in TARGETS):
                out.append({"tag":"SensorTower","title":t,"source":"SensorTower","link":"https://sensortower.com/blog"})
    except: pass
    return out

# ------------------------------
# 3. 新增：微信公众号 / 头条
# ------------------------------
def crawl_wechat_mp():
    out = []
    try:
        r = requests.get("https://weixin.sogou.com/weixin?type=2&query=App Store 应用商店", headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        for h in soup.select("h3")[:4]:
            t = h.get_text(strip=True)
            if any(k in t for k in TARGETS):
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
            if any(k in txt for k in TARGETS):
                out.append({"tag":"头条","title":txt,"source":"今日头条","link":"https://toutiao.com"})
    except: pass
    return out

# ------------------------------
# 主执行
# ------------------------------
def main():
    news = []
    news += crawl_apple()
    news += crawl_google()
    news += crawl_oppo()
    news += crawl_vivo()
    news += crawl_xiaomi()
    news += crawl_questmobile()
    news += crawl_sensortower()
    news += crawl_wechat_mp()
    news += crawl_toutiao()

    # 去重
    seen = set()
    final = []
    for item in news:
        if item["title"] in seen: continue
        seen.add(item["title"])
        final.append({
            "tag": item["tag"],
            "title": item["title"],
            "summary": ai_summary(item["title"], item["source"]),
            "impact": ai_impact(item["tag"], item["title"]),
            "source": item["source"],
            "time": datetime.now().strftime("%Y-%m-%d"),
            "link": item["link"]
        })

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump({
            "update_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "news": final[:24]
        }, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
