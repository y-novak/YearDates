from calendar import monthrange
y=2018
for m in range(1,13):
  for d in range(1,monthrange(y,m)[1]+1):
    print'%s%s/%s%s/%s'%('0'if m<10else'',m,'0'if d<10else'',d,y)