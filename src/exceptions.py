
class NotFoundErorr(Exception):
    entity_name: str

    def __init__(self):
        super().__init__(f"{self.entity_name} not found")


class ItemNotFoundErorr(NotFoundErorr):
    entity_name = "Item"
