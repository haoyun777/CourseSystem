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

    def create_course(self):
        pass

    def create_teacher(self):
        pass


class School(Base):
    def __init__(self, name, addr):
        self.user = name
        self.addr = addr
        self.course_list = []



class Student(Base):
    pass


class Course(Base):
    pass


class Teacher(Base):
    pass


