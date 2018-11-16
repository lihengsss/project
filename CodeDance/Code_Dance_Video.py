import cv2
import os
import time
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import numpy as np

def rgb2gray(rgb):
    '''
    把RGB矩阵转为灰度矩阵
    :param rgb: rgb矩阵
    :return: 灰度图矩阵
    '''
    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray

def codeVideo():
    # 建立字符映射字符串
    ascii_char = list(" @B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI               ")

    char_len = len(ascii_char)

    video_path = r'E:\CloudMusic\MV\video/'

    videos = os.listdir(video_path)

    for video_name in videos:

        file_name = video_name.split('.')[0]
        folder_name = video_path + file_name
        os.makedirs(folder_name,exist_ok=True)

        vc = cv2.VideoCapture(video_path+video_name) #读入视频文件

        c=0 #当前帧数的变量

        rval=vc.isOpened() #判断视频是否处于打开状态

        fps = 29  #要制作的视频的帧数

        fourcc = cv2.VideoWriter_fourcc(*'MJPG')

        # 创建VideoWriter对象，fourcc--编码格式，这里分辨率我手动设为960*540
        video_writer = cv2.VideoWriter('video.avi', fourcc, fps,(960, 540))

        while rval:   #循环读取视频帧
            c = c + 1

            #读取当前帧的图片的矩阵
            rval, frame = vc.read()

            print(c,frame.shape)

            #取矩阵的行数和列数
            rows, cols, channel = frame.shape

            #压缩矩阵的大小(interpolation参数根据需求设置)
            '''
            To shrink an image, it will generally look best with #INTER_AREA interpolation,
            whereas to enlarge an image, it will generally look best with c#INTER_CUBIC (slow) or #INTER_LINEAR(
            faster but still looks OK)
            '''

            #行列压缩量，根据需要的效果自行调节
            row_compress=26 #行压缩量
            col_compress=12 #列压缩量

            frame2=cv2.resize(frame,(int(cols/col_compress),int(rows/row_compress)),fx=0,fy=0,interpolation=cv2.INTER_LINEAR)

            # 将读取到的彩色矩阵转化为灰度矩阵
            gray_img = rgb2gray(frame2)

            #得到矩阵的宽高
            img_heigth, img_width = gray_img.shape

            img_text=""#替换图片的文本

            for i in range(int(img_heigth)):

                row_text = ""#行文本

                # 根据比例映射到对应的像素
                for j in range(int(img_width)):
                    row_text += ascii_char[int(gray_img[i][j] / 256 * char_len)]
                img_text+=row_text+"\n"

            #新建画布对象
            im = Image.new("RGB", (192*5, 108*5), (255, 255, 255))

            #得到画笔对象
            dr = ImageDraw.Draw(im)

            #设置字体
            # font = ImageFont.load_default().font
            font = ImageFont.truetype("consola.ttf",10, encoding="unic")

            #画文本到画布上
            dr.text((0, 0),img_text, font=font, fill="#000000")

            #画布转为矩阵
            img = np.asarray(im)

            #写入视频文件
            video_writer.write(img)

            #判断是否还有下一帧
            if rval:

                #等待1ms 不然视频会显示不正常
                cv2.waitKey(1)
            else:
                break

        #完成视频写入
        video_writer.release()

if __name__ == '__main__':
    codeVideo()