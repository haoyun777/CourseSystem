
# 多用户登陆认证装饰器
def auth(role):
    """
    :param role: 角色 ---> 管理员、学生、老师
    :return:
    """
    def login_auth(func):
        def inner(*args, **kwargs):

            from core import admin
            from core import student
            from core import teacher

            if role == "admin":
                if admin.admin_info["user"]:
                    res = func(*args, **kwargs)
                    return res
                else:
                    admin.login()

            elif role == "student":
                if student.student_info["user"]:
                    res = func(*args, **kwargs)
                    return res
                else:
                    student.login()

            elif role == "teacher":
                if teacher.teacher_info["user"]:
                    res = func(*args, **kwargs)
                    return res
                else:
                    teacher.login()

            else:
                print("当前视图没有权限！")

        return inner
    return login_auth


