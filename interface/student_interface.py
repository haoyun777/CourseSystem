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