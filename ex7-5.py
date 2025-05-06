'''
21. 主函式輸入 輸入 a 小時 b 分， 其中自定義一函式，時間換算，輸出  x 分
'''
def cal_min(a,b):
  return a*60 + b
a = int(input("please input num a (hr) :"))
b = int(input("please input num b (min):"))
print("x =",cal_min(a,b))
