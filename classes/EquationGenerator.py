from random import randint

class Generator:
    def __init__(self,op=0,dif=0):
            self.op = op
            self.dif = dif
            self.x = 0
            self.y = 0
            self.z = 0

    def generate(self,op,dif):
        match dif:
            case ("Easy"):
                bound = 10
            case ("Medium"):
                bound = 15
            case ("Hard"):
                bound = 25

        match op:
            case ("Addition"):
                self._generate_addition(bound)
            case ("Subtraction"):
                self._generate_subtraction(bound)
            case ("Multiplication"):
                self._generate_multiplication(bound)
            case ("Division"):
                self._generate_division(bound)

        result = (self.x,self.y,self.z)
        return result

    def _generate_addition(self,bound):
        self.x = randint(0,bound)
        self.y = randint(0,bound)
        self.z = self.x+self.y

    def _generate_subtraction(self,bound):
        self.x = randint(0,bound)
        self.y = randint(0,self.x)
        self.z = self.x-self.y

    def _generate_multiplication(self,bound):
        self.x = randint(0,bound)
        self.y = randint(0,bound)
        self.z = self.x*self.y

    def _generate_division(self,bound):
        self.y = randint(1,bound)
        self.z = randint(1,bound)
        self.x = self.y*self.z
