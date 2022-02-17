import os
import pickle
from conf import settings


def save_data(obj):

    class_name = obj.__class__.__name__

    user_dir_path = os.path.join(
        settings.DB_PATH, class_name
    )

    # 创建文件夹
    if not os.path.exists(user_dir_path):
        os.mkdir(user_dir_path)

    # 拼接当前用户的pickle文件路径
    user_path = os.path.join(
        user_dir_path, obj.user
    )

    # 打开文件，保存对象
    with open(user_path, 'wb') as f:
        pickle.dump(obj, f)


def select_data(cls, username):
    class_name = cls.__name__

    user_dir_path = os.path.join(
        settings.DB_PATH, class_name
    )

    # 创建文件夹
    if not os.path.exists(user_dir_path):
        os.mkdir(user_dir_path)

    # 拼接当前用户的pickle文件路径
    user_path = os.path.join(
        user_dir_path, username
    )

    # 判断文件是否存在
    if not os.path.exists(user_path):
        return None

    # 打开文件，获取对象
    with open(user_path, 'rb') as f:
        obj = pickle.load(f)
    return obj
