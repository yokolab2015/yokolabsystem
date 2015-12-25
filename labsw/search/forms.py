from django.forms import ModelForm
from docmng.models import Document
from django import forms

DOC_TYPE = (
	('OS輪講', 'OS輪講'),
	('仮想化輪講', '仮想化輪講'),
	('文献紹介', '文献紹介'),
	('卒論紹介', '卒論計画'),
	('卒論進歩', '卒論進歩'),
	('マニュアル', 'マニュアル'),
	('その他', 'その他'),
	('', '全て'),
)

FOR_TYPE = (
	('pdf', 'pdf'),
	('doc', 'doc'),
	('xls', 'xls'),
	('ppt', 'ppt'),
	('', '全て'),
)


class DocForm(ModelForm):
	class Meta:
		model = Document
		fields = ('name', 'author', 'type', 'format', 'sid', )

class DocForm2(forms.Form):
	title = forms.CharField(label='タイトル', min_length=2, max_length=128)
	createauthor = forms.CharField(label='作者',min_length=2, max_length=16)
	createyear = forms.CharField(label='年度', min_length=4, max_length=4)
	for_type = forms.ChoiceField(label='フォーマット', widget=forms.Select, choices=FOR_TYPE, required=False,)
	doc_type = forms.ChoiceField(label='文書種別', widget=forms.Select, choices=DOC_TYPE, required=False,)

class DocFormE(forms.Form):
        title = forms.CharField(label='タイトル', min_length=2, max_length=128)
        createauthor = forms.CharField(label='作者',min_length=2, max_length=16)
        #createyear = forms.CharField(label='年度', min_length=4, max_length=4)
        for_type = forms.ChoiceField(label='フォーマット', widget=forms.Select, choices=FOR_TYPE, required=False,)
        doc_type = forms.ChoiceField(label='文書種別', widget=forms.Select, choices=DOC_TYPE, required=False,)
        path = forms.FileField()


