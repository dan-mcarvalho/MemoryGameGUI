class Cartas:

    def __init__(self, value, pos, rect, indice):
        self.value = value
        self.pos = pos
        self.rect = rect
        self.flip = indice

    def check_card(self, carta):
        if self.value == carta.value:
            return True
        else:
            return False
