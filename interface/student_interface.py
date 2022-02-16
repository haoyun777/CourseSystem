from db import models


# 学生注册接口
def student_register_interface(username, password):
    # 1. 判断用户是否存在

    student_obj = models.Student.select(username)

    if student_obj:
        return False, "学生用户已存在！"

    student_obj = models.Student(username, password)

    student_obj.save()

    return True, "注册成功！"


def add_school_interface(school_name, student_name):
    student_obj = models.Student.select(student_name)

    if student_obj.school:
        return True, "当前学生已经选择过学校了！"

    student_obj.add_school(school_name)

    return True, f"成功选择学校【{school_name}】"


def get_course_list_interface(student_name):
    student_obj = models.Student.select(student_name)
    school_name = student_obj.school
    if not school_name:
        return False, "当前学生还没有选择学校呢！"

    school_obj = models.School.select(school_name)
    course_list = school_obj.course_list
    if not course_list:
        return False, "学校没有课程，请联系管理员创建！"

    return True, course_list

def add_course_interface(course_name, student_name):

    # 先判断当前课程是否已经被选择过

    student_obj = models.Student.select(student_name)
    course_list = student_obj.course_list

    if course_name in course_list:
        return True, "该课程已经被选择过了呢"

    student_obj.add_course(course_name)

    return True, f"【{course_name}】添加课程成功！"


def check_score_interface(student_name):
    student_obj = models.Student.select(student_name)
    return student_obj.score

