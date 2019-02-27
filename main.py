# -*- coding: utf-8 -*-
# python3.7
# 用于为知笔记.html格式批量导入印象笔记


import os


def get_filename(file_dir):
    file_list = []
    os.chdir(file_dir)
    for files in os.listdir(file_dir):
        temp = os.path.splitext(files)
        if temp[1] == '.html':
            name = temp[0]
            files_name = name + '_files'
            new_name = ''.join(name.split())
            if os.path.exists(files_name):
                # 判断同名文件夹是否存在\
                os.rename(files_name, new_name + '_files')
                os.rename(name + '.html', new_name + '.html')
            else:
                os.rename(files, new_name + '.html')
            file_list.append(new_name + '.html')
    return file_list


if __name__ == "__main__":
    #印象笔记程序安装目录
    exe_dir = "D:/印象笔记/"
    # 为知笔记导出目录
    html_dir = 'I:/test/'
    flie_list = get_filename(html_dir)
    os.chdir(exe_dir)
    for i in flie_list:
        f = html_dir+i
        p = 'Evernote.exe '+f
        os.system(p)
        print('Work done!')
