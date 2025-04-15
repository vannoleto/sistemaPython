class Category:
    def __init__(self, category_id, nome):
        self.id = category_id
        self.nome = nome

    @classmethod
    def from_dict(cls, data):
        return cls(data["id"], data["nome"])