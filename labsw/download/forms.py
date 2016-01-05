from django import forms
from django.forms import ModelForm
from docmng.models import Document

DOC_TYPE = (
	('OS輪講', 'OS輪講'),
	('仮想化輪講', '仮想化輪講'),
	('文献紹介', '文献紹介'),
	('卒論計画', '卒論計画'),
	('卒論進歩', '卒論進歩'),
	('マニュアル', 'マニュアル'),
	('その他', 'その他'),

)

FOR_TYPE = (
	('pdf', 'pdf'),
	('doc', 'doc'),
	('xls', 'xls'),
	('ppt', 'ppt'),
)

class MessageForm(forms.Form):
    message = forms.CharField(
        label='メッセージ',
        max_length=255,
        required=True,
        widget=forms.TextInput()
    )

class UploadForm(forms.Form):
    name = forms.CharField(label='タイトル', min_length=2, max_length=128)
    #author = forms.CharField(label='作者',min_length=2, max_length=16)
    format = forms.ChoiceField(label='フォーマット', widget=forms.Select, choices=FOR_TYPE, required=False,)
    type = forms.ChoiceField(label='文書種別', widget=forms.Select, choices=DOC_TYPE, required=False,)
    path = forms.FileField()