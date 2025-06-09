from django.urls import path
from home.views import landing

urlpatterns = [
    path('landing', landing, name='landing'), #Se eu não colocar esse nomezinho eu ele não consegue buscar pelo nome para passar para a view
]