from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.views.generic.list import ListView
from django.shortcuts import render_to_response
from django.db.models import Q
from . import forms, models
from django.shortcuts import redirect
from docmng.models import Document
from .forms import DocForm
from .forms import DocForm2
from django.utils.http import urlencode
#from django import html
# Create your views here.
from django.db.models.manager import QuerySet

def index(request):
	if request.method == "GET":
		form = DocForm(request.GET)
		if form.is_valid():
			entry = form.cleaned_data["entry"]
			print(entry)
			Document.objects.create(
				entry=entry
			)
		return redirect('/')

	entries = Document.objects.all()
	form = DocForm()
	return render_to_response(
		'index.html',
		context_instance=RequestContext(
			request,
			{
				'form': form,
				'entries': entries
			}
		)
	)

def show(request):
	Document.objects
	form = DocForm2()
	if request.method == 'GET':
		form = DocForm2(request.GET)
		books = Document.objects.all()
	#fn = request.GET['title']
	#ff = request.GET['for_type']
	#y = request.GET['createyear']
	an = request.GET['createauthor']
	#dt = request.GET['doc_type']
	'''d = {
		'fn': request.GET.get('title'),
        'ff': request.GET.get('for_type'),
        'y': request.GET.get('createyear'),
        'an': request.GET.get('createauthor'),
        'dt': request.GET.get('doc_type')
	}       '''
	books['entry']=Document.objects.filter(
		Q(author__contain=an)
	)
	#queries=[Q(author__contains=d)]
	#books = Document.objects.all().order_by('sid')
	#books = Document.objects.filter(author='fn')
	#books = Document.objects.filter(Q(author__contains='d'))
	#books = Document.objects.filter(Q(author__contains=form.cleaned_data['createauthor']))
	#print('an')
	return render_to_response('search/kekka.html',{'form':form, 'books': books},RequestContext(request))
	#return render_to_response('search/kekka.html',dict(book_id=book_id),context_instance=RequestContext(request))
	#return render('search/kekka.html', books)
	#return redirect('./search/kekka.html')
'''
def accpept(request, book_id=None):
	d = {
                'fn': request.GET.get('file_name'),
                'ff': request.GET.get('file_format'),
                'y': request.GET.get('year'),
                'an': request.GET.get('author_name'),
                'dt': request.GET.get('example1')
        }
'''
def search(request):
	form = DocForm2()
	#fn = request.GET.get('file_name')
	#ff = request.GET.get('file_format')
	#y = request.GET.get('year')
	#an = request.GET.get('author_name')
	#dt = request.GET.get('example1')
	'''
	d = {
		'fn': request.GET.get('file_name'),
        	'ff': request.GET.get('file_format'),
        	'y': request.GET.get('year'),
        	'an': request.GET.get('author_name'),
        	'dt': request.GET.get('example1')
	}'''
#この下で動く
	#one_entries = Document.objects.filter(author='浜田哲郎')
	#print(one_entries.query)
	#return render(request, 'search/search_file.html')
	return render_to_response('search/search_file.html',{'form':form },RequestContext(request))
'''
def result(request):
	form = forms.HelloForm(request.POST or None)
	if form.is_valid():
		models.Document.object.create(**form.cleaned_data)
		return redirect('search:result')
	d = {
		'form': form,
		'search_qs': models.Search.object.all().order_by('-id')
	}
	return render(request, 'search_result.html', d)
'''
