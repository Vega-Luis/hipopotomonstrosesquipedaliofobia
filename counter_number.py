"""
una funcion recurciva de cola que tiene como objetivo contar la cantidad de digitos de un numero

"""

# def counter(number):
#     global initial
#     if number <= 1:
#         return
    
#     if initial == number:
#         print(f"su numero tiene: {initial} digitos\n Este es su numero: {a}")
#     counter(number - 1)
   

# 
# 
# 
# initial = counteres 

# counter(counteres)
counteres = 0
def counter(number):
  global counteres
  
  if counteres == 0:
    for i in number:
      counteres += 1
    number = int(0)
  if number >= counteres:
    return
      
  print(f'su numero tiene: {number} digitos\nSu numero es: {a}')
  counter(number + 1)





a = str(input('ingrese su numero: '))
counter(a)