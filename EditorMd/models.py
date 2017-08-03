#coding:utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.admin import widgets as admin_widgets
# Create your models here.
from EditorMd.settings import EDITORMD_SETTING, UPLOADIMAGE
from EditorMd.widgets import EditorMdWidget, AdminUEditorWidget


class EditorMdField(models.TextField):
    """
    百度HTML编辑器字段,初始化时，可以提供以下参数
        initial:初始内容
        toolbars:提供工具按钮列表,取值为列表，如['bold', 'italic'],取值为：mini,normal,full，代表小，一般，全部
        imagePath:图片上传的路径,如"images/",实现上传到"{{MEDIA_ROOT}}/images"文件夹
        filePath:附件上传的路径,如"files/",实现上传到"{{MEDIA_ROOT}}/files"文件夹
    """

    def __init__(self, verbose_name=None, **kwargs):
        self.editormd_settings = dict(EDITORMD_SETTING, **UPLOADIMAGE)
        kwargs["verbose_name"] = verbose_name
        super(EditorMdField, self).__init__(**kwargs)

    def formfield(self, **kwargs):
        defaults = {'widget': EditorMdWidget(attrs=self.editormd_settings)}
        defaults.update(kwargs)
        if defaults['widget'] == admin_widgets.AdminTextareaWidget:
            defaults['widget'] = AdminUEditorWidget(
                attrs=self.editormd_settings)

        return super(EditorMdField, self).formfield(**defaults)


