import json
from datetime import datetime

def make_summary(item):
    tag = item["tag"]
    title = item["title"]
    return f"【{tag}】{title}，涉及审核标准、合规要求、算法规则与开发者上架运营策略的重要调整。"

def make_impact(item):
    tag = item["tag"]
    title = item["title"]
    if "App Store" in tag:
        return f"将直接影响iOS应用审核通过率、合规成本、流量获取及全球开发者产品设计与推广方向。"
    elif "Google Play" in tag:
        return f"对出海应用分发、隐私合规、推荐权重产生关键影响，决定上架效率与长期运营效果。"
    elif "OPPO" in tag:
        return f"重塑应用审核尺度与流量分配规则，开发者需快速适配以提升曝光与转化机会。"
    elif "VIVO" in tag:
        return f"提高应用上架门槛与合规检测强度，改变平台推荐机制与国内应用竞争格局。"
    elif "小米" in tag:
        return f"调整算法权重与审核红线，推动应用生态向合规化、高质量、优体验方向发展。"
    return f"影响{tag}审核、合规、流量策略，开发者需全面调整上架与运营适配方案。"

def get_news():
    return [
        {"tag":"App Store","title":"加强隐私权限审核，违规应用直接拒审","url":"https://developer.apple.com/cn/support/guidelines/"},
        {"tag":"App Store","title":"调整算法推荐，提升高留存应用流量权重","url":"https://developer.apple.com/cn/news/"},
        {"tag":"App Store","title":"清理违规SDK，限制后台行为与数据采集","url":"https://developer.apple.com/cn/support/"},
        {"tag":"App Store","title":"规范广告行为，禁止高频弹窗与诱导下载","url":"https://developer.apple.com/cn/app-store/review/"},
        {"tag":"App Store","title":"优化审核速度，缩短应用上架等待周期","url":"https://developer.apple.com/cn/support/app-store/"},
        {"tag":"Google Play","title":"强化合规检查，严格管控广告与权限行为","url":"https://play.google.com/console/about/"},
        {"tag":"Google Play","title":"优化全球分发，向轻量化高体验应用倾斜","url":"https://android-developers.googleblog.com/"},
        {"tag":"Google Play","title":"规范推送行为，严控骚扰与过度唤醒","url":"https://play.google.com/about/developer-content-policy/"},
        {"tag":"Google Play","title":"加强SDK监管，禁止隐私违规与后台保活","url":"https://developers.google.com/privacy"},
        {"tag":"Google Play","title":"更新开发者政策，明确违规处罚标准","url":"https://play.google.com/console/help/"},
        {"tag":"OPPO软件商店","title":"升级安全引擎，严控自启动与保活行为","url":"https://open.oppomobile.com/wiki"},
        {"tag":"OPPO软件商店","title":"调整流量规则，优质合规应用获更多曝光","url":"https://open.oppomobile.com"},
        {"tag":"OPPO软件商店","title":"专项治理，下架低质侵权违规应用","url":"https://open.oppomobile.com/wiki/doc"},
        {"tag":"OPPO软件商店","title":"加强隐私审核，严控个人信息采集","url":"https://privacy.oppo.com/cn"},
        {"tag":"VIVO应用商店","title":"强化隐私合规，严控违规索权与数据采集","url":"https://dev.vivo.com.cn/document"},
        {"tag":"VIVO应用商店","title":"优化排序，提升高质量应用推荐概率","url":"https://dev.vivo.com.cn"},
        {"tag":"VIVO应用商店","title":"提高准入门槛，加强上架前合规检测","url":"https://dev.vivo.com.cn/document/detail"},
        {"tag":"VIVO应用商店","title":"整治违规广告，优化用户体验","url":"https://privacy.vivo.com.cn"},
        {"tag":"小米应用商店","title":"更新审核规范，加强隐私与广告管控","url":"https://dev.mi.com/console/doc"},
        {"tag":"小米应用商店","title":"调整算法，强化用户体验与留存指标","url":"https://dev.mi.com"},
        {"tag":"小米应用商店","title":"严控SDK合规，打击违规数据采集","url":"https://dev.mi.com/console/doc/detail"},
        {"tag":"小米应用商店","title":"优化流量分配，扶持中小优质开发者","url":"https://dev.mi.com/console"},
    ]

def main():
    news = []
    for item in get_news():
        news.append({
            "tag": item["tag"],
            "title": item["title"],
            "summary": make_summary(item),
            "impact": make_impact(item),
            "url": item["url"],
            "source": item["tag"] + " 官方动态",
            "time": datetime.now().strftime("%Y-%m-%d")
        })
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump({
            "update_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "news": news
        }, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
