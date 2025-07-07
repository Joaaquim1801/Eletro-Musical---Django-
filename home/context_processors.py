from home.models import Carrinho
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def quantidade_itens_carrinho(request):
    quantidade = Carrinho.objects.filter(user=request.user).count()
    return {'total_itens_carrinho': quantidade}

def itens_carrinho(request):
    itens = Carrinho.objects.filter(user=request.user)
    soma_produtos = 0
    for item in itens:
        preco = item.produto.preco * item.quantidade
        soma_produtos += preco
    soma_formatada = locale.currency(soma_produtos, grouping=True, symbol=False)
    return {'itens_carrinho': itens}