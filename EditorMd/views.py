#coding:utf-8
import codecs
import os


from django.http import HttpResponse

#处理图片同域上传
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from EditorMd.settings import UPLOADIMAGE
from EditorMd.util import JsonResult, CheckFileType, CheckFileSize, buildFileName, add_watermark


@csrf_exempt
def upload(request):
    result = JsonResult()
    buf = request.FILES.get("editormd-image-file")
    filename = buf.name
    if not CheckFileType(filename,UPLOADIMAGE.get('ext',['.jpg', '.jpge', '.png', '.bmp'])):
        result.success =0
        result.message =u"不允许的文件格式"
        return HttpResponse(result.buildJsonResult())

    if not CheckFileSize(buf.size,UPLOADIMAGE.get('size',1024*1024)):
        result.success = 0
        result.message = u"文件大小超出服务器限制"
        return HttpResponse(result.buildJsonResult())

    try:
        truelyName = buildFileName(filename)
        webUrl = UPLOADIMAGE.get('urlpath','/static/editor.md/upload/')+ truelyName
        savePath = UPLOADIMAGE.get('savepath',os.path.dirname(os.path.abspath(__file__))+'/static/editor.md/upload/')+ truelyName

        #判断文件夹是否存在，不存在则创建
        folder, filename = os.path.split(savePath)
        if not os.path.isdir(folder):
            os.makedirs(folder)
        f = codecs.open(savePath,"wb")
        for chunk in buf.chunks():
            f.write(chunk)
        f.flush()
        f.close()
        add_watermark(savePath) #加水印

        result.success = 1
        result.url = webUrl
        result.message = u"上传成功"
        response = HttpResponse(result.buildJsonResult())
        response["Content-Type"] = "text/plain"
        return response
    except Exception as e:
        result.success = 0
        result.message =  u"网络错误"
        return HttpResponse(result.buildJsonResult())
