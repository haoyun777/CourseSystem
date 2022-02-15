from db import models


def admin_register_interface(username, password):
    # 1. 判断用户是否存在

    admin_obj = models.Admin.select(username)

    if admin_obj:
        return False, "用户已存在！"

    admin_obj = models.Admin(username, password)

    admin_obj.save()

    return True, "注册成功！"


def admin_login_interface(username, password):

    admin_obj = models.Admin.select(username)

    if not admin_obj:
        return False, "用户不存在！"

    if admin_obj.pwd == password:
        return True, "登陆成功！"
    else:
        return False, "密码错误！"


def create_school_interface(school_name, school_addr, admin_name):

    # 查看当前学校是否已存在, school_obj --> 对象 or None
    school_obj = models.School.select(school_name)

    if school_obj:
        return False, "学校已存在！"

    # 创建学校（由管理员对象创建）

    admin_obj = models.Admin.select(admin_name)
    admin_obj.create_school(
        school_name, school_addr
    )

    return True, f"学校【{school_name}】创建成功！"


def create_course_interface(school_name, course_name, admin_name):

    # 查看当前课程是否存在
    school_obj = models.School.select(school_name)
    if course_name in school_obj.course_list:
        return False, "当前课程已存在！"

    # 创建课程
    admin_obj = models.Admin.select(admin_name)
    admin_obj.create_course(
        school_obj, course_name
    )

    return True, f"课程【{course_name}】创建成功！绑定给【{school_name}】校区！"


def create_teacher_interface(teacher_name, admin_name, teacher_pwd="123"):

    # 查看老师是否存在
    teacher_obj = models.Teacher.select(teacher_name)
    if teacher_obj:
        return False, "老师已存在！"

    # 创建老师
    admin_obj = models.Admin.select(admin_name)
    admin_obj.create_teacher(
        teacher_name, teacher_pwd
    )
    return True, f"老师【{teacher_name}】创建成功！"
