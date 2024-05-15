import paramiko
from environs import Env


env = Env()
env.read_env()

# WARNING!!! Paramiko doesn’t work with my Cisco, Windows or other non-Unix system!
# Start script under Linux
# https://www.paramiko.org/faq.html

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(env('HOSTNAME'), username=env('USERNAME'), key_filename=env('KEY_FILENAME'))
# stdin, stdout, stderr = ssh.exec_command('ls -altr /opt/AntiSpamBot')
# print(stdout.read().decode())
stdin, stdout, stderr = ssh.exec_command('cat /opt/AntiSpamBot/logs.txt')
print(stdout.read().decode())
ssh.close()
