import email.message
#建立物件訊息
msg = email.message.EmailMessage()
msg["From"]="vivian.tajv@gmail.com"
msg["To"]="vivian.tajv@gmail.com"
msg["Subject"]="你好！"
#寄送純文字內容
msg.set_content("測試看看")

#寄送比較多樣式的內容(html)
#msg.add_alternative("<h3>呱呱國</h3>歡迎歡迎",subtype="html")

#連線到SMTP Server< 驗證寄件人身分送訊息
import smtplib
#搜尋 gmail smtp server 或是 yahoo smtp server
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("vivian.tajv@gmail.com","vivian950325")
server.send_message(msg)
server.close()