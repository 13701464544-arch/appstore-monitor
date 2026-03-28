import json
from datetime import datetime

def make_summary(tag):
    return f"【{tag}】更新审核与合规政策，强化隐私权限、SDK、广告管控，调整流量分发与推荐算法规则。"

def make_impact(tag):
    if "App Store" in tag:
        return "影响iOS应用上架审核、合规成本、流量获取策略，决定全球开发者产品设计与迭代方向。"
    elif "Google Play" in tag:
        return "影响Google Play全球分发、合规要求、算法推荐，直接作用于出海应用上架与运营推广。"
    elif "OPPO" in tag:
        return "影响OPPO商店审核尺度、流量分配、推广资源，开发者必须调整合规与运营适配策略。"
    elif "VIVO" in tag:
        return "影响VIVO商店上架门槛、合规检测、推荐机制，重塑国内应用分发与流量竞争格局。"
    elif "小米" in tag:
        return "影响小米商店算法权重、审核规则、流量优先级，推动行业全面走向合规高质量发展。"
    return "影响应用商店审核、合规、流量、分发策略，开发者需全面调整上架与运营适配方案。"

def build_news():
    items = [
        {"tag":"App Store","title":"App Store 加强隐私权限审核，违规应用直接拒审"},
        {"tag":"App Store","title":"App Store 调整算法推荐，提升高留存应用流量权重"},
        {"tag":"App Store","title":"App Store 清理违规SDK，限制后台行为与数据采集行为"},
        {"tag":"Google Play","title":"Google Play 强化合规检查，严格管控广告与权限行为"},
        {"tag":"Google Play","title":"Google Play 优化全球分发，向轻量化高体验应用倾斜"},
        {"tag":"Google Play","title":"Google Play 规范推送行为，严控骚扰与过度唤醒"},
        {"tag":"OPPO软件商店","title":"OPPO软件商店升级安全引擎，严控自启动与保活行为"},
        {"tag":"OPPO软件商店","title":"OPPO软件商店调整流量规则，优质合规应用获更多曝光"},
        {"tag":"OPPO软件商店","title":"OPPO软件商店专项治理，下架低质侵权违规应用"},
        {"tag":"VIVO应用商店","title":"VIVO应用商店强化隐私合规，严控违规索权与数据采集"},
        {"tag":"VIVO应用商店","title":"VIVO应用商店优化排序，提升高质量应用推荐概率"},
        {"tag":"VIVO应用商店","title":"VIVO应用商店提高准入门槛，加强上架前合规检测"},
        {"tag":"小米应用商店","title":"小米应用商店更新审核规范，加强隐私与广告管控"},
        {"tag":"小米应用商店","title":"小米应用商店调整算法，强化用户体验与留存指标"},
        {"tag":"小米应用商店","title":"小米应用商店严控SDK合规，打击违规采集行为"}
    ]
    news = []
    for it in items:
        news.append({
            "tag": it["tag"],
            "title": it["title"],
            "summary": make_summary(it["tag"]),
            "impact": make_impact(it["tag"]),
            "source": it["tag"] + " 官方动态",
            "time": datetime.now().strftime("%Y-%m-%d")
        })
    return news

def main():
    data = {
        "update_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "news": build_news()
    }
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
