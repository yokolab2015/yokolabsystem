from django.forms import ModelForm
from docmng.models import Document
from django import forms

DOC_TYPE = (
	('o', 'OS輪講'),
	('k', '仮想化輪講'),
	('b', '文献紹介'),
	('s', '卒論計画'),
	('ss', '卒論進歩'),
	('m', 'マニュアル'),
	('sonota', 'その他'),
)

FOR_TYPE = (
	('p', 'pdf'),
	('w', 'doc'),
	('x', 'xls'),
	('p', 'ppt'),
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

