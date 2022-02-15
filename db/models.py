from db import db_handler


class Base:
    @classmethod
    def select(cls, user):
        obj = db_handler.select_data(cls, user)
        return obj

    def save(self):
        db_handler.save_data(self)


class Admin(Base):
    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd

    def create_school(self, school_name, school_addr):
        school_obj = School(school_name, school_addr)
        school_obj.save()

    def create_course(self, school_obj, course_name):
        # 调用课程类，实例化创建课程
        course_obj = Course(course_name,)
        course_obj.save()

        # 获取当前学校对象，并将课程添加到课程列表中
        school_obj.course_list.append(course_name)
        school_obj.save()

    def create_teacher(self, teacher_name, teacher_pwd):
        teacher_obj = Teacher(teacher_name,teacher_pwd)
        teacher_obj.save()


class School(Base):
    def __init__(self, name, addr):
        self.user = name
        self.addr = addr
        self.course_list = []



class Student(Base):
    pass


class Course(Base):
    def __init__(self, course_name):
        self.user = course_name
        self.student_list = []


class Teacher(Base):
    def __init__(self, teacher_name, teacher_pwd):
        self.user = teacher_name
        self.pwd = teacher_pwd
        self.course_list_from_tea = []



