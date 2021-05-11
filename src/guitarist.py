from src.musician import Musician 

class Guitarist(Musician):
    def play(self):
        return super().play() + "guitar"