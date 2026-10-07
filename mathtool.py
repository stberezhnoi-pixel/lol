import sys, math
p=sys.argv[1:]
if len(p)==0 or p[0]=="--help":
 print("mathtool --- решение A*x^2+B*x+C=0\npython mathtool.py solve\npython mathtool.py solve -a 1 -b -3 -c 2\nA,B,C от -10000 до 10000")
 sys.exit(0)
if p[0]!="solve":
 print("ОШИБКА: неизвестная команда",file=sys.stderr)
 sys.exit(1)
try:
 if len(p)==1:
  a=int(input("A: "));b=int(input("B: "));c=int(input("C: "))
 else:
  if p[1]!="-a"or p[3]!="-b"or p[5]!="-c":raise
  a=int(p[2]);b=int(p[4]);c=int(p[6])
 if abs(a)>10000or abs(b)>10000or abs(c)>10000:raise
except:
 print("ОШИБКА",file=sys.stderr)
 sys.exit(1)
if a==0:
 if b==0:
  print("ОШИБКА: не уравнение",file=sys.stderr);sys.exit(1)
 print("Линейное")
 print(f"x={-c/b:.3f}")
else:
 print("Квадратное")
 d=b*b-4*a*c
 print(f"D={d}")
 if d<0:
  print("Корней нет")
 elif d==0:
  print(f"x={-b/(2*a):.3f}")
 else:
  s=math.sqrt(d)
  print(f"x1={(-b+s)/(2*a):.3f}")
  print(f"x2={(-b-s)/(2*a):.3f}")
