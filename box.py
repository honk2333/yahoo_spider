# coding: utf-8

"""
物体检测标注小工具

基本思路：
对要标注的图像建立一个窗口循环，然后每次循环的时候对图像进行一次复制，
鼠标在画面上画框的操作、画好的框的相关信息在全局变量中保存，
并且在每个循环中根据这些信息，在复制的图像上重新画一遍，然后显示这份复制的图像。

简化的设计过程：
1、输入是一个文件夹的路径，包含了所需标注物体框的图片。
如果图片中标注了物体，则生成一个相同名称加额外后缀_bbox的文件，来保存标注信息。
2、标注的方式：按下鼠标左键选择物体框的左上角，松开鼠标左键选择物体框的右下角，
按下鼠标右键删除上一个标注好的物体框。
所有待标注物体的类别和标注框颜色由用户自定义。
如果没有定义则默认只标注一种物体，定义该物体名称为Object。
3、方向键 ← 和 → 键用来遍历图片， ↑ 和 ↓ 键用来选择当前要标注的物体，
Delete键删除一种脏图片和对应的标注信息。

自定义标注物体和颜色的信息用一个元组表示
第一个元素表示物体名字
第二个元素表示BGR颜色的tuple或者代表标注框坐标的元祖
利用repr()保存和eval()读取
"""

"""
一些说明：
1. 标注相关的物体标签文件即 .labels 结尾的文件，需要与所选文件夹添加到同一个根目录下
一定要注意这一点，否则无法更新标注物体的类型标签，致使从始至终都只有一个默认物体出现
我就是这个原因，拖了两三天才整好，当然也顺便仔细的读了这篇代码。同时也学习了@staticmethod以及相应Python的decorator的知识。
可以说，在曲折中前进才是棒的。
2. .labels文件为预设物体标签文件，其内容具体格式为:
'object1', (B, G, R)
'object2', (B, G, R)
'object3', (B, G, R)……
具体见文后图片。
3. 最后生成的标注文件，在文后会有，到时再进行解释。
"""

import os
import cv2
# tkinter是Python内置的简单GUI库，实现打开文件夹、确认删除等操作十分方便
from tkinter.messagebox import askyesno
from tqdm import tqdm
# 定义标注窗口的默认名称
WINDOW_NAME = 'Simple Bounding Box Labeling Tool'
# 定义画面刷新帧率
FPS = 10
# 定义支持的图像格式
SUPPORTED_FORMATS = ['jpg', 'jpeg', 'png']
# 定义默认物体框的名字为Object，颜色为蓝色，当没有用户自定义物体时，使用该物体
DEFAULT_COLOR = {'object': (255, 0, 0) }
# 定义灰色，用于信息显示的背景和未定义物体框的显示
COLOR_GRAY = (192, 192, 192)
# 在图像下方多处BAR_HEIGHT的区域，用于显示信息
BAR_HEIGHT = 16
# linux
# 上下左右,DELETE键对应的cv2.waitKey()函数的返回值
KEY_UP = 119
KEY_DOWN = 115
KEY_LEFT = 97
KEY_RIGHT = 100
KEY_DELETE = 255
# KEY_EXIT =  27
KEY_EXIT = 96 
KEY_EMPTY = 0


# win
# KEY_UP = 119
# KEY_DOWN = 115
# KEY_LEFT = 97
# KEY_RIGHT = 100
# KEY_DELETE = 0
# KEY_EXIT =  27
# KEY_EMPTY = 32

get_bbox_name = 'bbox/{}.bbox'.format
# def get_bbox_name(x):
#     print('/bbox' + x[x.rfind('/'):] + '.bbox')
#     return '/bbox' + x[x.rfind('/'):] + '.bbox'

# 定义物体框标注工具类
class SimpleBBoxLabeling:
    def __init__(self, data_dir, fps=FPS, windown_name=WINDOW_NAME):
        self._data_dir = data_dir
        self.fps = fps
        self.window_name = windown_name if windown_name else WINDOW_NAME

        # pt0 是正在画的左上角坐标, pt1 是鼠标所在坐标
        self._pt0 = None
        self._pt1 = None
        # 表明当前是否正在画框的状态标记
        self._drawing = False
        # 当前标注物体的名称
        self._cur_label = None
        # 当前图像对应的所有已标注框
        self._bboxes = []
        # 如果有用户自己定义的标注信息则读取，否则使用默认的物体和颜色
        label_path = '{}.labels'.format(self._data_dir)
        self.label_colors = DEFAULT_COLOR if not os.path.exists(label_path) else self.load_labels(label_path)
        # self.label_colors = self.load_labels(label_path)
        # 获取已经标注的文件列表和未标注的文件列表
        print(self._data_dir)
        print(len(os.listdir(self._data_dir)))
        imagefiles = [x for x in os.listdir(self._data_dir) if x[x.rfind('.') + 1:].lower() in SUPPORTED_FORMATS]
        print(len(imagefiles))
        labeled = [x for x in imagefiles if os.path.exists(os.path.join(self._data_dir, get_bbox_name(x)))]
        print(len(labeled))
        to_be_labeled = [x for x in imagefiles if x not in labeled]
        print(len(to_be_labeled))
        # 每次打开一个文件夹，都自动从还未标注的第一张开始
        self._filelist = labeled + to_be_labeled
        self._index = len(labeled)
        if self._index > len(self._filelist) - 1:
            self._index = len(self._filelist) - 1
        print(self._index)
        # exit(1)

    # 鼠标回调函数
    def _mouse_ops(self, event, x, y, flags, param):
        # 按下左键，坐标为左上角，同时表示开始画框，改变drawing，标记为True
        if event == cv2.EVENT_LBUTTONDOWN:
            self._drawing = True
            self._pt0 = (x, y)
        # 松开左键，表明画框结束，坐标为有效较并保存，同时改变drawing，标记为False
        elif event == cv2.EVENT_LBUTTONUP:
            self._drawing = False
            self._pt1 = (x, y)
            self._bboxes.append((self._cur_label, (self._pt0, self._pt1)))
        # 实时更新右下角坐标
        elif event == cv2.EVENT_MOUSEMOVE:
            self._pt1 = (x, y)
        # 按下鼠标中键删除最近画好的框
        elif event == cv2.EVENT_MBUTTONDBLCLK:
            # print(self._bboxes)
            if self._bboxes:
                self._bboxes.pop()
        elif event == cv2.EVENT_MBUTTONUP and (flags&cv2.EVENT_FLAG_CTRLKEY):
            self._bboxes.append((self._cur_label, ((0,0), (10000,10000))))

    # 清除所有标注框和当前状态
    def _clean_bbox(self):
        self._pt0 = None
        self._pt1 = None
        self._drawing = False
        self._bboxes = []

    # 画标注框和当前信息的函数
    def _draw_bbox(self, img):
        # 在图像下方多出BAR_HEIGHT的区域，显示物体信息
        h, w = img.shape[:2]
        canvas = cv2.copyMakeBorder(img, 0, BAR_HEIGHT, 0, 0, cv2.BORDER_CONSTANT, value=COLOR_GRAY)
        # 正在标注的物体信息，如果鼠标左键已经按下，则像是两个点坐标，否则显示当前待标注物体的名
        label_msg = '{}: {}, {}'.format(self._cur_label, self._pt0, self._pt1) \
            if self._drawing \
            else 'Current label: {}'.format(self._cur_label)
        # 显示当前文件名，文件个数信息
        msg = '{}/{}: {} | {}'.format(self._index + 1, len(self._filelist), self._filelist[self._index], label_msg)
        cv2.putText(canvas, msg, (1, h+12), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
        # 画出已经标好的框和对应名字
        for label, (bpt0, bpt1) in self._bboxes:
            if bpt1[0] > w or bpt1[1] > h:
               bpt1 = (w,h)
            label_color = self.label_colors[label] if label in self.label_colors else COLOR_GRAY
            cv2.rectangle(canvas, bpt0, bpt1, label_color, thickness=2)
            cv2.putText(canvas, label, (bpt0[0]+3, bpt0[1]+15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, label_color, 2)
        # 画正在标注的框和对应名字
        if self._drawing:
            label_color = self.label_colors[self._cur_label] if self._cur_label in self.label_colors else COLOR_GRAY
            if (self._pt1[0] >= self._pt0[0]) and (self._pt1[1] >= self._pt1[0]):
                cv2.rectangle(canvas, self._pt0, self._pt1, label_color, thickness=2)
            cv2.putText(canvas, self._cur_label, (self._pt0[0] + 3, self._pt0[1] + 15),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, label_color, 2)
        return canvas

    # 利用repr()函数导出标注框数据到文件
    @staticmethod
    def export_bbox(filepath, bboxes):
        if bboxes:
            with open(filepath, 'w') as f:
                for bbox in bboxes:
                    line = repr(bbox) + '\n'
                    f.write(line)
        elif os.path.exists(filepath):
            os.remove(filepath)

    # 利用eval()函数读取标注框字符串到数据
    @staticmethod
    def load_bbox(filepath):
        bboxes = []
        with open(filepath, 'r') as f:
            line = f.readline().rstrip()
            while line:
                bboxes.append(eval(line))
                line = f.readline().rstrip()
        return bboxes

    # 利用eval()函数读取物体及对应颜色信息到数据
    @staticmethod
    def load_labels(filepath):
        label_colors = {}
        with open(filepath, 'r') as f:
            line = f.readline().rstrip()
            while line:
                label, color = eval(line)
                label_colors[label] = color
                line = f.readline().rstrip()
        print(label_colors)
        return label_colors

    # 读取图像文件和对应标注框信息（如果有的话）
    @staticmethod
    def load_sample(filepath):
        img = cv2.imread(filepath)
        bbox_filepath = get_bbox_name(filepath)
        bboxes = []
        if os.path.exists(bbox_filepath):
            bboxes = SimpleBBoxLabeling.load_bbox(bbox_filepath)
        return img, bboxes

    # 导出当前标注框信息并清空
    def _export_n_clean_bbox(self):
        bbox_filepath = os.sep.join([self._data_dir, get_bbox_name(self._filelist[self._index])])
        self.export_bbox(bbox_filepath, self._bboxes)
        self._clean_bbox()

    # 删除当前样本和对应的标注框信息
    def _delete_current_sample(self):
        filename = self._filelist[self._index]
        filepath = os.sep.join([self._data_dir, filename])
        if os.path.exists(filepath):
                os.remove(filepath)
        filepath = get_bbox_name(filepath)
        if os.path.exists(filepath):
                os.remove(filepath)
        self._filelist.pop(self._index)
        print('{} is deleted!'.format(filename))

    # 开始OpenCV窗口循环的方法，程序的主逻辑
    def start(self):
        # 之前标注的文件名，用于程序判断是否需要执行一次图像读取
        last_filename = ''

        # 标注物体在列表中的下标
        label_index = 0

        # 所有标注物体名称的列表
        labels = self.label_colors.keys()
        labels = [ label for label in labels]
        print(labels)
        # 带标注物体的种类数
        n_labels = len(labels)

        # 定义窗口和鼠标回调
        # img = None
        cv2.namedWindow(self.window_name)
        cv2.setMouseCallback(self.window_name, self._mouse_ops)
        key = KEY_EMPTY
        print(key)
        # 定义每次循环的持续时间
        delay = int(1000 / FPS)

        # 只要没有按下Exit键，就持续循环
        while key != KEY_EXIT:
            # 上下方向键选择当前标注物体
            if key == KEY_UP:
                if label_index == 0:
                    pass
                else:
                    label_index -= 1
            elif key == KEY_DOWN:
                if label_index == n_labels - 1:
                    pass
                else:
                    label_index += 1
            # 左右方向键选择标注图片
            elif key == KEY_LEFT:
                # 已经到了第一张图片的话就不需要清空上一张
                if self._index > 0:
                    self._export_n_clean_bbox()
                self._index -= 1
                if self._index < 0:
                    self._index = 0
            # elif key = KEY_SAVE:
            elif key == KEY_RIGHT:
                # 已经到了最后一张图片的就不需要清空上一张
                if self._index < len(self._filelist) - 1:
                    self._export_n_clean_bbox()
                self._index += 1
                if self._index > len(self._filelist) - 1:
                    self._index = len(self._filelist) - 1
            # 删除当前图片和对应标注的信息
            elif key == KEY_DELETE:
                if askyesno('Delete Sample', 'Are you sure?'):
                    self._delete_current_sample()
                    key = KEY_EMPTY
                    continue
            # 如果键盘操作执行了换图片， 则重新读取， 更新图片
            print(len(self._filelist))
            print(self._index)
            filename = self._filelist[self._index]
            print(filename)
            if filename != last_filename:
                filepath = os.sep.join([self._data_dir, filename])
                img, self._bboxes = self.load_sample(filepath)
            # 更新当前标注物体名称
            self._cur_label = labels[label_index]
            # 把标注和相关信息画在图片上并显示指定的时间
            canvas = self._draw_bbox(img)
            cv2.imshow(self.window_name, canvas)
            key = cv2.waitKey(delay)
            print('press:',key)
            # 当前文件名就是下次循环的老文件名
            last_filename = filename
        print('Finished!')
        cv2.destroyAllWindows()
        #如果退出程序，需要对当前文件进行保存
        self.export_bbox(os.sep.join([self._data_dir, get_bbox_name(filename)]), self._bboxes)
        print('Labels updated!')         

# tkinter是Python内置的简单GUI库，实现打开文件夹、确认删除等操作十分方便
from tkinter.filedialog import askdirectory
# 导入创建的工具类
# from SimpleBBoxLabeling import SimpleBBoxLabeling

from PIL import Image
 
def crop_imgs(dirid):
    dir_with_images = './nytimes_news/superJumbo/'+str(dirid)+'/bbox'
    bboxs = os.listdir(dir_with_images)
    print(len(bboxs))
    for bbox in tqdm(bboxs):
        print(bbox)
        name = './nytimes_news/superJumbo/'+str(dirid)+'/' + bbox[:-5]
        if not os.path.exists(name):
            # os.remove(os.path.join(dir_with_images,bbox))
            continue
        img = Image.open(name)
        w, h = img.size
        print(w,h)
        bboxes = []
        with open(os.path.join(dir_with_images,bbox), 'r') as f:
            line = f.readline().rstrip()
            while line:
                bboxes.append(eval(line))
                line = f.readline().rstrip()
        # print(len(bboxes)
        cnt = 0
        for sites in bboxes:
            print(sites[1])
            try:
                cropped = img.crop((sites[1][0][0], sites[1][0][1], min(sites[1][1][0],w), min(sites[1][1][1],h)))  # (left, upper, right, lower)
                print(name)
                cropped = cropped.convert('RGB')
                cropped.save("./nytimes_news/superJumbo/"+str(dirid)+"/parts/" + bbox[:-9]+ '-part' + str(cnt)  + '.jpg')
                cnt += 1
            except ValueError:
                continue
            
if __name__ == '__main__':
    # dir_with_images = askdirectory(title='Where is the images?')
    dirid = 26

    dir_with_images = './nytimes_news/superJumbo/' + str(dirid)
    labeling_task = SimpleBBoxLabeling(dir_with_images)
    labeling_task.start()

    # crop_imgs(dirid)

    # test
    # img = cv2.imread('/home/wanghk/code/yahoo_spider/superJumbo/9a5b4b12-f451-52d5-bf11-13a9d01dac6d.jpg')
    # img = cv2.imread('/home/ubuntu/MultiModal-Extractor/spider/superJumbo/imgs/9a5b4b12-f451-52d5-bf11-13a9d01dac6d.jpg')
    # while(1):
    #     cv2.imshow('img',img)
    #     key = cv2.waitKey(20)
    #     print(key)
    # cv2.destroyAllWindows()
