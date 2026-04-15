def tractar_cas():
   for i in tractar_cas:
       k = int(input())
       local = 0
       visitant = 0
       for i in k:
           equip, punts = input().split()
           punts = int(punts)
           if equip == 'L':
               local += punts
           else:
               visitant += punts
       if local > visitant :
           guanya = "L"
       elif visitant > local :
           guanya = 'V'
       else:
           guanya = 'E'
 


casosPendents = int(input())
while casosPendents > 0:
   tractar_cas()
   casosPendents -= 1