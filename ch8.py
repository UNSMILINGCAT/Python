import os

path = r"F:\python\ch6.py"


def make_write_file():
    # if os.path.isfile(path):
    #     print("文件已存在，无法创建同名文件")
    # else:
    path = r"\\192.168.0.104\优创共享\a.txt"
    file = open(path, "a")
    file.write("""
    这是多行文件
    的内容
    """)
    file.close()


def make_read_file():
    file = open(path, "r")
    print(file.readline())
    file.close()
    del file


def split_fully(path):
    parent_path, name = os.path.split(path)
    if name is "":
        return (parent_path,)
    else:
        return split_fully(parent_path) + (name,)


print(split_fully(path))
