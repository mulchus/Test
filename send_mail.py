import smtplib
from environs import Env

env = Env()
env.read_env()

sender_email = env("SENDER_EMAIL")
receiver_email = env("RECEIVER_EMAIL")
message = "Привет от Питона!"

smtp_server = smtplib.SMTP(env("SMTP_SERVER"), 587)
smtp_server.starttls()
smtp_server.login(sender_email, env("SENDER_PASSWORD"))
smtp_server.sendmail(sender_email, receiver_email, message)
smtp_server.quit()
