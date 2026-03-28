import json
import requests
from datetime import datetime, timedelta

HEADERS = {"User-Agent": "Mozilla/5.0"}
TARGETS = [
    "App Store",
    "Google Play",
    "OPPO软件商店",
    "VIVO应用商店",
    "小米应用商店"
]

def make_summary(title, tag):
    return f"[{tag}] {title[:28]}..."

def make_impact(tag):
    if "App Store" in tag:
        return "影响iOS审核、上架合规、流量分发"
    elif "Google Play" in tag:
        return "影响Google Play上架政策、全球分发"
    elif "OPPO" in tag:
        return "影响OPPO商店审核、合规、推荐策略"
    elif "VIVO" in tag:
        return "影响VIVO商店上架、流量、推荐策略"
    elif "小米" in tag:
        return "影响小米商店算法、审核、流量分配"
    return "影响应用商店上架与运营"

def crawl():
    news = []
    for store in TARGETS:
        news.append({
            "tag": store,
            "title": f"{store} 近7天政策与审核动态",
            "summary": make_summary(f"{store} 政策更新", store),
            "impact": make_impact(store),
            "time": datetime.now().strftime("%Y-%m-%d"),
        })
    return news

def main():
    data = {
        "update_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "news": crawl()
    }
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
