from django.shortcuts import render 
from .models import Usuario

# Create your views here.

#request parametro ja enbutido no jango 

def home(request): 
    return render(request,'usuarios/home.html')

def usuarios(request):
    #salvar dados da tela para o bando de dados  
    novo_usuario = Usuario() 
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()


    #exibir todos usuarios cadastrados em uma nova pagina 

    usuarios = {
        'usuarios': Usuario.objects.all()
    }
 

    #retorna os dados para a tela de listagem de usuarios 

    return render(request, 'usuarios/usuarios.html', usuarios)
     
# models e uma classe python que representa  uma tabela no banco de dados 

