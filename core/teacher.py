from lib import common
from interface import common_interface

teacher_info = {
    "user": None
}


def login():
    while True:
        username = input("请输入用户名：").strip()
        if username == "":
            print("用户名不能为空！")
            continue

        password = input("请输入密码：").strip()

        flag, msg = common_interface.login_interface(
            username, password, user_type="teacher"
        )

        print(msg)
        if flag:
            teacher_info["user"] = username
            break


@common.auth("teacher")
def check_course():
    pass


@common.auth("teacher")
def choose_course():
    pass


@common.auth("teacher")
def check_stu_from_course():
    pass


@common.auth("teacher")
def change_score_from_student():
    pass


func_dic = {
    '1': login,
    '2': check_course,
    '3': choose_course,
    '4': check_stu_from_course,
    '5': change_score_from_student,
}


def teacher_view():
    while True:
        print("""
            - 1. 登陆
            - 2. 查看教授课程
            - 3. 选择教授课程
            - 4. 查看课程下学生
            - 5. 修改学生分数
            """
              )

        choice = input("请输入功能编号：").strip()
        if choice == "q":
            break

        if choice not in func_dic:
            print("输入有误，请重新输入！")
            continue

        func_dic.get(choice)()
