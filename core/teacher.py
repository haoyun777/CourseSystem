from lib import common
from interface import common_interface
from interface import teacher_interface

teacher_info = {
    "user": ""
}


def login():
    while True:
        username = input("请输入用户名：").strip()
        if not username:
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
    course_list = teacher_interface.check_course_interface(
        teacher_info.get("user")
    )
    if course_list:
        print(course_list)
    else:
        print("请先选择课程！")


@common.auth("teacher")
def choose_course():
    while True:
        # 先选择学校
        flag, school_list = common_interface.get_all_school_interface()
        if not flag:
            print(school_list)
        for index, school_name in enumerate(school_list):
            print(f"编号：{index}      学校名：【{school_name}】")

        choice_school = input("请输入选择的学校编号：").strip()
        if not choice_school.isdigit():
            print("输入有误！")
            continue

        choice_school = int(choice_school)

        if choice_school not in range(len(school_list)):
            sss = range(len(school_list))
            for i in sss:
                print(i)
            print("输入编号有误！")
            continue

        school_name = school_list[choice_school]

        # 再选择课程
        # 1.获取所选择的学校课程列表
        flag, course_list = common_interface.get_all_course_in_school_interface(school_name)

        if not flag:
            print(course_list)
            break

        # 2.打印课程列表
        for index, course in enumerate(course_list):
            print(f"编号：{index}      课程：【{course}】")

        # 3.选择课程
        choice_course = input("请输入选择的课程编号：").strip()
        if not choice_course.isdigit():
            print("输入有误！")
            continue

        choice_course = int(choice_course)

        if choice_course not in range(len(course_list)):
            print("输入编号有误！")
            continue

        course_name = course_list[choice_course]

        # 调用教师选择课程接口
        flag, msg = teacher_interface.add_course_interface(
            course_name, teacher_info.get("user")
        )

        print(msg)
        break


@common.auth("teacher")
def check_stu_from_course():
    while True:
        # 先获取当前老师所选择的课程
        course_list = teacher_interface.check_course_interface(
            teacher_info.get("user")
        )
        if not course_list:
            print("请先选择课程！")
            break
        for index, course_name in enumerate(course_list):
            print(f"编号：{index}      课程：【{course_name}】")

        # 选择课程
        choice_course = input("请输入选择的课程编号：").strip()
        if not choice_course.isdigit():
            print("输入有误！")
            continue

        choice_course = int(choice_course)

        if choice_course not in range(len(course_list)):
            print("输入编号有误！")
            continue
        course_name = course_list[choice_course]

        # 打印课程下面的所有学生
        student_list = teacher_interface.get_all_student_from_course_interface(
            course_name, teacher_info.get("user")
        )
        print(student_list)
        break


@common.auth("teacher")
def change_score_from_student():
    while True:
        # 先获取当前老师所选择的课程
        course_list = teacher_interface.check_course_interface(
            teacher_info.get("user")
        )
        if not course_list:
            print("请先选择课程！")
            break
        for index, course_name in enumerate(course_list):
            print(f"编号：{index}      课程：【{course_name}】")

        # 选择课程
        choice_course = input("请输入选择的课程编号：").strip()
        if not choice_course.isdigit():
            print("输入有误！")
            continue

        choice_course = int(choice_course)

        if choice_course not in range(len(course_list)):
            print("输入编号有误！")
            continue
        course_name = course_list[choice_course]

        # 打印课程下面的所有学生以及分数
        student_list = teacher_interface.get_all_student_from_course_interface(
            course_name, teacher_info.get("user")
        )
        if not student_list:
            print("还没有学生选择该课程哦！")
            break

        for index, student_name in enumerate(student_list):

            score = teacher_interface.get_course_score_from_teacher_interface(
                student_name, course_name
            )

            print(f"编号：{index}      学生名：【{student_name}】      分数：【{score}】")

        # 选择一个学生
        choice_student = input("请输入要修改学生分数的编号：").strip()
        if not choice_student.isdigit():
            print("输入有误！")
            continue

        choice_student = int(choice_student)

        if choice_student not in range(len(student_list)):
            print("输入编号有误！")
            continue
        student_name = student_list[choice_student]

        # 修改分数
        score = input("请输入一个 0-100 的整数：").strip()
        if not score.isdigit():
            print("输入错误！")
        score = int(score)
        if not 0 <= score <= 100:
            print("输入错误！")

        flag, msg = teacher_interface.update_student_course_score_interface(
            student_name, course_name, score
        )
        print(msg)
        break


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
