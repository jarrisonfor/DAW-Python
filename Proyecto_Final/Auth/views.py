from django.shortcuts import render
from django.contrib.auth import login
from django.views import View
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class Registrar(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('monitor')
        return render(request, 'registration/register.html')

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('monitor')
        usuario = request.POST['usuario']
        password = request.POST['password']
        email = request.POST['email']
        try:
            user = User.objects.get(username=usuario)
            return render(request, 'registration/register.html', {'alreadyExist': True})
        except ObjectDoesNotExist:
            user = User.objects.create_user(usuario, email, password)
            user.save()
            login(request, user)
            return redirect('monitor')