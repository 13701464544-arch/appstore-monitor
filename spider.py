import json
import requests
from datetime import datetime, timedelta

HEADERS = {"User-Agent": "Mozilla/5.0"}
TARGET_STORES = ["App Store","Google Play","OPPO软件商店","VIVO应用商店","小米应用商店"]

def make_summary(title, tag):
    return f"【{tag}】发布最新政策，涉及审核收紧、合规升级、流量算法调整、权限管控及开发者上架要求变更。"

def make_impact(tag):
    if "App Store" in tag:
        return "影响iOS应用上架审核、隐私合规、流量获取、推广成本及全球开发者产品设计与迭代方向。"
    elif "Google Play" in tag:
        return "影响Google Play全球分发、隐私合规、推荐算法、广告策略及出海应用上架与运营成本。"
    elif "OPPO" in tag:
        return "影响OPPO软件商店上架门槛、内容审核、流量分配、推广资源与国内开发者运营策略。"
    elif "VIVO" in tag:
        return "影响VIVO应用商店审核尺度、合规要求、流量倾斜、推荐机制及国内应用分发生态格局。"
    elif "小米" in tag:
        return "影响小米应用商店算法推荐、审核规则、流量优先级、用户体验及全行业产品运营策略。"
    return "影响应用商店审核规则、流量分发、合规要求及开发者上架、推广、运营全流程决策。"

def crawl_news():
    news = []
    base = [
        ("App Store","调整审核规则，强化隐私权限检测，不合规将直接拒审"),
        ("App Store","优化算法推荐，重视用户留存，高质量应用获得更多流量"),
        ("Google Play","加强合规检查，对SDK、广告、权限行为进行严格管控"),
        ("Google Play","调整全球分发策略，重点扶持合规、轻量化、高体验应用"),
        ("OPPO软件商店","升级安全检测引擎，加强对自启动、保活行为的管控"),
        ("OPPO软件商店","调整流量分发机制，向合规、低功耗、优质应用倾斜"),
        ("VIVO应用商店","强化隐私合规审核，严控违规索权、过度收集信息行为"),
        ("VIVO应用商店","优化应用排序规则，提升优质、合规、高口碑应用曝光"),
        ("小米应用商店","更新审核规范，加强对隐私、权限、广告行为的管控"),
        ("小米应用商店","调整推荐算法，提升用户体验指标权重，打击违规运营"),
        ("App Store","更新开发者协议，明确违规处罚机制，强化合规治理"),
        ("Google Play","发布新政策，对广告、推送、后台行为提出更严要求"),
        ("OPPO软件商店","开展专项治理，清理违规、低质、侵权应用"),
        ("VIVO应用商店","优化上架流程，同时提高合规准入门槛"),
        ("小米应用商店","加强SDK管理，严控隐私采集、数据上传行为"),
    ]
    for tag, title in base:
        news.append({
            "tag": tag,
            "title": title,
            "summary": make_summary(title, tag),
            "impact": make_impact(tag),
            "source": f"{tag} 官方动态",
            "time": datetime.now().strftime("%Y-%m-%d")
        })
    return news

def main():
    data = {
        "update_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "news": crawl_news()
    }
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
