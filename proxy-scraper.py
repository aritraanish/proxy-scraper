import cloudscraper
import re
import os

# Promts

print("Script Made by AK")
print("")
maxtime = input("Enter the proxy speed in ms: ")
print("")

print("Poxy type:")
print("HTTP\t:\th")
print("HTTPS\t:\ts")
print("SOCKS4\t:\t4")
print("SOCKS5\t:\t5")
print("For all\t:\ta")
types = input("Enter your choice: ")

print("")
print("Anonymity level:")
print("High\t:\t4")
print("Medium\t:\t3")
print("Low\t:\t2")
print("No\t:\t1")
print("You can also combine multiple levels\n")
anon = input("Enter your choice: ")

print("")
print("Format type:")
print("IP:Port  :  1")
print("Protocol IP Port  :  2")
form = input("Enter your choice: ")

# Conditional checks

if maxtime.isdigit() != True:
	print("Proxy speed has to be a number!!")
	exit()

if (form != '1' and form != '2'):
	print("\nWrong format choice")
	exit()

print("")
print("Scraping proxy for you please wait. Script made by AK")
print("\n\n")

if types == 'a':
	url = 'https://hidemy.name/en/proxy-list/?maxtime={}&anon={}'.format(maxtime, anon)
elif types == 'h' or types == 's' or types == '4' or types == '5':
	url = 'https://hidemy.name/en/proxy-list/?maxtime={}&type={}&anon={}'.format(maxtime, types, anon)
else:
	print("Unknown proxy type selected!!")
	exit()

# Creating Cloudscraper instance

scraper = cloudscraper.create_scraper(browser='chrome')

# Downloading the website and writting in a file

a = scraper.get(url).text
endoded = a.encode("utf8")
with open('file.txt', 'wb') as file:
	file.write(endoded)



#These lines of codes are for Linux operating system

#----------------------------------------------------------------------------------
'''
protocol = os.popen("cat file.html | grep -o '<td>SOCKS4</td>\|<td>HTTP</td>\|<td>HTTPS</td>\|<td>SOCKS5</td>' | cut -c 5- | cut -d '<' -f 1")
ip = os.popen("cat file.html | grep -o '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}' | tail -n +2")
port = os.popen("cat file.html | grep -o '<td>[0-9]\{1,6\}</td>' | cut -c 5- | cut -d '<' -f 1")

protocol = protocol.readlines()
ip = ip.readlines()
port = port.readlines()


if len(ip) < len(protocol):
	ip = os.popen("cat file.html | grep -o '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}'")
	ip = ip.readlines()

if len(protocol) == 0 or len(ip) == 0 or len(port) == 0:
	print("Sorry no proxy found with that filter!!")
	exit()
 
count = 0
for i in protocol:
	protocol[count] = protocol[count][:-1]
	count = count + 1

count = 0
for i in ip:
	ip[count] = ip[count][:-1]
	count = count + 1

count = 0
for i in port:
	port[count] = port[count][:-1]
	count = count + 1

if len(protocol) == len(ip) == len(port):
	count = 0
	for i in protocol:
		print('{}\t{}\t{}'.format(protocol[count].lower(), ip[count], port[count]))
		count = count + 1

else:
	print("number of protocol/ip/port doesnot match")
	exit()

os.system('rm file.txt')
'''
#-----------------------------------------------------------------------------------

# Reading the file

lines = ''
with open('file.txt', 'rb') as file:
	for i in file:
		lines = lines + str(i)



# Searching for proxies

ip = re.findall('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', lines)
protocol = re.findall('<td>SOCKS4</td>|<td>SOCKS5</td>|<td>HTTP</td>|<td>HTTP, SOCKS4, SOCKS5</td>|<td>SOCKS4, SOCKS5</td>|<td>HTTP, SOCKS5</td>|<td>HTTP, SOCKS4</td>', lines)
port = re.findall('<td>[0-9]{1,5}</td>', lines)


# Checking if proxies were found


if (len(ip) == 0 or len(protocol) == 0 or len(port) == 0):
	print("No proxies found with that filter")
	os.remove("file.txt")
	exit()

counter = 0
for i in protocol:
	protocol[counter] = protocol[counter][4:][:-5].lower()
	counter = counter + 1

counter = 0
for i in port:
	port[counter] = port[counter][4:][:-5]
	counter = counter + 1


# Removing own IP if it exists in the list

if len(ip) > len(port):
	ip = ip[1:]


# Printing the proxies

counter = 0
if (len(ip) == len(protocol) == len(port)):
	for i in ip:
		
		if form == '1':
			print('{}:{}'.format(ip[counter], port[counter]))
		
		if form == '2':
			print('{}\t{}\t{}'.format(protocol[counter], ip[counter], port[counter]))
		
		counter = counter + 1
	print("\n")

else:
	print("Numbers of ip/port mismatch!!")
os.remove("file.txt")
exit()