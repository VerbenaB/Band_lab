from src.musician import Musician 

class Bassist (Musician):
    
    def play(self):
        return super().play() + "bass"