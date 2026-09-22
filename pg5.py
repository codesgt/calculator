from math import *
# function of addition substraction multiplication and division only
def Addi():
    a=list(map(float,input("enter number: ").split()))
    atotal=0
    for a2 in a:
     atotal=atotal + a2
    print("total= ",atotal)
    return atotal
#Addi()
def Subst():
   ss=list(map(float,input("enter number: ").split()))
   stotal=0
   for ss2 in ss:
    stotal=stotal-ss2
    stotal=fabs(stotal)
   print("total= ",stotal)
   return stotal
#Subst()
def Multi():
  mm=list(map(float,input("enter number: ").split()))
  mtotal=1
  for mm2 in mm:
    mtotal=mtotal*mm2
  print("total= ",mtotal)
  return mtotal
#Multi()
def Division():
  dd=list(map(float,input("enter number: ").split()))
  dtotal=dd[0]
  for dd2 in dd[1:]:
    dtotal=dtotal/dd2 
  print("total= ",dtotal)
  return dtotal
#Division()
print("calculator:")
print("always press enter key after entering value: ")
print("please enter sign for caculating:")
sign=input("sign= ")
if sign=='+' or sign=='-' or sign=='*' or sign=='/' :
    if sign=='+':
      total=Addi()
    elif sign=='-':
      total=Subst()
    elif sign=='*':
      total=Multi()
    elif sign=='/':
      total=Division()
    else:
      print("some thing wrong:")  
    #print("continue press 0:")
    conti=input("press 9 to exit\npress 0 to continue= ")
    if conti=='0':
      print("please enter sign for caculating:")
      sign=input("sign= ")
      if sign=='+' or sign=='-' or sign=='*' or sign=='/' :
        if sign=='+':
          n1=list(map(float,input("enter number: ").split()))
          for n in n1:
           total=total+n
          print("total= ",total)
          #Addi()
        elif sign=='-':
          n1=list(map(float,input("enter number: ").split()))
          for n in n1:
           total=total-n
          print("total= ",total)
          #Subst()
        elif sign=='*':
          n1=list(map(float,input("enter number: ").split()))
          for n in n1:
           total=total*n
          print("total= ",total)
          #Multi()
        elif sign=='/':
          n1=list(map(float,input("enter number: ").split()))
          for n in n1:
           total=total/n
          print("total= ",total)
          #Division()
        else:
          print("some thing wrong:")  
    else:
      print("you did not enter 0:")
else:
  print("you entered wrong sign:")
print("end!")
   

    