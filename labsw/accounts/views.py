from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from django.core.context_processors import csrf 
from django.http import HttpResponse
from accounts.models import Userinfo
from accounts.models import UserForm

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
    #users = Userinfo()
    #return render_to_response('admin.html', {'users':users}, context_instance=RequestContext(request))

    return render_to_response('delete.html', {}, context_instance=RequestContext(request))

def complete(request):
    p = request.POST['password']
    #loginuser = Userinfo.objects.filter()
    deleteuser = Userinfo.objects.filter(password = p)
    if deleteuser == 'NULL':
       return HttpReaponse("パスワードが間違っています")
    #if loginuser == deleteuser:
    #   deleteuser.delete()
    #   return HttpResponse("削除しました")
    #else:
    #    return redirect(delete)
    else:
       deleteuser.delete()
       return HttpResponse("削除完了しました")

