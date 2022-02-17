from db import models


def check_course_interface(teacher_name):
    teacher_obj = models.Teacher.select(teacher_name)

    course_list = teacher_obj.show_course

    return course_list


def add_course_interface(course_name, teacher_name):

    # 先判断当前课程是否已经被选择过

    teacher_obj = models.Teacher.select(teacher_name)
    course_list = teacher_obj.show_course

    if course_name in course_list:
        return True, "该课程已经被选择过了呢！"

    teacher_obj.add_course(course_name)

    return True, f"【{course_name}】添加课程成功！"


def get_all_student_from_course_interface(course_name, teacher_name):
    teacher_obj = models.Teacher.select(teacher_name)
    student_list = teacher_obj.get_student(course_name)

    return student_list


def get_course_score_from_teacher_interface(student_name, course_name):

    score = models.Teacher.get_student_score(student_name, course_name)
    return score


def update_student_course_score_interface(student_name, course_name, score):
    models.Teacher.update_student_score(student_name, course_name, score)

    return True, f"学生【{student_name}】的【{course_name}】课程分数更新成功，当前分数：{score}"
