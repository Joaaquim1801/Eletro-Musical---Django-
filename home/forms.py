from django import forms
from home.models import AvaliacoesProduto

class AvaliacoesProdutoForms(forms.ModelForm):
    class Meta:
        model = AvaliacoesProduto
        fields = ['comentario']
        labels = {'comentario': 'Comentário'}

        widgets = {
            'nota': forms.HiddenInput(),
            'comentario': forms.TextInput(attrs={'placeholder': 'Dê detalhes sobre o produto...', 'class': 'comentario-textarea'})
        }
    
    def clean_comentario(self):
        comentario = self.cleaned_data.get('comentario','').strip()
        if not comentario:
            raise forms.ValidationError('O comentário não pode ser enviado vazio')
        return comentario
