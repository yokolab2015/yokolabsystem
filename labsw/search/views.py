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
from .forms import DocFormE
from .forms import DocForm2


def search(request):
	username = request.user
	v = username. is_active
	if v:
		username = request.user
	else:
	# セッション情報無しの場合
		return HttpResponseRedirect('/login/')

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


def delete(request, editing_id):
	username = request.user
	v = username. is_active
	#p = 'yes'
	#i = 0
	if v:
		username = request.user
	else:
	# セッション情報無しの場合
		return HttpResponseRedirect('/login/')

	message = get_object_or_404(Document, id = editing_id)
	v2 = username.is_staff
	username = str(username)
	if v2:
		message.delete()
	else:
		if message.author == username:
			message.delete()
		else:
			return HttpResponse('ユーザが違います')
		
	form = DocForm2()
	books = Document.objects.all()
	return render_to_response('search/kekka.html',{'form':form, 'books':books}, RequestContext(request))

'''	if delete_ids:
		v2 = username.is_staff
		if v2:
			Document.objects.filter(id__in=delete_ids).delete()
		else:
			while p != 'No':
				try:
					p = Document.objects.filter(id__in=delete_ids).values_list('name',flat=True)[1]
				except IndexError:
					p = 'No'
				an = str(p)
				username = str(username)
			#username = '\''+ str(username)+'\''
			#if '['+ [username + ',']* username + ']' == an:
				return HttpResponse(an)
				if username != an:
					return HttpResponse('出来ぬ')
				elif p == 'No':
					#Document.objects.filter(id__in=delete_ids).delete()
					return HttpResponse('削除しました！！')
				i = i + 1'''



def delete_file(sender, instance, **kwargs):
    instance.file.delete(False)


def edit(request, editing_id):
	message = get_object_or_404(Document, id = editing_id)
	if request.method == 'POST':                         
		form = DocFormE(request.POST,request.FILES)    
		if form.is_valid():
			message.name = form.cleaned_data['title'] 
			message.author = form.cleaned_data['createauthor']
			#message.day = form.cleaned_data['createyear']
			message.format = form.cleaned_data['for_type']
			message.type = form.cleaned_data['doc_type']
			message.path = form.cleaned_data['path']		
			message.save()
			#return HttpResponseRedirect('/search/')
			#return render(request, 'search/kekka.html')
			books = Document.objects.all()
			return render_to_response('search/kekka.html',{'form':form, 'books':books}, RequestContext(request))

	else:                                            
        # GETリクエスト（初期表示）時はDBに保存されているデータをFormに結びつける
		form = DocFormE()
	d = {
       		'form': form,
	}
	return render(request, 'search/edit.html', d)    
