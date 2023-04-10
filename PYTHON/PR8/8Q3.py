class ComplexNumber:
    def __init__(self, r, i):
        self.r = r
        self.i = i
 
    def __add__(self, other):
        return ComplexNumber(self.r + other.r, self.i + other.i)
 
    def __sub__(self, other):
        return ComplexNumber(self.r - other.r, self.i - other.i)
 
    def __mul__(self, other):
        real = self.r * other.r - self.i * other.i
        imag = self.r * other.i + self.i * other.r
 
        if real == 0 and imag == 0:
            raise ValueError("The product is zero.")
 
        return ComplexNumber(real, imag)
 
    def __str__(self):
        if self.i >= 0:
            return f"{self.r} + {self.i}i"
        else:
            return f"{self.r} - {-self.i}i"
 
C1 = ComplexNumber(1, -2)
C2 = ComplexNumber(3, 4)
print('C1:',C1)
print('C2:',C2)
print('C1 + C2:',C1 + C2)
print('C1 - C2:',C1 - C2)
print('C1 * C2:',C1 * C2)
