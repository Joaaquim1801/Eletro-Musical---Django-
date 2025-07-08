from home.models import Carrinho

def quantidade_itens_carrinho(request):
    quantidade = 0
    if request.user.is_authenticated:
        quantidade = Carrinho.objects.filter(user=request.user).count()
    return {'total_itens_carrinho': quantidade}

def itens_carrinho(request):
    itens = []
    if request.user.is_authenticated:
        itens = Carrinho.objects.filter(user=request.user)
    return {'itens_carrinho': itens}

def usuario_logado(request):
    logado = False
    if request.user.is_authenticated:
        logado = True
    return {'logado': logado}