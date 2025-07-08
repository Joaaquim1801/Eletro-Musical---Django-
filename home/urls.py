from django.urls import path
from home.views import landing, catalogo, buscar, erro_busca,pagina_produto, atualizar_quantidade, mandar_mensagem_whatsapp

urlpatterns = [
    path('', landing, name='landing'), #Se eu não colocar esse nomezinho eu ele não consegue buscar pelo nome para passar para a view
    path('catalogo/<str:filtro_produto>', catalogo, name='catalogo'),
    path('buscar', buscar, name='buscar'),
    path('erro_busca', erro_busca, name='erro_busca'),
    path('pagina_produto/<str:produto_nome>', pagina_produto, name='pagina_produto'),
    path('atualizar_quantidade/', atualizar_quantidade, name='atualizar_quantidade'),
    path('mandar_mensagem_whatsapp/',mandar_mensagem_whatsapp,name='mandar_mensagem_whatsapp')
]