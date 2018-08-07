import os
import ch8.ch8
import shutil


def print_dir(path):
    """
    传递一个路径，首先列出所有子目录名称，之后列出目录中文件的名称
    :param path:
    :return:
    """
    list = os.listdir(path)
    sort_list = sorted(list)
    index = 0
    while index < len(sort_list):
        if os.path.isdir(os.path.join(path, sort_list[index])):
            print(sort_list.pop(index))
        else:
            index += 1
            continue
    for file_name in sort_list:
        print(os.path.join(file_name))


def rotate(path, version=0, max_version=5):
    """
    轮滚旧文件
    :param path:
    :param version:
    :param max_version:
    :return:
    """
    # 构建一个路径名，在这个版本号
    if not os.path.exists(path):
        # 如过路径是不存在的
        raise IOError("'%s' 路径不存在" % path)
    version_path = ch8.make_version_path(path, version)
    if version + 1 > max_version:
        os.remove(version_path)
        return
    old_path = ch8.make_version_path(path, version + 1)
    # 判断新生成的版本路径是否存在
    if os.path.exists(old_path):
        rotate(path, version + 1)
    shutil.move(version_path, old_path)


print_dir(r"F:\python")
