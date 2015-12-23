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

#def show(request):
#	Document.objects
#	form = DocForm2()
#	if request.method == 'GET':
#		form = DocForm2(request.GET)
#		books = Document.objects.all()
	#fn = request.GET['title']
	#ff = request.GET['for_type']
	#y = request.GET['createyear']
#	an = request.GET['createauthor']
	#dt = request.GET['doc_type']
#	d = {
#		'fn': request.GET.get('title'),
#       'ff': request.GET.get('for_type'),
#        'y': request.GET.get('createyear'),
#       'an': request.GET.get('createauthor'),
#        'dt': request.GET.get('doc_type')
#	}       
#	books['entry']=Document.objects.filter(
#		Q(author__contain=an)
#	)
	#queries=[Q(author__contains=d)]
	#books = Document.objects.all().order_by('sid')
	#books = Document.objects.filter(author='fn')
	#books = Document.objects.filter(Q(author__contains='d'))
	#books = Document.objects.filter(Q(author__contains=form.cleaned_data['createauthor']))
	#print('an')
#	return render_to_response('search/kekka.html',{'form':form, 'books': books},RequestContext(request))
	#return render_to_response('search/kekka.html',dict(book_id=book_id),context_instance=RequestContext(request))
	#return render('search/kekka.html', books)
	#return redirect('./search/kekka.html')

#def accpept(request, book_id=None):
#	d = {
#                'fn': request.GET.get('file_name'),
#                'ff': request.GET.get('file_format'),
#                'y': request.GET.get('year'),
#                'an': request.GET.get('author_name'),
#                'dt': request.GET.get('example1')
#        }

def search(request):
	form = DocForm2()
	if request.method == 'GET':
		return render_to_response('search/search_file2.html',{'form':form },RequestContext(request))
	elif request.method == 'POST':
		form = DocForm2(request.post)
		an = request.POST['createauthor']
		fn = request.POST['title']
		books = Document.filter(Q(name__contains=fn) | Q(author=an))
		return render_to_response('search/kekka.html',{'form':form, 'books':books}, RequestContext(request))

	#form = DocForm2()
	#fn = request.GET.get('file_name')
	#ff = request.GET.get('file_format')
	#y = request.GET.get('year')
	#an = request.GET.get('author_name')
	#dt = request.GET.get('example1')
#この下で動く
	#one_entries = Document.objects.filter(author='浜田哲郎')
	#print(one_entries.query)
	#return render(request, 'search/search_file.html')
	#return render_to_response('search/search_file.html',{'form':form },RequestContext(request))

