from django.shortcuts import render_to_response
from django.shortcuts import redirect, render
from django.template import RequestContext
from django.core.context_processors import csrf 
from django.http import HttpResponse
from docmng.models import Userinfo
from docmng.models import UserForm

def register(request):
    users = Userinfo()
    form = None
    if request.method == 'POST':
       form = UserForm(request.POST, instance=users)
       if form.is_valid():
          newuser = form.save(commit=False)
          newuser.save()
          return render_to_response('confirm.html', {'newuser':newuser}, context_instance=RequestContext(request))
       pass
    else:
       form = UserForm(instance = users)
    return render_to_response('register.html', {'form':form}, context_instance=RequestContext(request))

def create_user(request):
    return render_to_response('createuser.html', {}, context_instance=RequestContext(request))

def delete(request):
    #管理者ならば(セッション管理)adminページへ移動
    #if admin
    #users = Userinfo.objects.all()
    #return render_to_response('admin.html', {'users':users}, context_instance=RequestContext(request))

    return render_to_response('delete.html', {}, context_instance=RequestContext(request))

def complete(request):
    id = request.POST.getlist('id')
    possword = request.POST.getlist('password')
   # if id:
   #    Userinfo.objects.filter(id__in=id).delete()
   # else:
   #   return redirect('delete')
    if possword:
       deleteuser = Userinfo.objects.filter(password=possword)
       #loginuser = ...
       if deleteuser:
          deleteuser.delete()
       else:
          return HttpResponse("パスワードが間違っています")
    return HttpResponse("削除しました")
