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
        teacher_obj = Teacher(teacher_name, teacher_pwd)
        teacher_obj.save()


class School(Base):
    def __init__(self, name, addr):
        self.user = name
        self.addr = addr
        self.course_list = []


class Student(Base):
    def __init__(self, student_name, student_pwd):
        self.user = student_name
        self.pwd = student_pwd
        self.school = None
        self.course_list = []
        self.score = {}  # {"course_name": 100}
        self.payed = {}  # {"course_name": False}

    def add_school(self, school_name):
        self.school = school_name
        self.save()

    def add_course(self, course_name):

        self.course_list.append(course_name)
        self.score[course_name] = 0
        self.save()

        course_obj = Course.select(course_name)
        course_obj.student_list.append(self.user)
        course_obj.save()



class Course(Base):
    def __init__(self, course_name):
        self.user = course_name
        self.student_list = []


class Teacher(Base):
    def __init__(self, teacher_name, teacher_pwd):
        self.user = teacher_name
        self.pwd = teacher_pwd
        self.__course_list_from_tea = []

    @property
    def show_course(self):
        return self.__course_list_from_tea

    def add_course(self, course_name):

        self.__course_list_from_tea.append(course_name)
        self.save()

    def get_student(self, course_name):

        course_obj = Course.select(course_name)
        return course_obj.student_list

    @staticmethod
    def get_student_score(student_name, course_name):

        student_obj = Student.select(student_name)
        student_course_score = student_obj.score[course_name]
        return student_course_score

    @staticmethod
    def update_student_score(student_name, course_name, score):

        student_obj = Student.select(student_name)
        student_obj.score[course_name] = score
        student_obj.save()

