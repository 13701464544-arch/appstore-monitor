import requests
from bs4 import BeautifulSoup
import feedparser
import json
from datetime import datetime
import time

# 全局配置
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
KEYWORDS = ["App Store", "Google Play", "应用商店", "应用市场", "审核", "合规", "算法", "流量", "SDK", "权限", "开发者", "政策"]

# --------------------------
# 1. 各平台爬虫函数
# --------------------------

def crawl_apple():
    """爬取苹果开发者新闻"""
    url = "https://developer.apple.com/news/"
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        items = []
        for article in soup.select(".news-item")[:5]:
            title = article.select_one("h3").get_text(strip=True)
            link = "https://developer.apple.com" + article.select_one("a")["href"]
            summary = article.select_one(".summary").get_text(strip=True) if article.select_one(".summary") else title
            items.append({
                "tag": "App Store",
                "title": title,
                "summary": summary,
                "source": "苹果开发者",
                "time": datetime.now().strftime("%Y-%m-%d"),
                "link": link,
                "impact": "影响App Store审核与上架策略"
            })
        return items
    except:
        return []

def crawl_google():
    """爬取Google Play开发者新闻"""
    url = "https://android-developers.googleblog.com/"
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        items = []
        for post in soup.select(".post")[:5]:
            title = post.select_one("h2").get_text(strip=True)
            link = post.select_one("a")["href"]
            summary = post.select_one(".post-body").get_text(strip=True)[:100] + "..."
            items.append({
                "tag": "Google Play",
                "title": title,
                "summary": summary,
                "source": "Google开发者",
                "time": datetime.now().strftime("%Y-%m-%d"),
                "link": link,
                "impact": "影响Google Play全球应用分发"
            })
        return items
    except:
        return []

def crawl_oppo():
    """爬取OPPO开放平台"""
    url = "https://open.oppomobile.com/wiki/doc#id=10288"
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        items = []
        for item in soup.select(".news-item")[:3]:
            title = item.get_text(strip=True)
            items.append({
                "tag": "OPPO",
                "title": title,
                "summary": "OPPO应用市场政策更新",
                "source": "OPPO开放平台",
                "time": datetime.now().strftime("%Y-%m-%d"),
                "link": url,
                "impact": "影响OPPO应用上架与流量分发"
            })
        return items
    except:
        return []

def crawl_vivo():
    """爬取VIVO开放平台"""
    url = "https://developer.vivo.com.cn/doc"
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        items = []
        for item in soup.select(".article-item")[:3]:
            title = item.get_text(strip=True)
            items.append({
                "tag": "VIVO",
                "title": title,
                "summary": "VIVO应用市场合规更新",
                "source": "VIVO开发者",
                "time": datetime.now().strftime("%Y-%m-%d"),
                "link": url,
                "impact": "影响VIVO应用审核与推荐"
            })
        return items
    except:
        return []

def crawl_xiaomi():
    """爬取小米开发者站"""
    url = "https://dev.mi.com/console/doc/detail?pId=1828"
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        items = []
        for item in soup.select(".doc-item")[:3]:
            title = item.get_text(strip=True)
            items.append({
                "tag": "小米",
                "title": title,
                "summary": "小米应用商店算法调整",
                "source": "小米开发者",
                "time": datetime.now().strftime("%Y-%m-%d"),
                "link": url,
                "impact": "影响小米应用自然流量分配"
            })
        return items
    except:
        return []

def crawl_36kr():
    """爬取36氪应用商店相关新闻"""
    url = "https://36kr.com/search/articles/应用商店"
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        items = []
        for article in soup.select(".article-item")[:5]:
            title = article.select_one("h3").get_text(strip=True)
            link = "https://36kr.com" + article.select_one("a")["href"]
            summary = article.select_one(".desc").get_text(strip=True)
            items.append({
                "tag": "36氪",
                "title": title,
                "summary": summary,
                "source": "36氪",
                "time": datetime.now().strftime("%Y-%m-%d"),
                "link": link,
                "impact": "行业深度分析，影响产品决策"
            })
        return items
    except:
        return []

def crawl_huxiu():
    """爬取虎嗅应用商店相关新闻"""
    url = "https://www.huxiu.com/search?kw=应用商店"
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        items = []
        for article in soup.select(".search-result-item")[:5]:
            title = article.select_one("h3").get_text(strip=True)
            link = "https://www.huxiu.com" + article.select_one("a")["href"]
            summary = article.select_one(".summary").get_text(strip=True)
            items.append({
                "tag": "虎嗅",
                "title": title,
                "summary": summary,
                "source": "虎嗅",
                "time": datetime.now().strftime("%Y-%m-%d"),
                "link": link,
                "impact": "行业观点，影响产品策略"
            })
        return items
    except:
        return []

# 可继续扩展：腾讯新闻、网易新闻、头条、钛媒体、donews、品玩、Questmobile、SensorTower等
# 格式同上，只需替换URL和选择器

# --------------------------
# 2. 主爬虫入口
# --------------------------

def main():
    all_news = []
    # 调用所有爬虫
    all_news.extend(crawl_apple())
    all_news.extend(crawl_google())
    all_news.extend(crawl_oppo())
    all_news.extend(crawl_vivo())
    all_news.extend(crawl_xiaomi())
    all_news.extend(crawl_36kr())
    all_news.extend(crawl_huxiu())
    
    # 去重、过滤关键词
    seen = set()
    filtered = []
    for item in all_news:
        if item["title"] not in seen and any(kw in item["title"] for kw in KEYWORDS):
            seen.add(item["title"])
            filtered.append(item)
    
    # 生成最终数据
    result = {
        "update_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "news": filtered[:20]  # 最多20条
    }
    
    # 写入data.json
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 爬取完成，共 {len(filtered)} 条有效信息")

if __name__ == "__main__":
    main()
