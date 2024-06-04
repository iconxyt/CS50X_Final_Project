from django.db import models

class Number(models.Model):
    number = models.PositiveBigIntegerField(default=0)
    isPrime = models.BooleanField()

    def __str__(self):
        return self.number

    def TestisPrime(self):
        prime = True
        for x in range(2, self.number):
            if self.number % x == 0:
                prime = False
        if self.number == 1:
            prime = False
        return prime

    def divisors(self):
        divs = list()
        for x in range(1, self.number + 1):
            if self.number % x == 0:
                divs.append(x)
        return divs

    def isEven(self):
        if self.number % 2 == 0:
            return True
        else:
            return False

    def isPerfect(self):
        divs = list()
        for x in range(1, self.number + 1):
            if self.number % x == 0:
                divs.append(x)
        if sum(divs) - self.number == self.number:
            return True
        else:
            return False

    def getbinary(self):
        return bin(self.number)