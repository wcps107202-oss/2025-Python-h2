correct_password = "python123"
attempts = 3

while attempts > 0:
    password = input(f"請輸入密碼（剩餘 {attempts} 次機會）：")
    
    if password == correct_password:
        print("密碼正確，登入成功！")
        break  # 跳出迴圈
    else:
        attempts -= 1
        if attempts > 0:
            print("密碼錯誤，請重試。")
        else:
            print("密碼錯誤次數過多，帳號已鎖定。")
