r,t,m=input().split()
r=int(r)
t=int(t)
m=int(m)
if r>t and r>m:
  print(r)
elif t>r and t>m:
  print(t)
else:
  print(m)
