#Write one or more cronjobs using Python which would monitor multiple (at least 3) 
# services on different servers and log their responses in a text file accordingly. If a service fails,
# send an email to the concerned authority with proper information.
import json
import argparse
import sys
import paramiko
import smtplib
from email.mime.text import MIMEText

config_path = 'config.json'
def send_email(to_address, subject, body):
	try:
		msg = MIMEText(body)
		msg['Subject'] = subject
		msg['From'] = "test@test.com"
		msg['To'] = 'test@test.com'
		fromaddr = "test@test.com"
        
		server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		server.login(fromaddr, '******')
		server.sendmail(fromaddr, [to_address], msg.as_string())
		server.quit()
	except Exception as e:
		raise e

class sshConnect():
	def __init__(self, **kwargs):
		self._validateParams(**kwargs)
		self.hostAddress = kwargs['hostAddress']
		self.username = kwargs['username']
		self.password = kwargs.get("password", None)
		self.sshKey = kwargs.get("sshKey",None)
	
	def _connectionOpen(self):
		self.ssh_client = paramiko.SSHClient()
		self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		self.ssh_client.connect(hostname=self.hostAddress, username=self.username, password=self.password)


	def _connectionClose(self):
		self.ssh_client.close()

	def _discUsage(self):
		command = "df -h / | tail -1 | awk -F' ' '{print $5}'"
		return command

	def _memoryUsage(self):
		#command = "free -g | head -2 | tail -1 | awk -F' ' '{print $4}'"
		command = "top -l 1 -s 0 | grep PhysMem | awk -F' ' '{print $6}'"
		return command

	def _serviceResponse(self, command, command_type):
		self._connectionOpen()
		stdin,stdout,stderr = self.ssh_client.exec_command(command)
		err = stderr.readlines()
		if err:
			opts = {
					'subject':"Error detected for {}".format(self.hostAddress),
					'body':err,
					'to_address':"test@test.com"
				}
			send_email(**opts)
		result = stdout.readlines()
		if result:
			opts = {
					'subject':"{} Usage for Host {}".format(command_type, self.hostAddress),
					'body':result[0],
					'to_address':'test@test.com'    
				}
			send_email(**opts)
		self._connectionClose()

	def _validateParams(self, **kwargs):
		params = ['hostAddress', 'username', 'password']
		for param in params:
			if param not in kwargs.keys() or kwargs.get(param, None) is None:
				raise Exception('{} is required, Please provide {}'.format(param, param))



if __name__ == "__main__":
	file_obj = open(config_path, 'r')
	config_data = file_obj.read()
	try:
		config_data = json.loads(config_data)
	except Exception as e:
		raise Exception("invalid json file")

	try:
		for params in config_data:
			service = sshConnect(**params)
			service,service._serviceResponse(service._memoryUsage(), 'Memory')
			service,service._serviceResponse(service._discUsage(), 'Disc')
	except Exception as e:
		print(str(e))
        sys.exit(1)