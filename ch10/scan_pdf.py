import os
import re


def print_pdf(root, dirs, files):
    for file in files:
        path = os.path.join(root, file)
        path = os.path.normcase(path)
        if re.search(r".*\.pdf", path):
            print(path)


def print_pdf_1(root, dir, files):
    for file in files:
        print(file)
        print(dir)
        path = os.path.join(dir, file)
        path = os.path.normcase(path)
        if not re.search(r".*\.pdf", path):
            continue
        if re.search(r".\.hu", path):
            continue
        print(path)


def print_regex():
    s = ('xcxxx', 'abcxxxabc', 'xyx', 'abc', 'x.x', 'axa', 'axxxxa', 'axxyx')
    a = filter(lambda s: re.match("[^x]*cxxx.*", s), s)
    print(*a)


# for root, dirs, files in os.walk('.'):
#     print_pdf(root, dirs, files)
# exit_dos = input("please enter any key to exit...")
# del exit_dos

if __name__ == '__main__':
    # print_regex()
    # for root, dirs, files in os.walk('.'):
    #     print_pdf_1(root, dirs, files)
    string="aboobahniag.pdf"
    print(re.search(r"[^boobah].*\.pdf",string))
