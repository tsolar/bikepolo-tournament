from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect


def index(request):
    return HttpResponse('esto es el index de accounts')

    
def profile(request):
    if '_auth_user_id' not in request.session:
        return redirect(reverse('base_index'))
    else:
        user_pk = request.session['_auth_user_id']
    user = User.objects.get(pk=user_pk)
    context = dict(
        user=user
    )
    return render(request, 'accounts/profile.html', context)
