import os
from conf import settings
from db import models


def get_all_school_interface():
    school_dir = os.path.join(
        settings.DB_PATH, "School"
    )

    if not os.path.exists(school_dir):
        return False, "没有学校，请先联系管理员！"

    school_list = os.listdir(school_dir)
    return True, school_list


def get_all_course_in_school_interface(school_name):
    school_obj = models.School.select(school_name)
    course_list = school_obj.course_list
    if not course_list:
        return False, "该学校没有课程！"
    return True, course_list


# 公共登陆接口
def login_interface(username, password, user_type):
    if user_type == "admin":
        obj = models.Admin.select(username)
    elif user_type == "student":
        obj = models.Student.select(username)
    elif user_type == "teacher":
        obj = models.Teacher.select(username)
    else:
        return False, "登陆角色错误，请输入正确的登陆角色！"

    if not obj:
        return False, "用户不存在！"

    if obj.pwd == password:
        return True, "登陆成功！"
    else:
        return False, "密码错误！"
