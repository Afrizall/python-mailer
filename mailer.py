import sys, smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

    
def kirim_email(sender, target):
    mail.sendmail(sender, target, pesan.as_string())
    print "[+] Sending To : " + target 

host = raw_input("Host SMTP : ")
port = raw_input("Port SMTP : ")
user = raw_input("SMTP Username : ")
password = raw_input("SMTP Password : ")
sender_mail = str(raw_input("Sender : "))
judul = raw_input("Subject : ")
html_file = raw_input("File HTML : ")
file_list = raw_input("Mail List : ")

mail = smtplib.SMTP(host, port)
mail.ehlo()
mail.starttls()
mail.login(user, password)

html = open(html_file, "r").read()
html = MIMEText(html, 'html')

pecah_mail_list = open(file_list, "r").read().split("\n")

for target in pecah_mail_list :

    if not target :
        continue

    pesan = MIMEMultipart('alternative')
    pesan['Subject'] = judul
    pesan['From'] = sender_mail
    pesan['To'] = target
    pesan.attach(html)

    kirim_email(sender_mail, target)

mail.quit()
