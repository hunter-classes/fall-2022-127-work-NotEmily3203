now = int(input("What time is it now in hours (1-24): "))
hrs = int(input("In how many hours should the alarm go off: "))
alarm = now+hrs
x=0
while x==0:
  if alarm >= 1 and alarm <=24:
    print(f"your alarm will ring at {alarm}")
    x=1
  else:
    alarm = alarm-24