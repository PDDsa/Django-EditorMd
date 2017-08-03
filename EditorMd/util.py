#coding:utf-8
import json
import os

#检查文件扩展名是否在允许的扩展名内
import time

from EditorMd import settings
# {
#     success : 0 | 1,           // 0 表示上传失败，1 表示上传成功
#     message : "提示的信息，上传成功或上传失败及错误信息等。",
#     url     : "图片地址"        // 上传成功时才返回
# }
class JsonResult(object):

    def __init__(self):
        self.success = 0
        self.message=''
        self.url=''

    def buildJsonResult(self):
        content = {
            'success':self.success,
            'message':self.message,
            'url':self.url
        }
        return json.dumps(content)


def CheckFileType(filename,AllowExtensions):
    exts = list(AllowExtensions)
    name,ext = os.path.splitext(filename)
    return ext in exts
#检查文件大小
def CheckFileSize(filesize,SizeLimit):
    return filesize<SizeLimit

#生成文件名称
def buildFileName(filename):
    """
        PathFormat处理
    """
    dt = datetime.now()
    name,ext = os.path.splitext(filename)
    return "md_"+dt.strftime("%Y%m%d%H%M%S") + ext


# 加水印
def add_watermark(savePath):
    try:
        # 判断是否是图片文件
        if not os.path.splitext(savePath)[-1].lower() in ['.jpg', '.jpge', '.png', '.bmp']:
            return
        # 获取配置
        watermark = settings.MDWATERMASK
        is_mark = watermark.get('isOpen', False)  # 是否开启加水印功能
        watermarktext = watermark.get('waterMarkText', u"七夜安全博客")  # 水印内容
        font = watermark.get('waterMarkFont', 'msyhbd.ttf')  # 字体
        size = watermark.get('waterMarkSize', 15)  # 字体大小
        bottom = watermark.get('waterMarkBottom', 45)  # 下边距
        right = watermark.get('waterMarkRight', 155)  # 右边距

        # 判断是否开启了加水印功能
        if not is_mark:
            return
        # python2.7 pillow
        try:
            from PIL import Image, ImageDraw, ImageFont
        except ImportError:
            return

        # 打开图片
        im = Image.open(savePath).convert('RGBA')
        # 透明的图层，用于写文本
        text_layer = Image.new('RGBA', im.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(text_layer)

        # 加载字体，设置大小
        font_path = os.path.join(os.path.dirname(__file__), 'static/editor.md/fonts/'+font)
        fnt = ImageFont.truetype(font_path, size)  # 要加中文字体才能识别中文
        point = (text_layer.size[0] *(1- right), text_layer.size[1]*(1 - bottom))  # 位置
        draw.text(point, watermarktext, font=fnt, fill=(255, 255, 255, 255))
        # out=Image.alpha_composite(im, text_layer)
        out = Image.composite(text_layer, im, text_layer)
        out.save(savePath)
        out.close()
    except Exception as e:
        print('[error]', e.message)

# if __name__=="__main__":
#     print __file__
#     print os.path.join(os.path.dirname(__file__), 'static/editor.md/fonts/'+'tt.ttf')
