import requests
import re
import subprocess

filehandle = requests.get('http://www.vpnbook.com/freevpn')
VPNBookHTML = filehandle.text

try:
   username = str(re.findall('Username:\s*<strong>(.*)<\/strong>',VPNBookHTML)[0])
except IndexError, e:
   username = ''
   
try:
   password = str(re.findall('Password:\s*<strong>(.*)<\/strong>',VPNBookHTML)[0])
except IndexError, e:
   password = ''
   
logindir = "LoginConfig.txt"
openvpn = ['openvpn','--config','vpnbook.ovpn'] # change based off desired county and port connections
#kill = 'sudo killall openvpn'

LoginConfig = open(logindir,'w')
LoginConfig.write(username + '\n' + password)
LoginConfig.close()
subprocess.Popen(openvpn)
