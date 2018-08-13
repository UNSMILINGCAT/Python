import os
import re


def print_pdf(regex, path):
    """

    :param regex:
    :param path:
    :return:
    """
    for files_path in os.walk(path):
        __scan_pdf(regex, files_path)


def __scan_pdf(regex, files_path=None):
    """
    根据正则来匹配相应的文件
    :param: regex 正则
    :param: files_path 文件的路径元组
    :return:
    """
    for file in files_path[2]:
        path = os.path.join(files_path[0], file)
        path = os.path.normcase(path)
        if re.search(regex, path):
            print(path)


if __name__ == '__main__':
    regex_1 = r"boobah.*\.pdf"
    regex_1 = r"[^boobah]"
    print_pdf(regex_1, ".")
    on = input()
