from django.shortcuts import render, get_object_or_404
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
#from .forms import DocForm
from .forms import DocForm2
from django.utils.http import urlencode
#from django import html
# Create your views here.
from django.db.models.manager import QuerySet
#from download import views
#from .models import Message 

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


def search(request):
	form = DocForm2()
	if request.method == 'POST':
		form = DocForm2(request.POST)
		an = request.POST['createauthor']
		fn = request.POST['title']
		y = request.POST['createyear']
		ff = request.POST['for_type']
		dt = request.POST['doc_type']
		books = Document.objects.filter(Q(name__contains=fn) & Q(author__contains=an) & Q(day__contains=y) & Q(format__contains=ff) & Q(type__contains=dt))
		return render_to_response('search/kekka.html',{'form':form, 'books':books}, RequestContext(request))
	else :
		return render_to_response('search/search_file2.html',{'form':form },RequestContext(request))

def download(request, editing_id):
    message = get_object_or_404(Document, id=editing_id)
    zip_string = (message.path)                        
    response = HttpResponse(zip_string, content_type=None)
    Filename= message.path.name.rsplit('/',1)[1]                                                
    response['Content-Disposition'] = 'attachment; filename =' + Filename
    d = {                                                                
        'messages': Document.objects.all(),                               
    }                                                                    
    return response


def delete(request):
    delete_ids = request.POST.getlist('delete_ids')
    if delete_ids:                                 

        #os.remove(Message.objects.filter(id__in=delete_ids).name)
        Document.objects.filter(id__in=delete_ids).delete()        
    return redirect('search:search')                             


def delete_file(sender, instance, **kwargs):
    instance.file.delete(False)


def edit(request, editing_id):
	message = get_object_or_404(Document, id = editing_id)
	if request.method == 'POST':                         
		form = DocForm2(request.POST,request.FILES)    
		if form.is_valid():                              
            #handle_uploaded_file(request.FILES['file'],request.FILES['file'].name)
            #message.message = form.cleaned_data['message']                         
			message.name = form.cleaned_data['title']                             
			message.author = form.cleaned_data['createauthor']
			#message.day = form.cleaned_data['createyear']
			message.format = form.cleaned_data['for_type']
			message.type = form.cleaned_data['doc_type']
			message.save()
			return HttpResponseRedirect('/search/')
	else:                                            
        # GETリクエスト（初期表示）時はDBに保存されているデータをFormに結びつける
		form = DocForm2()
	d = {
       		'form': form,
	}
	return render(request, 'search/edit.html', d)    
