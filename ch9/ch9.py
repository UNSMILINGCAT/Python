import sys
import getopt
import os

# fun = lambda x: x % 2 == 0
# filter_me = [2, 5, 2, 5, 6, 7, 5, 3, 2, 6, 12]
# result = filter(fun, filter_me)
# print(*result)
# cmdline_params = sys.argv[1:]
# opts, args = getopt.getopt(cmdline_params, "hc:", ['help', 'config='])
# for option, parameter in opts:
#     if option == '-h' or option == '--help':
#         print(r"-h or --help --显示帮助信息")
#         print("-c or --config=<file>--了解详细的配置文件")
#     if option in ('c', '--config'):
#         # 关于
#         print("使用配置文件 %s" % parameter)

if sys.platform == 'win32':
    print("运行于windows平台")
    command = "c:\\windows\\system32\\cmd.exe"
print("运行于 %s" % command)
os.system(command)
