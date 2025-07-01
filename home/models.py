from django.db import models
from django.utils.text import slugify

class Produtos(models.Model):

    nome = models.CharField(max_length=100, null=False, blank=False)
    slug = models.SlugField(unique=True, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    preco_original = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    modelo = models.CharField(max_length=100, null=False, blank=False)
    estoque = models.IntegerField(null=False, blank=False)
    mais_vendido = models.BooleanField(default=False)
    promocao = models.BooleanField(default=False)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    autualizado_em = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        # Gera o slug automaticamente com base no nome
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)

class ImagemProduto(models.Model):

    produto = models.ForeignKey(Produtos, on_delete=models.CASCADE, related_name='imagens')
    imagem = models.ImageField(upload_to='produtos/', null=False, blank=False)
    destaque = models.BooleanField(default=False)

    def __str__(self):
        return f'Imagem de {self.produto.nome}'
    #antes estava self.nome, e a classe ImagemProduto não tinha o campo nome, por isso tive que associar com o produto

class MarcaProduto(models.Model):
    produto = models.ForeignKey(Produtos, on_delete=models.CASCADE, related_name='marcas')
    marca = models.CharField(max_length=100, null=False, blank=False)
    categoria = models.ForeignKey('CategoriaProduto', on_delete=models.CASCADE, related_name='marcas')

    def __str__(self):
        return f'Marca de {self.produto.nome}: {self.marca}'
    
class CategoriaProduto(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)   