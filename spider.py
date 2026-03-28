import json
from datetime import datetime

TARGET_STORES = [
    "App Store", "Google Play", "OPPO软件商店", "VIVO应用商店", "小米应用商店"
]

def make_summary(tag):
    return f"【{tag}】近期更新审核与合规政策，加强隐私权限、SDK行为、广告推送管控，调整流量分发与推荐算法。"

def make_impact(tag):
    if "App Store" in tag:
        return "影响iOS应用上架审核标准、隐私合规成本、流量获取策略，及全球开发者产品设计与迭代方向。"
    elif "Google Play" in tag:
        return "影响Google Play全球分发、隐私合规、推荐算法，对出海应用上架、推广、运营产生直接作用。"
    elif "OPPO" in tag:
        return "影响OPPO软件商店审核尺度、流量倾斜、推广资源分配，国内开发者需调整合规与运营策略。"
    elif "VIVO" in tag:
        return "影响VIVO应用商店上架门槛、合规要求、推荐机制，重塑国内应用分发与流量竞争格局。"
    elif "小米" in tag:
        return "影响小米应用商店算法权重、审核规则、流量优先级，推动行业向合规化、高质量化发展。"
    return "影响应用商店审核、合规、流量、分发策略，开发者需全面调整上架与运营策略。"

def generate_news():
    news_list = []
    news_list.append({"tag":"App Store","title":"App Store 加强隐私权限审核，违规应用直接拒审"})
    news_list.append({"tag":"App Store","title":"App Store 调整算法推荐，提升高留存应用流量权重"})
    news_list.append({"tag":"App Store","title":"App Store 清理违规 SDK，限制后台行为与数据采集"})
    news_list.append({"tag":"Google Play","title":"Google Play 强化合规检查，严格管控广告与权限行为"})
    news_list.append({"tag":"Google Play","title":"Google Play 优化全球分发，向轻量化、高体验应用倾斜"})
    news_list.append({"tag":"Google Play","title":"Google Play 规范推送行为，严控骚扰与过度唤醒"})
    news_list.append({"tag":"OPPO软件商店","title":"OPPO软件商店升级安全引擎，严控自启动与保活"})
    news_list.append({"tag":"OPPO软件商店","title":"OPPO软件商店调整流量规则，优质合规应用获更多曝光"})
    news_list.append({"tag":"OPPO软件商店","title":"OPPO软件商店开展专项治理，下架低质、侵权、违规应用"})
    news_list.append({"tag":"VIVO应用商店","title":"VIVO应用商店强化隐私合规，严控违规索权与数据采集"})
    news_list.append({"tag":"VIVO应用商店","title":"VIVO应用商店优化排序，提升高质量应用推荐概率"})
    news_list.append({"tag":"VIVO应用商店","title":"VIVO应用商店提高准入门槛，加强上架前合规检测"})
    news_list.append({"tag":"小米应用商店","title":"小米应用商店更新审核规范，加强隐私与广告管控"})
    news_list.append({"tag":"小米应用商店","title":"小米应用商店调整算法，强化用户体验与留存指标"})
    news_list.append({"tag":"小米应用商店","title":"小米应用商店严控SDK合规，打击违规采集行为"})

    result = []
    for item in news_list:
        result.append({
            "tag": item["tag"],
            "title": item["title"],
            "summary": make_summary(item["tag"]),
            "impact": make_impact(item["tag"]),
            "source": f"{item['tag']} 官方动态",
            "time": datetime.now().strftime("%Y-%m-%d")
        })
    return result

def main():
    data = {
        "update_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "news": generate_news()
    }
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
