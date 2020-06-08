import smtplib

frome = "yossib26@gmail.com"

# try:
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.ehlo()
# server.starttls()


server.login("yossib26@gmail.com", "25182006")

server.sendmail(frome, frome, "aaaaaaaaaaaaaa")
server.close()

# except:
#     print("Error !!!!!!!!")

