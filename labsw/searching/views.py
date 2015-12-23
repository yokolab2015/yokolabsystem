from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
#from labsw.searching.models import Choice, Poll
from django.shortcuts import get_object_or_404, render_to_response
#from django import forms
from django.template import RequestContext
from django.core.urlresolvers import reverse
#from labsw.docmng.models import docmng
from django.shortcuts import render_to_response, get_object_or_404
from docmng.models import Document
from . import models
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello.")

def detail(request, searching_id):
	#return HttpResponse("You are looking at poll %s." % searching_id)
	p = get_object_or_404(Document, pk=searching_id)
	return render_to_response('searching/detail.html', {'searching': p})

def vote(request, searching_id):
	#p = get_object_or_404(Document, pk=searching_id)
	#try:
	#	selected_choice = p.choice_set.get(pk=request.POST['choice'])
	#except (KeyError, Choice.DoesNotExist):
	# Poll 投票フォームを再表示します。
	#	return render_to_response('searching/detail.html', {
	#	'searching': p,
	#	'error_message': "選択肢を選んでいません。",
	#})
	#else:
	#	selected_choice.votes += 1
	#	selected_choice.save()
	return HttpResponseRedirect('labsw.searching.views.results')

def results(request, searching_id):
	p = get_object_or_404(searching, pk=searching_id)
	return render_to_response('searching/results.html', {'searching': p})

# Create your views here.
