import json
from datetime import datetime

def get_summary(tag):
    return f"【{tag}】近期更新应用审核、合规与隐私政策，调整推荐算法与流量分配，加强SDK与广告行为管控。"

def get_impact(tag):
    if tag == "App Store":
        return "影响iOS应用上架审核标准、合规成本、流量获取策略，全球开发者需调整产品与运营方案。"
    elif tag == "Google Play":
        return "影响Google Play全球分发政策、隐私合规、推荐算法，直接决定出海应用的上架与推广效果。"
    elif tag == "OPPO软件商店":
        return "影响OPPO应用审核尺度、流量分配、推广资源，开发者需适配新规则以获取更多曝光机会。"
    elif tag == "VIVO应用商店":
        return "影响VIVO应用上架门槛、合规检测、推荐机制，将重塑国内应用分发与流量竞争格局。"
    elif tag == "小米应用商店":
        return "影响小米应用商店算法权重、审核规则、流量优先级，推动行业走向合规与高质量发展。"
    return "影响应用商店审核、合规、流量分发策略，开发者需全面调整上架与运营适配方案。"

def get_news():
    return [
        {"tag": "App Store", "title": "App Store 加强隐私权限审核，违规应用直接拒审"},
        {"tag": "App Store", "title": "App Store 调整算法推荐，提升高留存应用流量权重"},
        {"tag": "App Store", "title": "App Store 清理违规SDK，限制后台行为与数据采集"},
        {"tag": "App Store", "title": "App Store 规范广告行为，禁止高频弹窗与诱导下载"},
        {"tag": "App Store", "title": "App Store 优化审核速度，缩短应用上架等待周期"},
        {"tag": "Google Play", "title": "Google Play 强化合规检查，严格管控广告与权限行为"},
        {"tag": "Google Play", "title": "Google Play 优化全球分发，向轻量化高体验应用倾斜"},
        {"tag": "Google Play", "title": "Google Play 规范推送行为，严控骚扰与过度唤醒"},
        {"tag": "Google Play", "title": "Google Play 加强SDK监管，禁止隐私违规与后台保活"},
        {"tag": "Google Play", "title": "Google Play 更新开发者政策，明确违规处罚标准"},
        {"tag": "OPPO软件商店", "title": "OPPO软件商店升级安全引擎，严控自启动与保活行为"},
        {"tag": "OPPO软件商店", "title": "OPPO软件商店调整流量规则，优质合规应用获更多曝光"},
        {"tag": "OPPO软件商店", "title": "OPPO软件商店专项治理，下架低质侵权违规应用"},
        {"tag": "OPPO软件商店", "title": "OPPO软件商店加强隐私审核，严控个人信息采集"},
        {"tag": "VIVO应用商店", "title": "VIVO应用商店强化隐私合规，严控违规索权与数据采集"},
        {"tag": "VIVO应用商店", "title": "VIVO应用商店优化排序，提升高质量应用推荐概率"},
        {"tag": "VIVO应用商店", "title": "VIVO应用商店提高准入门槛，加强上架前合规检测"},
        {"tag": "VIVO应用商店", "title": "VIVO应用商店整治违规广告，优化用户使用体验"},
        {"tag": "小米应用商店", "title": "小米应用商店更新审核规范，加强隐私与广告管控"},
        {"tag": "小米应用商店", "title": "小米应用商店调整算法，强化用户体验与留存指标"},
        {"tag": "小米应用商店", "title": "小米应用商店严控SDK合规，打击违规数据采集行为"},
        {"tag": "小米应用商店", "title": "小米应用商店优化流量分配，扶持中小优质开发者"}
    ]

def main():
    news = get_news()
    result = []
    for item in news:
        result.append({
            "tag": item["tag"],
            "title": item["title"],
            "summary": get_summary(item["tag"]),
            "impact": get_impact(item["tag"]),
            "source": item["tag"] + " 官方动态",
            "time": datetime.now().strftime("%Y-%m-%d")
        })

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump({
            "update_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "news": result
        }, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
