from django.contrib import admin
from home.models import Produtos, ImagemProduto, MarcaProduto, CategoriaProduto, SubCategoriaProduto

class ProdutosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque', 'ativo', 'mais_vendido', 'promocao')
    search_fields = ('nome', 'marca', 'modelo')
    list_filter = ( 'ativo', 'mais_vendido', 'promocao')
    prepopulated_fields = {'slug': ('nome',)}

class ImagemProdutoAdmin(admin.ModelAdmin):
    list_display = ('produto', 'destaque')
    search_fields = ('produto__nome',)
    list_filter = ('destaque',)

admin.site.register(Produtos,ProdutosAdmin)
admin.site.register(ImagemProduto,ImagemProdutoAdmin)
admin.site.register(MarcaProduto)
admin.site.register(CategoriaProduto)
admin.site.register(SubCategoriaProduto)
