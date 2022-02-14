

def register():
    pass


def login():
    pass


def choice_school():
    pass


def choice_course():
    pass


def check_score():
    pass


func_dic = {
    '1': register,
    '2': login,
    '3': choice_school,
    '4': choice_course,
    '5': check_score,
}


def student_view():
    while True:
        print("""
            - 1. 注册
            - 2. 登陆
            - 3. 选择校区
            - 4. 选择课程
            - 5. 查看分数
            """
              )

        choice = input("请输入功能编号").strip()
        if choice == "q":
            break

        if choice not in func_dic:
            print("输入有误，请重新输入！")
            continue

        func_dic.get(choice)()
