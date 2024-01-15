
from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    # rotas, views, nome referencia 
    # exemplo: se vc quiser voltar vai ter que chamar a funcao pelo nome.. exe: name=home
    path('', views.home, name='home'),   

    path('usuarios/', views.usuarios, name='listagem_usuarios'), 
   
   ]
 