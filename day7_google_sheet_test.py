# google 表格 的 模組
import pygsheets

# 吃 google 的設定黨 git 
gs = pygsheets.authorize(service_file = "infinite-glow-430001-e9-82f4dd2eb476.json")

# 使用 url 開啟 表格 
sht = gs.open_by_url("https://docs.google.com/spreadsheets/d/1ZZA1Wx6XFdIMKmMf0rl4awiVcCy1FxcnDo9drtpwYkY/edit?gid=0#gid=0")

#sht = gs.open_by_url("https://docs.google.com/spreadsheets/d/1ZZA1Wx6XFdIMKmMf0rl4awiVcCy1FxcnDo9drtpwYkY/edit?gid=584450884#gid=584450884")

a1_value = sht[0].cell("A1").value
sht[0].update_value("B1","update by python")

"""
Dir = {}


a1_Value = sht[1].cell("A1").value

for i in range(3):
    if i == 0:
        continue
    key= sht[1].cell(A)

"""


#while 
#sht_value = sht[1].cell{"A"}
#sht_key = sht[1].cell



# 打印出來
#print(a1_value,b1_value)