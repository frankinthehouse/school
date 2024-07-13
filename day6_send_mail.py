import smtplib,ssl
#去 email 的 mime 的 text import MIMEText 特定的小模組
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart
from email.header import Header
alot_receiver = ["fantasticseven1204@gmail.com","kiol726as@gmail.com"]


for receiver in alot_receiver:
    sender = "kiol726a@gmail.com"
    msg = MIMEMultipart()
    #MIMEMultipart 的字典 ["From"] = "key" 
    #發送人 

    msg["From"] = sender
    #收件者
    msg["To"] = receiver

    # 標題 跟 編碼格式
    header = Header("I LOVE U UNA baby","utf-8")

    # encode 是將 內容 轉成編碼格式
    msg["Subject"] = header.encode()

    # 信的內容
    body = "This is email send from python"

    msg.attach(MIMEText(body))

    ssl_context = ssl.create_default_context()

                        #google 的 特定網址跟端口
    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=ssl_context) as server:
        # 登入  帳號跟 應用程式密碼
        server.login(sender,"rtfz hdnm alob fubo")
        server.sendmail(sender,receiver,msg.as_string())

    print("success send email")