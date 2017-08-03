#coding:utf-8
try:
    #python3
    from urllib.parse import urlencode
except ImportError:
    #python2
    from urllib import urlencode

from django import forms
from django.contrib.admin.widgets import AdminTextareaWidget
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe


class EditorMdWidget(forms.Textarea):
    def __init__(self, attrs=None):

        self.params = attrs.copy()
        super(EditorMdWidget, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        context={"name":name,'value':value}
        context.update( self.params)
        return mark_safe(render_to_string('editor_md.html', context))
    #
    class Media:
        css = {
            'all': ('/static/editor.md/css/style.css','/static/editor.md/css/editormd.css',)
        }
        js = ("/static/editor.md/js/jquery.min.js",
              "/static/editor.md/js/editormd.min.js",
              )


class AdminUEditorWidget(AdminTextareaWidget, EditorMdWidget):

    def __init__(self, **kwargs):
        super(AdminUEditorWidget, self).__init__(**kwargs)
