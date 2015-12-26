from django.shortcuts import render_to_response
from django.shortcuts import redirect, render
from django.template import RequestContext
from django.core.context_processors import csrf 
from django.http import HttpResponse
from docmng.models import Userinfo
from docmng.models import UserForm

def register(request):
    if request.method == 'POST':
       user = Userinfo()
       form = UserForm(request.POST, instance=user)

       if form.is_valid():
          newuser = form.save(commit=False)
          newuser = Userinfo.objects.create_user(user.username, user.email, user.password)
          newuser.number = user.number
          newuser.fuclty = user.fuclty
          newuser.save()
          return render_to_response('confirm.html', {'newuser':newuser}, context_instance=RequestContext(request))
       pass
    else:
       user = Userinfo()
       form = UserForm(instance=user)
    return render_to_response('register.html', {'form':form}, context_instance=RequestContext(request))

'''
    users = Userinfo()
    form = None
    if request.method == 'POST':
       form = UserForm(request.POST, instance=users)
       if form.is_valid():
          newuser = form.save(commit=False)
          newuser.save()
       pass
    else:
       form = UserForm(instance = users)
'''

def create_user(request):
    return render_to_response('createuser.html', {}, context_instance=RequestContext(request))

def delete(request):
    #管理者ならば(セッション管理)adminページへ移動
    #if admin
    #users = Userinfo.objects.all()
    #return render_to_response('admin.html', {'users':users}, context_instance=RequestContext(request))

    return render_to_response('delete.html', {}, context_instance=RequestContext(request))

def complete(request):
    p = request.POST['password']
    deleteuser = Userinfo.objects.filter(password=p)
    if deleteuser:
       deleteuser.delete()
    else:
       return HttpResponse("パスワードが間違っています")

    return HttpResponse("削除しました")

def adcomp(request):
    id = request.POST.getlist('id')
    if id:
       Userinfo.objects.filter(id__in=id).delete()
    else:
      return redirect('delete')
