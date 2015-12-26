from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,  # 追加する
)

from django.http import HttpResponse
from django.views.decorators.http import require_POST  # 追加する
from docmng.models import Document  # 追加する
from .forms import MessageForm  # 追加する
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.decorators import login_required
from .forms import UploadForm






def handle_uploaded_file(f,t):
    with open(t, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def index(request):
    request.session[u'username'] = "1170364"

    #Filename= message.file.name.rsplit('/',1)[1]
    d = {
        'messages': Document.objects.all(),
    }
    return render(request, 'download/index.html', d)


def add(request):
    if 'username' in request.session:
        username = int(request.session['username'])
    else:
        # セッション情報無しの場合
        return render(request,'download/login.html')

    form = UploadForm(request.POST or None,request.FILES or None)
    d = {
        'form': form,
        'username': username,
    }
    if form.is_valid():

        b = Document(name = request.POST['name'], author = request.POST['author']
                     ,type = request.POST['type'],format = request.POST['format']
                     ,sid = username, path = request.FILES['path'])
        #a = b.Document(Sid = username)
        b.save()

        return HttpResponseRedirect('/download/',d)

    return render(request, 'download/edit.html', d)
##
def edit(request, editing_id):
    message = get_object_or_404(Document, id = editing_id)
    if request.method == 'POST':
        form = UploadForm(request.POST,request.FILES)
        if form.is_valid():
            #handle_uploaded_file(request.FILES['file'],request.FILES['file'].name)
            message.message = form.cleaned_data['message']
            message.title = form.cleaned_data['title']
            message.path = form.cleaned_data['file']

            message.save()
            return HttpResponseRedirect('/download/')
    else:
        # GETリクエスト（初期表示）時はDBに保存されているデータをFormに結びつける
        form = UploadForm()

    d = {
        'form': form,
    }
    return render(request, 'download/edit.html', d)



def download(request, editing_id):
    if 'username' in request.session:
        username = request.session['username']
    else:
        # セッション情報無しの場合
        return render(request,'download/login.html')

    message = get_object_or_404(Document, id=editing_id)
    zip_string = (message.file)
    response = HttpResponse(zip_string, content_type=None)
    Filename= message.file.name.rsplit('/',1)[1]
    #test = 'サモンズボード.png'
    #print(test)
    #print(Filename)
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
    return redirect('download:index')

def delete_file(sender, instance, **kwargs):
    instance.file.delete(False)


##
def user_login(request):

    if request.POST:
        form = Login_form(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if request.GET.get('next') is not None:
                        # Redirect to a success page.
                        return redirect(request.GET['next'])

    # New form when not the request is get.
    else:
        form = Login_form()
    return render(request, 'download/login.html', {'form' : form})

class Login_form(forms.Form):
    username = forms.CharField(label="User name")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    def clean(self):
        cleaned_data = super(Login_form, self).clean()
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if not authenticate(username=username, password=password):
            raise forms.ValidationError("Wrong user name or passwsord")
        return self.cleaned_data

def user_logout(request):
    logout(request)
    return render(request, 'download/logout.html')

@login_required
def add_user(request):
    if request.POST:
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            username       = request.POST['username']
            password       = request.POST['password']
            email          = request.POST['email']
            new_user = User.objects.create_user(username = username, email = email, password=password)
            new_user.is_active = True
            new_user.save()
            return render(request, 'download/add_user_successful.html')

    else:
        form = MyUserCreationForm()
    return render(request, 'download/add_user.html', {'form' : form})

class MyUserCreationForm(forms.Form):
    username = forms.CharField(label = "User name")
    password = forms.CharField(label = "Password", widget = forms.PasswordInput)
    password_bis = forms.CharField(label = "Password", widget = forms.PasswordInput)
    email = forms.EmailField(label = "Email")
    def clean(self):
        cleaned_data = super(MyUserCreationForm, self).clean()
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        password_bis = self.cleaned_data.get('password_bis')
        if password and password_bis and password != password_bis:
            raise forms.ValidationError("Passwords are not identical.")
        user_check = User.objects.filter(username = username).exists()
        if user_check:
            raise forms.ValidationError("Duplicate user name!")
        return self.cleaned_data