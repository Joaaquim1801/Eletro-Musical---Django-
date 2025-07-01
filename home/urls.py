from django.urls import path
from home.views import landing, catalogo

urlpatterns = [
    path('', landing, name='landing'), #Se eu não colocar esse nomezinho eu ele não consegue buscar pelo nome para passar para a view
    path('catalogo/<str:filtro_produto>', catalogo, name='catalogo'),
]