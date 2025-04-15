import uuid
import os
import json
from models.user import User
from models.category import Category
from models.product import Product


class Sistema:
    def __init__(self):
        self.usuarios = []
        self.categorias = []
        self.produtos = []
        self.sessoes = {}  # token: user_id

        # Diretório base para os arquivos
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.USUARIOS_FILE = os.path.join(self.BASE_DIR, "usuarios.txt")
        self.CATEGORIAS_FILE = os.path.join(self.BASE_DIR, "categorias.txt")
        self.PRODUTOS_FILE = os.path.join(self.BASE_DIR, "produtos.txt")

        # Carregar dados ao iniciar o sistema
        self.carregar_dados()

    def gerar_id(self):
        return str(uuid.uuid4())

    # Métodos de persistência
    def salvar_dados(self):
        """Salva os dados em arquivos .txt no formato JSON."""
        try:
            with open(self.USUARIOS_FILE, "w") as f:
                f.write(json.dumps([u.__dict__ for u in self.usuarios]))
            with open(self.CATEGORIAS_FILE, "w") as f:
                f.write(json.dumps([c.__dict__ for c in self.categorias]))
            with open(self.PRODUTOS_FILE, "w") as f:
                f.write(json.dumps([p.__dict__ for p in self.produtos]))
        except Exception as e:
            print(f"Erro ao salvar os dados: {e}")

    def carregar_dados(self):
        """Carrega os dados de arquivos .txt no formato JSON."""
        try:
            if os.path.exists(self.USUARIOS_FILE):
                with open(self.USUARIOS_FILE, "r") as f:
                    self.usuarios = [User(**u) for u in json.loads(f.read())]
            if os.path.exists(self.CATEGORIAS_FILE):
                with open(self.CATEGORIAS_FILE, "r") as f:
                    self.categorias = [Category.from_dict(c) for c in json.loads(f.read())]
            if os.path.exists(self.PRODUTOS_FILE):
                with open(self.PRODUTOS_FILE, "r") as f:
                    self.produtos = [Product.from_dict(p) for p in json.loads(f.read())]
        except Exception as e:
            print(f"Erro ao carregar os dados: {e}")

    # Métodos de usuários
    def registrar_usuario(self, nome, email, senha):
        if any(u.email == email for u in self.usuarios):
            print("E-mail já cadastrado!")
            return
        user = User(self.gerar_id(), nome, email, senha)
        self.usuarios.append(user)
        self.salvar_dados()  # Salva os dados após registrar
        print("Usuário registrado com sucesso!")

    def login(self, email, senha):
        for user in self.usuarios:
            if user.email == email and user.senha == senha:
                token = self.gerar_id()  # Gera um token simples
                self.sessoes[token] = user.id
                print(f"Login bem-sucedido! Seu token é: {token}")
                return token
        print("Email ou senha inválidos!")
        return None

    def get_user_by_token(self, token):
        user_id = self.sessoes.get(token)
        return next((u for u in self.usuarios if u.id == user_id), None)

    # Métodos de categorias
    def criar_categoria(self, nome):
        nome_normalizado = nome.strip().lower()  # Normaliza o nome da categoria
        if any(c.nome.lower() == nome_normalizado for c in self.categorias):
            print("Categoria já existe!")
            return
        categoria = Category(self.gerar_id(), nome_normalizado)
        self.categorias.append(categoria)
        self.salvar_dados()  # Salva os dados após criar categoria
        print("Categoria criada com sucesso!")

    # Métodos de produtos
    def cadastrar_produto(self, token, nome, descricao, preco, nome_categoria):
        user = self.get_user_by_token(token)
        if not user:
            print("Usuário não autenticado!")
            return

        nome_categoria_normalizado = nome_categoria.strip().lower()  # Normaliza o nome da categoria
        categoria = next((c for c in self.categorias if c.nome.lower() == nome_categoria_normalizado), None)
        if not categoria:
            print("Categoria não encontrada!")
            return

        produto = Product(self.gerar_id(), nome, descricao, preco, categoria.nome, user.id)
        self.produtos.append(produto)
        self.salvar_dados()  # Salva os dados após cadastrar produto
        print("Produto cadastrado com sucesso!")

    def listar_produtos_do_usuario(self, token):
        user = self.get_user_by_token(token)
        if not user:
            print("Usuário não autenticado!")
            return

        produtos_usuario = [p for p in self.produtos if p.dono == user.id]
        if not produtos_usuario:
            print("Nenhum produto cadastrado.")
        else:
            for p in produtos_usuario:
                print(f"- {p.nome} |\n {p.descricao} |\n R$ {p.preco:.2f} |\n Categoria: {p.categoria}")