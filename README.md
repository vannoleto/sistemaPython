
# 🐍 Sistema de Gerenciamento via Terminal em Python

Este é um sistema simples de gerenciamento de **usuários**, **categorias** e **produtos** desenvolvido em **Python**, com funcionamento via **terminal (modo texto)** e armazenamento de dados em arquivos `.txt`.

---

## 📁 Estrutura dos Arquivos

- **`user.py`** – Define a classe `User`, que representa um usuário com nome, e-mail e senha.
- **`category.py`** – Define a classe `Category`, que representa uma categoria de produtos.
- **`product.py`** – Define a classe `Product`, que representa os produtos cadastrados.
- **`sistema.py`** – Contém toda a lógica de funcionamento do sistema.
- **`main.py`** – Arquivo principal que exibe o menu e controla a interação do usuário.

---

## 💾 Armazenamento dos Dados

Os dados do sistema são salvos em **arquivos `.txt`**, garantindo que as informações permaneçam mesmo após o fechamento do programa:

- `usuarios.txt`
- `categorias.txt`
- `produtos.txt`

> Embora seja possível usar arquivos `.json`, foi escolhida a abordagem com `.txt` para manter o projeto 100% em Python puro, sem bibliotecas externas.

---

## 🔄 Funcionalidades do Sistema

### 1️⃣ Registrar Usuário
- O usuário informa nome, e-mail e senha.
- O sistema verifica se o e-mail já está cadastrado.
- Os dados são salvos em `usuarios.txt`.

### 2️⃣ Login
- O usuário informa e-mail e senha.
- Se os dados estiverem corretos, o sistema gera um **token de sessão** que identifica o usuário logado.

### 3️⃣ Criar Categoria
- Após o login, o usuário pode criar novas categorias (ex: Eletrônicos, Roupas).
- O sistema não permite nomes repetidos.
- As categorias são salvas em `categorias.txt`.

### 4️⃣ Cadastrar Produto
- O usuário cadastra produtos com nome, descrição, preço e categoria.
- O sistema verifica se a categoria existe antes de permitir o cadastro.
- Os dados são armazenados em `produtos.txt`.

### 5️⃣ Listar Meus Produtos
- Lista todos os produtos cadastrados pelo usuário logado.

### 6️⃣ Sair
- Encerra o programa. Todos os dados ficam salvos para a próxima execução.

---

## 🖥️ Exemplo de Menu no Terminal

```
=== MENU ===
1 - Registrar novo usuário
2 - Login
3 - Criar categoria
4 - Cadastrar produto
5 - Listar meus produtos
6 - Sair
```

---

## 🚀 Como Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```

2. Navegue até a pasta do projeto:
   ```bash
   cd nome-da-pasta
   ```

3. Execute o programa:
   ```bash
   python main.py
   ```

---

## 🛠️ Requisitos

- Python 3.x instalado na máquina.
- Nenhuma biblioteca externa é necessária (Python puro).

---

## 📌 Observações

- O sistema pode ser expandido para usar arquivos JSON, banco de dados ou interface gráfica.
- Ideal para quem está aprendendo lógica de programação, orientação a objetos e manipulação de arquivos em Python.

---

## 🧑‍💻 Autor

Desenvolvido por **Vanderson Noleto**  
📧 Email: vandersondbv7@gmail.com 
🔗 GitHub: [https://github.com/seu-usuario](https://github.com/vannoleto)

---


