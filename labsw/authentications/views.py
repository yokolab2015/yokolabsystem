from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext

from authentications.forms import UserForm
from django.contrib.auth.models import User


@login_required
def user_profile(request):
    context = RequestContext(request,
                             {'user': request.user})
    return render_to_response('user_profile.html',
                              context_instance=context)
