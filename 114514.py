import sys
import random


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
""".strip()

def func(text):
    """
    核心类（core）
    -------------------------------------
    if嵌套 判断字母__true____lower__add
            |    (random)|
            |            |__upper__add
            |
            |____false__add 
    (代码写的臭 if嵌套用时爽，事后一直火葬场)
    """
    res = ""
    for i in text:
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
    return res

def OpenFiles(path):
    """
    OpenFiles: 打开文件
    ------------------------------------
    ToDO: 完善对读取文件中的异常处理
    """
    with open(path, 'r') as f:
        code = f.read()
    return code


def P_text(word=''):
    """
    P_text: 打印一个带logo的提示语
    ------------------------------------
    其实都是混子代码（指join）
    """
    if word:
        print_list = []
        print_list.append(logo)
        print_list.append(word)
        w = ''
        print(w.join(print_list))
    else:
        print(logo)

def Target(text):
    """
     Target: 判断传入的参数
    -----------------------------------
     if嵌套 验空==>判断参数
     (if嵌套不是好方法，小孩不要学 逃)
    """
    # print(text)
    if text:
        if text[0] == '-h':
            P_text(PRINT_HELP)

        elif text[0] == '-t':
            # print("-t")
            res = func(text[1])
            P_text()
            print(f"return: {res}")


        elif text[0] == '-f':
            # print("-f")
            P_text("Reading files....")
            files = OpenFiles(text[1])
            res = func(files)
            P_text()
            print(f"return: {res}")


        else:
            print(f'Invalid keyword: {text}, Maybe you can try "-h" to get help.')

    else:
        # print("他是空的")
        P_text(PRINT_HELP)
        return 0


def main():
    """
    这个不是main函数 ;)
    This isn't a main funication
    """
    target = sys.argv[1:] #传入参数
    # print(f"main:{target}")
    Target(target)



if __name__ == '__main__':
    main()
