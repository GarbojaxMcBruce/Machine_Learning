import random
class Hunter:
    name = ''
    value = 0
    
    
    def __init__(self, name, value):
        self.name = name
        self.value = value
        
    def auto_move(self):
        return [random.randint(-1, 1), random.randint(-1, 1)]

    def return_value(self):
        return self.value
    