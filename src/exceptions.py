
class NotFoundErorr(Exception):
    entity_name: str

    def __init__(self):
        super().__init__(f"{self.entity_name} not found")


class ItemNotFoundErorr(NotFoundErorr):
    entity_name = "Item"


class NotEnoughItems(Exception):
    def __init__(self, e):
        super(NotEnoughItems, self).__init__(f"Don't enough items in database. {e}")


class WrongTypeError(ValueError):
    def __init__(self):
        super().__init__(f"You try pass a wrong type. item points must be float or int type.")
