from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html') # Supondo que você tenha um template chamado 'home.html'


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Altere o redirecionamento aqui para uma URL válida
            return redirect('home') # Redireciona para a página inicial após o login
        else:
            return render(request, 'usuarios/login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'usuarios/login.html', {'form': form})

# User = get_user_model() # Parece que você já importou User diretamente

def LogoutView(request):
    # Sua lógica de logout aqui (provavelmente uma classe do django.contrib.auth.views)
    pass

def RegisterView(request):
    # Sua lógica de registro aqui (provavelmente uma classe)
    pass

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    # serializer_class = RegisterSerializer # Descomente se você tiver um serializer

@login_required
def profile_view(request):
    user = request.user
    context = {
        'user': user,
        # Adicione outras informações do perfil que você queira exibir
    }
