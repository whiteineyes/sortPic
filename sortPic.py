import os
import shutil


def func(rootDir, outputDir):  # 定义函数，参数为要操作的根文件夹路径，和输出的新文件夹路径
    for secDir in os.listdir(rootDir):  # 列出rootDir目录下的所有二层文件夹，并遍历结果
        secAdr = os.path.join(rootDir,secDir)  #  把二级文件夹的名称与根文件夹路径拼接
        for fileName in os.listdir(secAdr):  # 遍历二级文件夹目录下的所有文件
            if '.jpg' == fileName[-4:] or '.png' == fileName[-4:] or '.mp4' == fileName[-4:]: # 匹配，根据文件名后四位判断是否为图片类型
                print(fileName) 
                fileAdr = os.path.join(secAdr,fileName)  #  把文件的名称与二级文件夹路径拼接
                if os.path.isfile(fileAdr):     # 判断文件路径是否为文件
                    shutil.copy(fileAdr, outputDir)  # 把文件复制到输出文件夹
                    print("copying "+fileName)
    print("finished")

func("D:/Onedrive/Apps/google/" , "D:/Onedrive/apps/sorted/")
