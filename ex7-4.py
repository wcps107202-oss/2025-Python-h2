'''

20. 主函式輸入 高與寬，編寫程式，其中自定義一函式，算矩形面積
'''
def area_fun(h,w):
  return h * w
h = int(input("please input heigh :"))
w = int(input("please input width :"))
print("area=",area_fun(h,w))
