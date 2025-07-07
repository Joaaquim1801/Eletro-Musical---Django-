from django.shortcuts import render, redirect, get_object_or_404
from home.models import Produtos, MarcaProduto, CategoriaProduto, Carrinho
from unidecode import unidecode
from django.contrib import messages

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

CATEGORIAS = list(CategoriaProduto.objects.values_list('nome',flat=True)) #Sem o list ele não consegue iterar sobre
def landing(request):

    produtos_top_vendas = Produtos.objects.filter(ativo=True, mais_vendido=True).order_by('-id')[:7]  # Obtém os 7 produtos mais recentes
    produtos_promocao = Produtos.objects.filter(ativo=True, promocao=True).order_by('-id')[:7]  # Obtém os 7 produtos em promoção mais recentes
    return render(request, 'home/landing.html',{'produtos_mais_vendidos': produtos_top_vendas, 'produtos_promocao': produtos_promocao})

def catalogo(request, filtro_produto):

    sort = request.GET.get('sort', 'nome')
    marcas_selecionadas = request.GET.getlist('marcas_lista_checkboxs')
    subcategorias_selecionadas = request.GET.getlist('subcategorias_lista_checkboxs')
    marcas_categoria = []
    subcategorias = []
    subcategorias_ids = set()

    if filtro_produto in CATEGORIAS:

        #Variáveis
        categoria_produto = CategoriaProduto.objects.filter(nome=filtro_produto).first() # Obtém a categoria do produto
        produtos = Produtos.objects.filter(marcas__categoria=categoria_produto,ativo=True).distinct() # Utiliza a foreignkey da marcas, que por sua vez tem a foreignkey da categoria
        # O distinct() é usado para evitar duplicatas se um produto tiver várias marcas na mesma categoria
        categoria_nome = filtro_produto.title()
        marca_nome = None

        #Quantidade de produtos da marca na side bar de marcas
        for marca in MarcaProduto.objects.filter(categoria=categoria_produto).distinct().values_list('marca', flat=True):
            qntd_produtos_marca = Produtos.objects.filter(marcas__marca=marca, marcas__categoria=categoria_produto).count()  # Conta quantos produtos existem para cada marca na categoria
            marcas_categoria.append((marca, qntd_produtos_marca))

        #Sidebar de subcategorias
        for produto in produtos:
            if produto.subcategoria and produto.subcategoria.id not in subcategorias_ids:
                subcategoria = produto.subcategoria.nome
                subcategoria_id = produto.subcategoria.id
                qntd_produtos_subcategoria_marca = produtos.filter(subcategoria=subcategoria_id).count()
                subcategorias.append((subcategoria_id,subcategoria,qntd_produtos_subcategoria_marca))
                subcategorias_ids.add(subcategoria_id)

    else:

        #Variáveis
        categorias_nomes = []
        marca_nome = MarcaProduto.objects.filter(marca=filtro_produto) #Pega o id da marca
        produtos = Produtos.objects.filter(marcas__in=marca_nome, ativo=True) if marca_nome else Produtos.objects.none()
        categoria_nome = filtro_produto

        # Sidebar de marcas
        for produto in produtos:
            for marca in produto.marcas.all():
                for marca_objeto in MarcaProduto.objects.filter(marca=marca.marca).distinct():
                    categorias_nomes.append(marca_objeto.categoria)

        categoria_produto = CategoriaProduto.objects.filter(nome__in=categorias_nomes)

        #Quantidade de produtos da marca na side bar de marcas
        for marca in MarcaProduto.objects.filter(marca=filtro_produto).distinct().values_list('marca', flat=True):
            qntd_produtos_marca = Produtos.objects.filter(marcas__marca=marca, marcas__categoria__in=categorias_nomes).count()  # Conta quantos produtos existem para cada marca na categoria
            marcas_categoria.append((marca, qntd_produtos_marca))

        #Sidebar de subcategorias
        for produto in produtos:
            if produto.subcategoria and produto.subcategoria.id not in subcategorias_ids:
                subcategoria = produto.subcategoria.nome
                subcategoria_id = produto.subcategoria.id
                qntd_produtos_subcategoria_marca = produtos.filter(subcategoria=subcategoria_id).count()
                subcategorias.append((subcategoria_id,subcategoria,qntd_produtos_subcategoria_marca))
                subcategorias_ids.add(subcategoria_id)

    # Checkboxs marcas
    if marcas_selecionadas:
        produtos = produtos.filter(marcas__marca__in=marcas_selecionadas).distinct()
    
    # Checkboxs subcategorias
    if subcategorias_selecionadas:
        produtos = produtos.filter(subcategoria__in=subcategorias_selecionadas).distinct()

    # Ordernar por:

    if sort == 'nome':
        produtos = produtos.order_by('nome')
    elif sort == 'menor_preco':
        produtos = produtos.order_by('preco')
    elif sort == 'maior_preco':
        produtos = produtos.order_by('-preco')
    elif sort == 'lancamento':
        produtos = produtos.order_by('-criado_em')
    elif sort == 'desconto':
        produtos = sorted(produtos, key=lambda x: x.desconto_percentual, reverse=True)  # Ordena os produtos por desconto percentual

            
#flat = True -> ele ajusta a lista criada para que os itens não sejam tuplas únicas, mas sim o valor de que tupla [(x),(y)] -> [x,y]

    
    return render(request, 'home/catalogo.html', {'produtos': produtos, 'categoria_nome': categoria_nome,'marcas': marcas_categoria, 'request': request, 'marcas_selecionadas': marcas_selecionadas, 'subcategorias': subcategorias, 'subcategorias_selecionadas': subcategorias_selecionadas})  # Adiciona o nome da categoria ao contexto

def buscar(request):
    
    #Variáveis
    sort = request.GET.get('sort', 'nome')
    marcas_selecionadas = request.GET.getlist('marcas_lista_checkboxs')
    subcategorias_selecionadas = request.GET.getlist('subcategorias_lista_checkboxs')
    subcategorias = []
    subcategorias_ids = set()
    marcas_nomes = []
    categorias_nomes = []

    #Verificação da busca
    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            produtos = Produtos.objects.filter(nome_sem_acentos__icontains=unidecode(nome_a_buscar), ativo=True)
            if not produtos.exists(): #Verifica a existência
                return redirect('erro_busca')
            
            
    for produto in produtos:
        for marca in produto.marcas.all():
            nome_marca = marca.marca
            if nome_marca not in [m[0] for m in marcas_nomes]:
                categorias_nomes.append(marca.categoria)
                qntd_produtos_marca = Produtos.objects.filter(marcas__marca=marca.marca, marcas__categoria=marca.categoria).count()
                marcas_nomes.append((marca.marca, qntd_produtos_marca))

        if produto.subcategoria and produto.subcategoria.id not in subcategorias_ids:
                subcategoria = produto.subcategoria.nome
                subcategoria_id = produto.subcategoria.id
                qntd_produtos_subcategoria_marca = produtos.filter(subcategoria=subcategoria_id).count()
                subcategorias.append((subcategoria_id,subcategoria,qntd_produtos_subcategoria_marca))
                subcategorias_ids.add(subcategoria_id)

    #Caso o que for digitado for a categoria dos produtos
    if nome_a_buscar in CATEGORIAS:
        categoria_produto = CategoriaProduto.objects.filter(nome=nome_a_buscar).first()
        produtos = Produtos.objects.filter(marcas__categoria=categoria_produto,ativo=True).distinct() 

        #Quantidade de produtos da marca na side bar de marcas
        for marca in MarcaProduto.objects.filter(categoria=categoria_produto).distinct().values_list('marca', flat=True):
            qntd_produtos_marca = Produtos.objects.filter(marcas__marca=marca, marcas__categoria=categoria_produto).count()  # Conta quantos produtos existem para cada marca na categoria
            marcas_nomes.append((marca, qntd_produtos_marca))

        #Sidebar de subcategorias
        for produto in produtos:
            if produto.subcategoria and produto.subcategoria.id not in subcategorias_ids:
                subcategoria = produto.subcategoria.nome
                subcategoria_id = produto.subcategoria.id
                qntd_produtos_subcategoria_marca = produtos.filter(subcategoria=subcategoria_id).count()
                subcategorias.append((subcategoria_id,subcategoria,qntd_produtos_subcategoria_marca))
                subcategorias_ids.add(subcategoria_id)

            
    #Checkboxs marcas
    if marcas_selecionadas:
        produtos = produtos.filter(marcas__marca__in=marcas_selecionadas).distinct()

    #Checkboxs subcategorias
    if subcategorias_selecionadas:
        produtos = produtos.filter(subcategoria__in=subcategorias_selecionadas).distinct()
    
    #Ordernar por
    if sort == 'nome':
        produtos = produtos.order_by('nome')
    elif sort == 'menor_preco':
        produtos = produtos.order_by('preco')
    elif sort == 'maior_preco':
        produtos = produtos.order_by('-preco')
    elif sort == 'lancamento':
        produtos = produtos.order_by('-criado_em')
    elif sort == 'desconto':
        produtos = sorted(produtos, key=lambda x: x.desconto_percentual, reverse=True)

    return render(request, 'home/buscar.html', {'produtos': produtos,'categoria_nome': 'busca', 'marcas': marcas_nomes, 'request': request, 'marcas_selecionadas': marcas_selecionadas,'subcategorias': subcategorias, 'subcategorias_selecionadas': subcategorias_selecionadas})
#Tem que passar o parâmetro request dentro do dicionário para disponibilizar o objeto no template

def erro_busca(request):
    return render(request, 'home/erro_busca.html')

def pagina_produto(request,produto_nome):
    produto = Produtos.objects.get(id=produto_nome)
    subcategoria_produto = produto.subcategoria.id
    produtos_relacionados = Produtos.objects.filter(subcategoria=subcategoria_produto).exclude(id=produto.id).order_by('id')[:4]
    marca =  ''.join([n.marca for n in produto.marcas.all()]) #Isso converte uma lista única em uma string

    if request.method == "POST":
        acao = request.POST.get("acao")
        if acao == 'adicionar':
            messages.success(request, f'Produto adicionado ao carrinho com sucesso')
        
        return redirect('pagina_produto', produto.id)

    return render(request, 'home/pagina_produto.html',{'produto_objeto': produto, 'marca_produto': marca, 'produtos_relacionados': produtos_relacionados})

@csrf_exempt
def atualizar_quantidade(request):
    if request.method == 'POST' and request.user.is_authenticated:
        dados = json.loads(request.body)
        produto_id = dados.get('produto_id')
        quantidade = int(dados.get('quantidade', 1))
        acao = dados.get('acao')

        produto = Produtos.objects.get(id=produto_id)

        carrinho_item, criado = Carrinho.objects.get_or_create(
            user=request.user,
            produto=produto,
            defaults={'quantidade': quantidade}
        )

        if not criado:
            if acao == "produto":
                carrinho_item.quantidade += quantidade
                carrinho_item.save()
            else:
                carrinho_item.quantidade = quantidade
                carrinho_item.save()

        return JsonResponse({'status': 'ok', 'quantidade': carrinho_item.quantidade})

    return JsonResponse({'status': 'erro'}, status=400)