class Product:
    def __init__(self, product_id, nome, descricao, preco, categoria, dono):
        self.id = product_id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.categoria = categoria
        self.dono = dono  # ID do usuário dono do produto

    @classmethod
    def from_dict(cls, data):
        return cls(data["id"], data["nome"], data["descricao"], data["preco"], data["categoria"], data["dono"])