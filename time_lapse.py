# @author: 公众账号：小鹏同学
import time
import os
import cv2


def sort_file_by_time(file_path):
    # 文件排序
    #./Camera/mmexport1598752339323.jpg
    files = os.listdir(file_path)
    if not files:
        return
    else:
        files = sorted(files, key=lambda x: os.path.getmtime(
            os.path.join(file_path, x)))  # 格式解释:对files进行排序.x是files的元素,:后面的是排序的依据.   x只是文件名,所以要带上join.
        return files


def jpg_avi():
    # 图片转换为视频
    # 保存视频的FPS，可以适当调整
    fps = 24

    # 可以用(*'DVIX')或(*'X264'),如果都不行先装ffmepg: sudo apt-get install ffmepg
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')

    # myVideoName.avi是要生成的视频名称
    saveVideoName = 'myVideoName.mp4'

    # (256,341)是图片尺寸，与图片尺寸不符合会报错
    frameSize = (1080, 787)

    # videoWriter = cv2.VideoWriter(saveVideoName='myvideoname.avi',
    # fourcc=cv2.VideoWriter_fourcc(*'MJPG'), fps=1, frameSize=(256,341)))
    videoWriter = cv2.VideoWriter(saveVideoName, fourcc, fps, frameSize)

    my_sort_files = sort_file_by_time("./add_text/")
    for i in range(len(my_sort_files)):
        img = cv2.imread("./add_text/%s" % str(my_sort_files[i]), -1)
        print('生成视频帧： ' + str(my_sort_files[i]))
        videoWriter.write(img)
    # for i in range(1, 189):
    #     img = cv2.imread("./add_text/%s.jpg" % i, -1)
    #     print(i)
    #     videoWriter.write(img)
    videoWriter.release()


def add_text():
    # 给图片的左下角添加时间文字
    my_sort_files = sort_file_by_time("./Camera/")
    for i in range(len(my_sort_files)):

        my_old_name = './Camera/' + str(my_sort_files[i])
        print('add text : ' + my_old_name)
        # my_new_name = './sun/' + str(i + 1) + ".jpg"
        # os.rename(my_old_name, my_new_name)
        # 加载背景图片
       
        # 显示图片
        # cv2.imshow("add_text", bk_img)
        # cv2.waitKey()
        # 保存图片
        # cv2.imwrite("./add_text/" + my_old_name[13:24] + '' + my_old_name[24:26] + '' + my_old_name[26:], bk_img)
        # 如果是时间戳./Camera/mmexport1598752339323.jpg
        timestamp = my_old_name[17:-7] # 1598752187266转int时太大，需要截掉末尾3位 所以是-7

        # timeArray = time.strptime(my_time_from_str, r"%Y-%m-%d %H:%M:%S")
        # my_left_botton_time = time.strftime(r"%Y%m%d-%H:%M:%S",timeArray)
        # print(timeArray)
        # cv2.imwrite("./add_text/" + my_left_botton_time, bk_img)

        #转换成localtime
        time_local = time.localtime(int(timestamp))
        #转换成新的时间格式(2016-05-05 20:28:54)
        dt = time.strftime(r"%Y-%m-%d %H:%M:%S",time_local)
        my_str_dt = str(dt)
        my_str_dt = my_str_dt.replace(' ', '___')
        my_str_dt = my_str_dt.replace(':', '_')

        bk_img = cv2.imread(my_old_name)# 读取图片的路径加名字
        # 在图片上添加文字信息
        cv2.putText(bk_img, my_str_dt, (50, 760), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.imwrite("./add_text/" + str(my_str_dt) + '.jpg', bk_img)
        print(dt)


if __name__ == '__main__':
    add_text()
    jpg_avi()