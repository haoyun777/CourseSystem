from lib import common
from interface import student_interface
from interface import common_interface

student_info = {
    "user": ""
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

        flag, msg = student_interface.student_register_interface(
            username, password
        )

        print(msg)
        if flag:
            break


def login():
    while True:
        username = input("请输入用户名：").strip()
        if not username:
            print("用户名不能为空！")
            continue

        password = input("请输入密码：").strip()

        flag, msg = common_interface.login_interface(
            username, password, user_type="student"
        )

        print(msg)
        if flag:
            student_info["user"] = username
            break


@common.auth("student")
def choice_school():
    while True:
        flag, school_list = common_interface.get_all_school_interface()
        if not flag:
            print(school_list)
        for index, school_name in enumerate(school_list):
            print(f"编号：{index}      学校名：【{school_name}】")

        choice = input("请输入选择的学校编号：").strip()
        if not choice.isdigit():
            print("输入有误！")
            continue

        choice = int(choice)

        if choice not in range(len(school_list)):
            print("输入编号有误！")
            continue

        school_name = school_list[choice]

        flag, msg = student_interface.add_school_interface(
            school_name, student_info.get("user")
        )

        print(msg)
        if flag:
            break


@common.auth("student")
def choice_course():
    while True:
        # 1.获取当前学生所在学校的课程列表
        flag, course_list = student_interface.get_course_list_interface(
            student_info.get("user")
        )

        if not flag:
            print(course_list)
            break

        # 2.打印课程列表
        for index, course in enumerate(course_list):
            print(f"编号：{index}      课程：【{course}】")

        # 3.选择课程
        choice = input("请输入选择的课程编号：").strip()
        if not choice.isdigit():
            print("输入有误！")
            continue

        choice = int(choice)

        if choice not in range(len(course_list)):
            print("输入编号有误！")
            continue

        course_name = course_list[choice]

        # 4.调用学生选择课程接口
        flag, msg = student_interface.add_course_interface(
            course_name, student_info.get("user")
        )

        print(msg)
        if flag:
            break


@common.auth("student")
def check_score():
    student_score = student_interface.check_score_interface(
        student_info.get("user")
    )
    if student_score:
        for k, v in student_score.items():
            print(f"【{k}】分数：{v}")
    else:
        print(student_score)


func_dic = {
    '1': register,
    '2': login,
    '3': choice_school,
    '4': choice_course,
    '5': check_score,
}


def student_view():
    while True:
        print("""
            - 1. 注册
            - 2. 登陆
            - 3. 选择校区
            - 4. 选择课程
            - 5. 查看分数
            """
              )

        choice = input("请输入功能编号：").strip()
        if choice == "q":
            break

        if choice not in func_dic:
            print("输入有误，请重新输入！")
            continue

        func_dic.get(choice)()
