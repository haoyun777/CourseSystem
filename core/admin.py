from interface import admin_interface
from lib import common


admin_info = {
    "user": None
}

def register():
    while True:
        username = input("请输入用户名：").strip()
        password = input("请输入密码：").strip()
        re_password = input("请确认密码：").strip()

        if password == re_password:
            pass
        else:
            print("两次输入的密码不一致，请重新输入！")
            continue

        flag, msg = admin_interface.admin_register_interface(
            username, password
        )

        print(msg)
        if flag:
            break


def login():
    while True:
        username = input("请输入用户名：").strip()
        password = input("请输入密码：").strip()

        flag, msg = admin_interface.admin_login_interface(
            username, password
        )

        print(msg)
        if flag:
            admin_info["user"] = username
            break





@common.auth("admin")
def create_school():
    while True:
        # 1. 输入学校的名称和地址
        school_name = input("请输入学校名称：").strip()
        school_addr = input("请输入学校地址：").strip()

        # 2. 调用接口保存学校
        flag, msg = admin_interface.create_school_interface(
            school_name, school_addr, admin_info.get("user")
        )

        print(msg)

        if flag:
            break


@common.auth("admin")
def create_course():
    pass


@common.auth("admin")
def create_teacher():
    pass


func_dic = {
    '1': register,
    '2': login,
    '3': create_school,
    '4': create_course,
    '5': create_teacher,
}


def admin_view():
    while True:
        print("""
            - 1. 注册
            - 2. 登陆
            - 3. 创建学校
            - 4. 创建课程
            - 5. 创建讲师
            """
              )

        choice = input("请输入功能编号：").strip()
        if choice == "q":
            break

        if choice not in func_dic:
            print("输入有误，请重新输入！")
            continue

        func_dic.get(choice)()
