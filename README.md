![Texto alternativo](916cfbf2-311c-4a17-ac93-03fca837b992.png)
# 🎵 Eletro Musical - Website Django
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

Um sistema completo de e-commerce para loja de instrumentos musicais, desenvolvido com Django e múltiplas funcionalidades modernas.

## 📋 Sobre o Projeto

Este projeto foi criado com o propósito de testar conhecimentos em Django e elaborar um website completo para uma loja de instrumentos musicais. O sistema oferece desde cadastro e autenticação de usuários até um sistema completo de compra de produtos online com integração ao WhatsApp através da biblioteca PyWhatKit.

## 🚀 Tecnologias Utilizadas

- **Python** - Linguagem principal
- **Django** - Framework web
- **Django Allauth** - Sistema de autenticação
- **JavaScript** - Interatividade frontend
- **PyWhatKit** - Automação de mensagens WhatsApp
- **HTML/CSS** - Interface do usuário
- **SQLite** - Banco de dados (desenvolvimento)

## ⚡ Funcionalidades Principais

### 🛒 Sistema de E-commerce Completo
- **Catálogo de Produtos**: Visualização completa dos produtos cadastrados via Admin Panel
- **Página Dedicada**: Cada produto possui sua própria página com detalhes completos
- **Sistema de Avaliação**: Usuários registrados podem avaliar produtos com estrelas e comentários
- **Carrinho de Compras**: Adicionar produtos, modificar quantidades e gerenciar itens
- **Busca Dinâmica**: Pesquisa por nome e filtros avançados
- **Filtros Inteligentes**: Por categoria, marca e modificadores de ordem (A-Z, preço, etc.)

### 📱 Integração WhatsApp
- **Finalização Automática**: Ao finalizar compra, o usuário é direcionado ao WhatsApp
- **Mensagem Formatada**: Informações do carrinho são enviadas automaticamente
- **Contato Direto**: Comunicação direta com a loja

### 🔐 Sistema de Autenticação
- **Registro e Login**: Sistema completo de usuários
- **Autenticação Google**: Login social integrado

## 🛠️ Instalação e Configuração

### Pré-requisitos
- Python 3.8+
- pip (gerenciador de pacotes Python)

### Passo a Passo

1. **Clone o repositório**
```bash
git clone https://github.com/seu-usuario/eletro-musical.git
cd eletro-musical
```

2. **Crie e ative o ambiente virtual**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```
3. **Instale as dependências**
```python
pip install -r requirements.txt
```
4. **Configure as variáveis de ambiente**
Crie um arquivo `.env` na raiz do projeto com:
```env
envSECRET_KEY='sua-secret-key-aqui'
AUTH_GOOGLE_CLIENT_ID='seu-google-client-id'
AUTH_GOOGLE_SECRET='seu-google-secret'
```
Para gerar a SECRET_KEY:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

5. **Execute as migrações**

```bash
python manage.py migrate
```

6. **Crie um superusuário**

```bash
python manage.py createsuperuser
```

7. **Execute o servidor**

```bash
python manage.py runserver
```

## 🔧 Configuração da Autenticação Google
Para configurar o login com Google, siga estas etapas:

  1. Acesse o Google Cloud Console;
  2. Crie um novo projeto ou selecione um existente;
  3. Ative a API do Google+;
  4. Configure as credenciais OAuth 2.0;
  5. Adicione as credenciais no arquivo .env;

📹 Tutorial em vídeo ( Créditos: Canal pythonando ): https://www.youtube.com/watch?v=qdOX-6Zhugs
## 📁 Estrutura do Projeto
```
eletro-musical/
├── setup/              # Configurações do Django
├── templates/          # Templates HTML
├── static/            # Arquivos estáticos (CSS, JS, imagens)
├── media/             # Arquivos de mídia (uploads)
├── usuarios/          # App de usuários
├── venv/              # Ambiente virtual
├── .env               # Variáveis de ambiente
├── requirements.txt   # Dependências
└── manage.py         # Gerenciador Django
```
## 🎯 Comandos Úteis
```bash
# Ajuda com comandos do Django
python manage.py help

# Criar superusuário
python manage.py createsuperuser

# Executar servidor de desenvolvimento
python manage.py runserver

# Criar migrações
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Coletar arquivos estáticos
python manage.py collectstatic
```
## 📊 Admin Panel
Acesse /admin/ para gerenciar:

* Produtos e categorias
* Usuários e permissões
* Avaliações e comentários
* Configurações do sistema

🤝 Contribuindo

 1. Faça um fork do projeto
 2. Crie uma branch para sua feature (git checkout -b feature/AmazingFeature)
 3. Commit suas mudanças (git commit -m 'Add some AmazingFeature')
 4. Push para a branch (git push origin feature/AmazingFeature)
 5. Abra um Pull Request

# 📝 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
# 📞 Contato
* Joaquim Maia - joaquimaiafilho2018@gmail.com
* Link do Projeto: https://github.com/Joaaquim1801/Eletro-Musical---Django-/

⭐ Se este projeto te ajudou, considere dar uma estrela no repositório!
