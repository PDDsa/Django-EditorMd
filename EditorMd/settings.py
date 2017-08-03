#coding:utf-8
#上传图片设置
import os
from django.conf import settings

#这是editor.md的属性配置
EDITORMD_SETTING = {
    'width':'90%',
    'height':500,
    'path': settings.STATIC_URL+"editor.md/lib/",
    'theme': "dark",
    'previewTheme': "dark",
    'editorTheme': "pastel-on-dark",
    'codeFold': 'true',
    'syncScrolling': 'true',
    'searchReplace': 'true',
    'watch': 'true', # 关闭实时预览
    'htmlDecode': "style,script,iframe|on*",# 开启HTML标签解析，为了安全性，默认不开启
    'toolbar': 'true', # 关闭工具栏
    'previewCodeHighlight': 'true', # 关闭预览HTML的代码块高亮，默认开启
    'emoji': 'true',#支持emoji表情
    'taskList': 'true',
    'tocm': 'true', # Using[TOCM]
    'tex': 'true', # 开启科学公式TeX语言支持，默认关闭
    'flowChart': 'true', # 开启流程图支持，默认关闭
    'sequenceDiagram': 'true', # 开启时序 / 序列图支持，默认关闭,
    'dialogLockScreen': 'true', # 设置弹出层对话框不锁屏，全局通用，默认为true
    'dialogShowMask': 'true', # 设置弹出层对话框显示透明遮罩层，全局通用，默认为true
    'dialogDraggable': 'true', # 设置弹出层对话框不可拖动，全局通用，默认为true
    'dialogMaskOpacity': 0.1, # 设置透明遮罩层的透明度，全局通用，默认值为0.1
    'dialogMaskBgColor': "#fff", # 设置透明遮罩层的背景颜色，全局通用，默认为#fff


}
#这是上传图片时的配置
UPLOADIMAGE = {
    'imageUpload': 'true',
    'imageFormats': ['jpg', 'jpeg', 'png', 'bmp'],
    'imageUploadURL':'/editor/upload/',#这是处理上传图片请求的url,大家可以看一下urls.py中的配置
    'ext':['.jpg', '.jpge', '.png', '.bmp'],#上传文件后缀名称
    'size':1024*1024,#上传文件大小,默认为1M
    'urlpath':settings.STATIC_URL+'editor.md/upload/',#这是上传成功后,返回上传图片的url路径
    'savepath':os.path.dirname(os.path.abspath(__file__))+'/static/editor.md/upload/'#这是实际物理存储路径
}


#给editormd上传的图片加水印
MDWATERMASK = {
    'isOpen':'false',
    'waterMarkText':u"七夜安全博客",#水印内容
    'waterMarkFont':'msyhbd.ttf',#字体路径
    'waterMarkSize':18,# 字体大小
    'waterMarkBottom':0.1,# 下边距,距离底部为宽度的10%
    'waterMarkRight':0.3,# 右边距,,距离底部为长度的30%

}
# if __name__=='__main__':
#     editormd_settings = dict(EDITORMD_SETTING, **UPLOADIMAGE)
#     print(editormd_settings)
#     print(os.path.dirname(os.path.abspath(__file__)))