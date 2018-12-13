import ctypes, sys

def is_admin():
	try:
		return ctypes.windll.shell32.IsUserAnAdmin()
	except:
		return False


def blockIt(website):
	try:
		content = ''
			
		fp = open('C:\\Windows\\System32\\drivers\\etc\\hosts','a+')
		fp.seek(0)
		content = fp.read()
		if website in content:
			print("It is already blocked!")
		else:
			if "www" in website:
				domain = website.replace("www.","")
				fp.write("\n")
				fp.writelines("127.0.0.1 "+website+"\n")
				fp.writelines("127.0.0.1 "+domain+"\n")
				print("Blocked!")
			else:
				fp.write("\n")
				fp.writelines("127.0.0.1 "+website+"\n")
				fp.writelines("127.0.0.1 www."+website+"\n")
				print("Blocked!")

		fp.close()
		return True
	except:
		return False

def unblockIt(website):
	try:
		content = ''

		elem = []

		newElem = []

		finalContent = ''
			
		fp = open('C:\\Windows\\System32\\drivers\\etc\\hosts','r+')
		content = fp.read()
		fp.close()
		if website in content:
			elem = content.split("\n")
			for line in elem:
				if not website in line:
					newElem.append(line)
			finalContent = "\n".join(newElem)
			fp = open('C:\\Windows\\System32\\drivers\\etc\\hosts','w+')
			fp.write(finalContent)
			fp.close()
			print("Unblocked!")
		else:
			print("It is not in the blocked list")

		fp.close()
		return True
	except:
		return False
		

def main():
	if not is_admin():
		print("No Admin Access, asking for permission...")
		ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
	else:
		print("Website Blocker Script\n\n")
		print("Enter a choice to continue...\n")
		choice = str(input("Block (1) / Unblock (2) ? : "))
		if choice == "1":
			web = str(input("Enter a website name to block : "))
			if not blockIt(web):
				print("Error!")
		elif choice == "2":
			web = str(input("Enter a website name to unblock : "))
			if not unblockIt(web):
				print("Error!")

		else:
			print("Bad Choice!\n")

		while True:
			pass

if __name__ == '__main__':
	main()