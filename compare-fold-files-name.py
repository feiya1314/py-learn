import os

folder1ExtFiles = set()
folder2ExtFiles = set()


def compare_folders(folder1, folder2):
    # root 所指的是当前正在遍历的这个文件夹的本身的地址
    # dirs 是一个 list ，内容是该文件夹中所有的目录的名字(不包括子目录)
    # files 同样是 list , 内容是该文件夹中所有的文件(不包括子目录)
    for root, dirs, files in os.walk(folder1):
        # 获取当前文件夹相对于folder1的路径
        relative_path = os.path.relpath(root, folder1)

        # 构建在folder2中对应的路径
        folder2_path = os.path.join(folder2, relative_path)

        # 获取文件夹1中当前文件夹的所有文件名
        files1 = set(files)

        # 获取文件夹2中相应文件夹的所有文件名
        if os.path.isdir(folder2_path):
            files2 = set(os.listdir(folder2_path))
        else:
            # 文件夹2中没有对应的子文件夹，跳过该文件夹的对比
            continue

        # 找出文件名不一致的文件
        diff_files = files1.symmetric_difference(files2)

        # 输出文件名不一致的文件
        for file in diff_files:
            print(os.path.join(root, file))


# 指定两个文件夹的路径
folder1 = r"G:\pyworkspace\easy-chat-service"
folder2 = r"G:\pyworkspace\easy-chat-service-2"

# 调用函数进行对比并输出结果
compare_folders(folder1, folder2)
