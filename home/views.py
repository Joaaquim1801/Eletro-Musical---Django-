from django.shortcuts import render
from home.models import Produtos, MarcaProduto, CategoriaProduto

CATEGORIAS = list(CategoriaProduto.objects.values_list('nome',flat=True)) #Sem o list ele não consegue iterar sobre
def landing(request):
    return render(request, 'home/landing.html')

def catalogo(request, filtro_produto):
    if filtro_produto in CATEGORIAS:
        categoria_produto = CategoriaProduto.objects.filter(nome=filtro_produto).first()
        produtos = Produtos.objects.filter(marcas__categoria=categoria_produto,ativo=True).distinct()
        # O distinct() é usado para evitar duplicatas se um produto tiver várias marcas na mesma categoria
        categoria_nome = filtro_produto.title()
        marca_nome = None
        marcas_categoria = list(MarcaProduto.objects.filter(categoria=categoria_produto).values_list('marca', flat=True)) # Filtra marcas pela categoria
    else:
        marca_nome = MarcaProduto.objects.filter(marca=filtro_produto).first()
        produtos = Produtos.objects.filter(marcas=marca_nome, ativo=True) if marca_nome else Produtos.objects.none()
        categoria_nome = marca_nome.categoria if marca_nome else None


    return render(request, 'home/catalogo.html', {'produtos': produtos, 'categoria_nome': categoria_nome, 'marca_nome': marca_nome, 'marcas': marcas_categoria})  # Adiciona o nome da categoria ao contexto