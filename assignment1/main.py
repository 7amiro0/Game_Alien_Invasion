def number(*n):
   w = []
   for q in n:
       e = q ** 2
       w.append(int(e))
   return (w)

def number1(*n):
   w = []
   r = int(input('Pleas enter power: '))
   for q in n:
       e = q ** r
       w.append(int(e))
   return (w)

number(1, 2, 2.5, 3)
number1(1, 2, 2.5, 3)