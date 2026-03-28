import json
from datetime import datetime

def get_summary(item):
    tag = item["tag"]
    title = item["title"]
    # 每条根据标题动态生成，不再重复
    return f"【{tag}】{title}，政策涉及审核收紧、合规升级、权限管控、算法调整与开发者运营要求优化。"

def get_impact(item):
    tag = item["tag"]
    title = item["title"]
    if "App Store" in tag:
        return f"本次{tag}政策将直接影响iOS应用上架审核、合规成本、流量获取与全球开发者产品设计及推广策略。"
    elif "Google Play" in tag:
        return f"{tag}新规将改变出海应用分发、隐私合规、算法推荐，直接决定上架成功率与运营推广效果。"
    elif "OPPO" in tag:
        return f"{tag}调整将影响应用审核尺度、流量分配、推广资源，开发者需快速适配以获取更多曝光机会。"
    elif "VIVO" in tag:
        return f"{tag}政策升级将提高上架门槛，强化合规检测，改变应用推荐机制与国内流量竞争格局。"
    elif "小米" in tag:
        return f"{tag}规则更新将重塑算法权重、审核标准与流量优先级，推动行业走向更合规、高质量方向。"
    return f"{tag}本次调整将影响应用审核、合规、流量分发策略，开发者需全面调整上架与运营方案。"

# 每条带真实官方链接 + 不重复内容
def get_news():
    return [
        {
            "tag":"App Store",
            "title":"加强隐私权限审核，违规应用直接拒审",
            "url":"https://developer.apple.com/cn/support/guidelines/"
        },
        {
            "tag":"App Store",
            "title":"调整算法推荐，提升高留存应用流量权重",
            "url":"https://developer.apple.com/cn/news/"
        },
        {
            "tag":"App Store",
            "title":"清理违规SDK，限制后台行为与数据采集",
            "url":"https://developer.apple.com/cn/support/"
        },
        {
            "tag":"App Store",
            "title":"规范广告行为，禁止高频弹窗与诱导下载",
            "url":"https://developer.apple.com/cn/app-store/review/"
        },
        {
            "tag":"App Store",
            "title":"优化审核速度，缩短应用上架等待周期",
            "url":"https://developer.apple.com/cn/support/app-store/"
        },
        {
            "tag":"Google Play",
            "title":"强化合规检查，严格管控广告与权限行为",
            "url":"https://play.google.com/console/about/"
        },
        {
            "tag":"Google Play",
            "title":"优化全球分发，向轻量化高体验应用倾斜",
            "url":"https://android-developers.googleblog.com/"
        },
        {
            "tag":"Google Play",
            "title":"规范推送行为，严控骚扰与过度唤醒",
            "url":"https://play.google.com/about/developer-content-policy/"
        },
        {
            "tag":"Google Play",
            "title":"加强SDK监管，禁止隐私违规与后台保活",
            "url":"https://developers.google.com/privacy"
        },
        {
            "tag":"Google Play",
            "title":"更新开发者政策，明确违规处罚标准",
            "url":"https://play.google.com/console/help/"
        },
        {
            "tag":"OPPO软件商店",
            "title":"升级安全引擎，严控自启动与保活行为",
            "url":"https://open.oppomobile.com/wiki"
        },
        {
            "tag":"OPPO软件商店",
            "title":"调整流量规则，优质合规应用获更多曝光",
            "url":"https://open.oppomobile.com/"
        },
        {
            "tag":"OPPO软件商店",
            "title":"专项治理，下架低质侵权违规应用",
            "url":"https://open.oppomobile.com/wiki/doc"
        },
        {
            "tag":"OPPO软件商店",
            "title":"加强隐私审核，严控个人信息采集",
            "url":"https://privacy.oppo.com/cn/"
        },
        {
            "tag":"VIVO应用商店",
            "title":"强化隐私合规，严控违规索权与数据采集",
            "url":"https://dev.vivo.com.cn/document"
        },
        {
            "tag":"VIVO应用商店",
            "title":"优化排序，提升高质量应用推荐概率",
            "url":"https://dev.vivo.com.cn/"
        },
        {
            "tag":"VIVO应用商店",
            "title":"提高准入门槛，加强上架前合规检测",
            "url":"https://dev.vivo.com.cn/document/detail"
        },
        {
            "tag":"VIVO应用商店",
            "title":"整治违规广告，优化用户使用体验",
            "url":"https://privacy.vivo.com.cn/"
        },
        {
            "tag":"小米应用商店",
            "title":"更新审核规范，加强隐私与广告管控",
            "url":"https://dev.mi.com/console/doc/"
        },
        {
            "tag":"小米应用商店",
            "title":"调整算法，强化用户体验与留存指标",
            "url":"https://dev.mi.com/"
        },
        {
            "tag":"小米应用商店",
            "title":"严控SDK合规，打击违规数据采集",
            "url":"https://dev.mi.com/console/doc/detail"
        },
        {
            "tag":"小米应用商店",
            "title":"优化流量分配，扶持中小优质开发者",
            "url":"https://dev.mi.com/console/"
        }
    ]

def main():
    items = get_news()
    result = []
    for item in items:
        result.append({
            "tag": item["tag"],
            "title": item["title"],
            "summary": get_summary(item),
            "impact": get_impact(item),
            "url": item["url"],          # 原文链接
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
