# 我是如何用python实现延时摄影的

# 以下是详细步骤

1. 打开手机，使用下面图片小程序码“定时间隔拍照”拍照得到一大堆图片。手机每隔n秒拍一张图片，得到很多张图片（通过手机小程序可以实现，你也可以用其他软件）
![小程序图片](小程序定时间隔拍照.jpg)

2. 把这些图片拷贝到“Camera”文件夹下。

3. 运行python文件，就会在“add_text”文件夹下得到添加了时间的图片，并在python所在的文件夹生成了视频。

4. 视频演示如下：


# 缺点

1. 步骤繁琐：没有手机自带的延时摄影方便。
2. 画质差：手机小程序“定时间隔拍照”保存的图片不够清晰，图片偏小，适合对画质不高的人群。这个缺点可以通过去找其他软件代替把他规避掉。

# 优点
1. DIY程度高：可以控制视频的时间，帧数，图片水印等效果。
2. 省空间：视频小，一千张小图片生成后视频约100兆大小。


