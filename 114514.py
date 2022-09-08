import sys
import random
import os
import platform

from collections import Counter

target = []
output = False
output_path = ''

logo = """
 _   _   _       _____   _____   _____   _____   _____   
| | | | | |     | ____| |_   _| |_   _| | ____| |  _  \  
| | | | | |     | |__     | |     | |   | |__   | |_| |  
| | | | | |     |  __|    | |     | |   |  __|  |  _  /  
| |_| | | |___  | |___    | |     | |   | |___  | | \ \  
\_____/ |_____| |_____|   |_|     |_|   |_____| |_|  \_\ 
Up-Low Letter     v.114514
"""

PRINT_HELP = """
-h  Print this help message
-t  Convert the text,must be include by ''
-f  Convert the text from files
-o  Output the result into a file
""".strip()

class Error(ValueError):
	pass

def OpenFiles(path,output):
	"""
	OpenFiles: 打开文件
	------------------------------------
	ToDO: 完善对读取文件中的异常处理
	"""
	with open(path, 'r') as f:
		code = f.read()
	func(code,output)

def func(cont,output):
	"""
	核心类（core）
	-------------------------------------
	if嵌套 判断字母__true____lower__add
			|	(random)|
			|			|__upper__add
			|
			|____false__add 
	(代码写的臭 if嵌套用时爽，事后一直火葬场)
	"""
	res = ""
	for i in cont:
		if i.isalpha():
			# print(f"i是{i}, 是字母")
			if  random.choice([True, False]):
				# print(1)
				letter = i.upper()
				res = "".join([res, letter])
			else:
				# print(0)
				letter = i.lower()
				res = "".join([res, letter])
		else:
			# print(f"i是{i}, 不是是字母")
			res = "".join([res, i])
	P_text(f"return:{res}")
	# print(output)
	# print(output_path)
	if output:
		OutPut(res)
	else:
		sys.exit(0)

def OutPut(cont):
	"""
	Output: 输出文件
	------------------------------------
	他甚至在文件检验是否存在
	"""
	# print(output_path)
	if os.path.exists(output_path):
		while True:
			inp = input("The file already exists. Do you want to overwrite it(yes/no)?")
			if inp == 'yes' or inp == 'y':
				print("Alright!They have been overwrite.That depends on your brilliant choice.Just YOLO!")
				break
			elif inp == 'no' or inp == 'n':
				print("Your file isn't be change, they are very safe! \nThank for your use")
				sys.exit(0)
	with open(output_path, 'w') as f:
		f.write(cont)
	sys.exit(0)

def P_text(word=""):
	"""
	P_text: 打印一个带logo的提示语
	------------------------------------
	其实都是混子代码（指join）
	"""
	print_list = []
	print_list.append(logo)
	print_list.append(word)
	print(("-" * 60 + '\n').join(print_list))

def CheckOS():
	if platform.system() != "Darwin":
		print("WARNING: It seems like you're using a non-Apple device, which is not cool!")


def get_help():
	P_text(PRINT_HELP)
	sys.exit(0)

key_list ={
	"-t": func,
	"-f": OpenFiles,
}

def Target(text):
	key = []
	key_i = []

	CheckOS()
	# 收集参数
	for i,t in enumerate(text):
		if t.startswith('-'):
			key.append(t)
			key_i.append(i)
			# print(f"key:{key},key_i{key_i}")

	# 判断是否输出
	if "-o" in key:
		global output
		output = True
		i = text.index("-o")
		global output_path
		output_path = text[i+1]

	# 参数查重
	c_repeat = dict(Counter(key))
	if [key for key,value in c_repeat.items()if value > 1] or ("-t" in key and "-f" in key) or ("-h" in key and ("-t" in key or "-f" in key)):
		raise Error("There are some parm is repetitive, please work out them at first.")

	# 解析参数
	for i,k in enumerate(key):
		if k not in key_list.keys():
			raise Error(f'Invalid keyword: {k}, Maybe you can try "-h" to get help.') 
		
		if k == '-h':
			get_help()

		if k in key_list.keys():
			# print(k,i)
			keyword = key_list[k]
			keyword_i = text[key_i[i] + 1]
			# print(keyword,keyword_i)
			keyword(keyword_i,output)


def main():
	CheckOS()
	target = sys.argv[1:]
	Target(target)


if __name__ == '__main__':
	main()