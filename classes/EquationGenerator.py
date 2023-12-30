from random import randint

class Generator:
    def __init__(self,op=0,dif=0):
            self.op = op
            self.dif = dif
            self.x = 0
            self.y = 0
            self.z = 0

    def generate(self,op,dif):
        match op:
            case ("Addition"):
                self._generate_addition(dif)
            case ("Subtraction"):
                self._generate_subtraction(dif)
            case ("Multiplication"):
                self._generate_multiplication(dif)
            case ("Division"):
                self._generate_division(dif)
        result = (self.x,self.y,self.z)
        return result

    def _generate_addition(self,dif):
        match dif:
            case ("Easy"):
                bound = 9
            case ("Medium"):
                bound = 25
            case ("Hard"):
                bound = 50
        self.x = randint(0,bound)
        self.y = randint(0,bound)
        self.z = self.x+self.y

    def _generate_subtraction(self,dif):
        match dif:
            case ("Easy"):
                lBound = 8
                uBound = 16
            case ("Medium"):
                lBound = 16
                uBound = 30
            case ("Hard"):
                lBound = 50
                uBound = 100
        self.x = randint(lBound,uBound)
        self.y = randint(0,lBound)
        self.z = self.x-self.y

    def _generate_multiplication(self,dif):
        match dif:
            case ("Easy"):
                bound = 10
            case ("Medium"):
                bound = 15
            case ("Hard"):
                bound = 20
        self.x = randint(0,bound)
        self.y = randint(0,bound)
        self.z = self.x*self.y

    def _generate_division(self,dif):
        match dif:
            case ("Easy"):
                bound = 12
            case ("Medium"):
                bound = 18
            case ("Hard"):
                bound = 25
        self.y = randint(1,bound)
        self.z = randint(1,bound)
        self.x = self.y*self.z
