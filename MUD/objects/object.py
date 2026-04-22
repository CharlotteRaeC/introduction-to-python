class Object:
    def __init__(
        self,
        d,
    ):
        self.name = d.get("name")
        self.room_description = d.get("room_description")
        self.key_words = d.get("key_words")
        self.description = d.get("description")
        self.take = False


class Item(Object):
    def __init__(self, d):
        super().__init__(d)
        self.weight = d.get("weight", 0)
        self.mod = d.get("mod", [])
        self.take = True


class Weapon(Item):
    def __init__(self, d):
        super().__init__(d)
        self.dice = d.get("dice", "1d6")
        self.hitroll = d.get("hitroll", 0)
        self.damroll = d.get("damroll", 0)
