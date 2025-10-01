from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt # REMOVER DA PRODUÇÃO - USAR EM DEBUG APENAS

# Create your views here.
def home_view(request):
    return render(request, 'home.html')

@csrf_exempt  # REMOVER DA PRODUÇÃO - USAR EM DEBUG APENAS
def usuario_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Credenciais inválidas'})
    return render(request, 'usuario_login.html')

def usuario_cadastrar(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Aqui você pode adicionar lógica para salvar o usuário no banco de dados
        # Por simplicidade, estamos apenas redirecionando para a página de login
        return redirect('usuario_login')
    return render(request, 'usuario_cadastrar.html')