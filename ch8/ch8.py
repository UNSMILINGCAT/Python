import os
import time
import shutil

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


def print_dir(dir_path):
    for dir_name in os.listdir(dir_path):
        print(os.path.join(dir_path, dir_name))


def print_tree(dir_path):
    for name in os.listdir(dir_path):
        full_path = os.path.join(dir_path, name)
        if os.path.isfile(full_path):
            print(full_path)
        else:
            print_tree(full_path)


def print_dir_info(dir_path):
    for name in os.listdir(dir_path):
        full_path = os.path.join(dir_path, name)
        file_size = os.path.getsize(full_path)
        mod_time = time.ctime(os.path.getmtime(full_path))
        print("%s : %8d bytes, 修改 %s " % (name, file_size, mod_time))


def make_version_path(path, version):
    if version is 0:
        # 没有版本号，直接返回当前路径
        return path
    else:
        # 追加老的版本号
        return path + "." + str(version)


def rotate(path, version=0):
    # 构建一个路径名，在这个版本号
    if not os.path.exists(path):
        # 如过路径是不存在的
        raise IOError("'%s' 路径不存在" % path)
    version_path = make_version_path(path, version)

    old_path = make_version_path(path, version + 1)
    # 判断新生成的版本路径是否存在
    if os.path.exists(old_path):
        rotate(path, version + 1)
    shutil.move(version_path, old_path)


def rotate_log_file(path):
    if os.path.exists(path) is not True:
        new_file = open(path, "w")
        new_file.write("1111111")
        del new_file
    rotate(path)


# print(split_fully(path))
# # 取文件名的后缀
# print(os.path.splitext("image.jpg.txt")[1])
# print("nihao"[2])
# # 规范化或“清理”路径
# print(os.path.normpath(r"c:\Program File\java\..\Python30"))
# print(os.path.abspath(r"..\python"))
# 判断路径是否存在
# print(os.path.exists(r"..\python"))
# print_dir(r"F:\python")
# print_dir(r"c:\users\不笑猫\Desktop")
# print_tree(r"F:\python")
# print_dir_info(r"F:\python")
path = r"F:\Python\demo.log"
rotate_log_file(path)
# list = [0, 2, 56, 2]
# del list[1]
# print(list)
# print(list[1])
