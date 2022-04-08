from __future__ import print_function
from pyscreeze import unicode
from win32gui import FindWindow, FindWindowEx, SetWindowText
import ctypes, sys


def get_handle_num(handle_title):
    print(handle_title)
    handle_num_all = []
    """通过句柄标题获取句柄编号"""
    handle_num = FindWindow(None, handle_title)  # 搜索句柄标题，获取句柄编号
    if handle_num == 0:
        print("目标程序未启动,即将中止！")
        return None  # 返回异常
    else:
        handle_num_all.append(handle_num)
        while True:
            handle_num = FindWindowEx(None, handle_num, None, handle_title)
            if handle_num == 0:
                break
            else:
                handle_num_all.append(handle_num)
        return handle_num_all


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin():
    # 将要运行的代码加到这里
    handlenum = get_handle_num('阴阳师-网易游戏')
    for i in range(len(handlenum)):
        print("修改句柄" + str(handlenum[i]) + "为阴阳师" + str(i + 1) + "号")
        SetWindowText(handlenum[i], "阴阳师" + str(i + 1) + "号")
else:
    if sys.version_info[0] == 3:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    else:  # in python2.x
        ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)

if __name__ == '__main__':
    is_admin()
