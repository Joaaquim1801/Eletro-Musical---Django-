from django import forms
from home.models import AvaliacoesProduto

class AvaliacoesProdutoForms(forms.ModelForm):
    class Meta:
        model = AvaliacoesProduto
        fields = ['nota', 'comentario']
        labels = {'comentario': 'Comentário'}

        widgets = {
            'nota': forms.HiddenInput(),
            'comentario': forms.Textarea(attrs={'placeholder': 'Dê detalhes sobre o produto...'})
        }