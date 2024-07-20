import pygsheets

gs = pygsheets.authorize(service_file = ".infinite-glow-430001-e9-82f4dd2eb476.json")

sht = gs.open_by_url("https://docs.google.com/spreadsheets/d/1ZZA1Wx6XFdIMKmMf0rl4awiVcCy1FxcnDo9drtpwYkY/edit?gid=0#gid=0")

b1value = sht[1].cell("B1").value

#print(b1value)
"""
for i in range(6):
    if i == 0 :
        continue

    BValue = sht[1].cell("B"+str(i+1)).value
    
    SPLIT = BValue.split("@")
    if SPLIT[1] != "123.com":
        print("X",SPLIT[0],SPLIT[1])
    elif SPLIT[1] == "123.com":
        print("V",SPLIT[0],SPLIT[1])
    else :
        print(ERROR)
"""

for i in range(6):
    newi = i+1
    if newi == 1 :
        continue
    mail = sht[1].cell("B"+str(newi)).value
    mail_split = mail.split("@")
    
    sht[1].update_value("C"+str(newi),mail_split[1])
    


