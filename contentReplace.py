import getopt
import os
import sys
import re

### Readme: 在脚本文件contenReplace.py中第50行修改控制器原路径、51行修改控制器新路径。

# 查找函数：search_path 查找根路径 file_name 需要查找的文件名
def search(search_path, search_file_pattern, search_result):
    # 获取当前路径下地所有文件
    all_file = os.listdir(search_path)
    regex = re.compile(search_file_pattern)
    # 对于每一个文件
    for each_file in all_file:
        # 若文件为一个文件夹
        if os.path.isdir(search_path + os.sep + each_file):
            # 递归查找文件夹中的文件
            search(search_path + os.sep + each_file,
                   search_file_pattern, search_result)
        # 如果匹配被查找的文件名格式
        elif regex.match(each_file):
            # 输出路径
            search_result.append(search_path + os.sep + each_file)


# 替换 sed -i 's/old_str/new_str/'
# 文本替换 replace_file_name 需要替换的文件路径，replace_old_str 要替换的字符，replace_new_str 替换的字符


def replace(replace_file_name, replace_old_str, replace_new_str):
    # open()类创建一个file对象，可以通过调用file.方法对其进行操作，'r'为read only  'w'为write only
    f1 = open(replace_file_name, "r")
    content = f1.read()
    f1.close()
    t = content.replace(replace_old_str, replace_new_str)
    with open(replace_file_name, "w") as f2:
        f2.write(t)
    f2.close()


if __name__ == '__main__':
    result = []
    # 默认当前目录
    path = os.getcwd()

    # 正则表达式匹配目标文件名
    file_pattern = "dlc(.*).\$PJ"

    # 在此更改需要替换的路径
    old_str = "E:\MySE11-230(V7N5)_qingzhou2_di2pi_F1_20220606\control\Discon.dll"
    new_str = "E:\MySE11-230(V7N5)_qingzhou2_di2pi_F1_2022\control\Discon.dll"
    
    
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hp:f:o:n:", [
                                   "help", "path=", "file=", "old=", "new="])
    except getopt.GetoptError:
        print('usage: search_and_replace.py -p <path> -f <file_name_pattern> -o <old_str> -n <new_str>')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print(
                'usage: contentReplace.py -p <path> -f <file_name> -o <old_str> -n <new_str>')
            sys.exit()
        elif opt in ("-p", "--path"):
            path = arg
        elif opt in ("-f", "--file"):
            file_name = arg
        elif opt in ("-o", "--old"):
            old_str = arg
        elif opt in ("-n", "--new"):
            new_str = arg

    search(path, file_pattern, result)
    for file_name in result:
        replace(file_name, old_str, new_str)
        print("replace {} to {} in file {} successfully".format(
            old_str, new_str, file_name))


