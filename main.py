#2. feladat: Hozzon létre egy olyan függvényt, amely két érték közül visszatér a nagyobb értékkel!

'''Lehetséges Megoldás'''

def maximum(x, y):
  if x >= y:
    return x
  else:
    return y

#2. feladat: Hozzon létre egy olyan függvényt, amely két érték közül visszatér a kisebb értékkel!
    
'''Lehetséges Megoldás'''

def minimum(x, y):
  if x <= y:
    return x
  else:
    return y

#2. feladat: Hozzon létre egy olyan függvényt, amely egy értéknek visszatér az abszolút értékével!

'''Lehetséges Megoldás'''

def abszolut(x):
  if x > 0:
    return x
  else:
    return -x
