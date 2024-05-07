import smtplib
from environs import Env
from email.mime.text import MIMEText

env = Env()
env.read_env()

sender_email = env("SENDER_EMAIL")
receiver_email = env("RECEIVER_EMAIL")
subject = "Пробное письмо"
message = """Привет от Питона!<br>
            Python comes with a number of codecs built-in, either
            implemented as C functions or with dictionaries as mapping tables.
            The following table lists the codecs by name,<br>
            Если сервер Тильды не получит ожидаемый ответ,
            то будет еще две попытки повторного запроса на ваш сервер (всего 3 запроса).
            Запрос может отправляться не сразу, а с задержкой от 1 до 20 минут после публикации.
            Поэтому, если запрос не пришел сразу, то нужно убедиться, что он не пришел в указанное время.<br>
          """

mess = MIMEText(message, 'html')
mess['From'] = sender_email
mess['To'] = receiver_email
mess['Subject'] = subject

print(mess)

smtp_server = smtplib.SMTP(env("SMTP_SERVER"), 587)
smtp_server.starttls()
smtp_server.login(sender_email, env("SENDER_PASSWORD"))
smtp_server.sendmail(sender_email, receiver_email,  mess.as_string())
smtp_server.quit()
