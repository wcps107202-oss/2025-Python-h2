def get_day_message(day):
    match day:
        case "星期一":
            return "新的一週開始！加油！"
        case "星期二":
            return "繼續努力，還有四天！"
        case "星期三":
            return "週中了，堅持下去！"
        case "星期四":
            return "快到週末了！"
        case "星期五":
            return "TGIF！明天就是週末！"
        case "星期六" | "星期日":  # 多個值
            return "享受週末時光！"
        case _:
            return "請輸入有效的星期"

# 測試
days = ["星期一", "星期五", "星期日", "無效日期"]
for day in days:
    print(f"{day}: {get_day_message(day)}")
