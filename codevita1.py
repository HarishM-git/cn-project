n=int(input())
a=[input().strip() for _ in range(n)]
valid=True
final1=0
final2=0
last_ch=None
last_ch2=None
if (len(a)!=n):
  print('-1')
else:
  for i in a:
    if i not in ['down','up','right','left']:
      valid=False
      print('-1')
      break
  if(valid):
    arr=a[:2]
    arre=a[:2]
    for it in (a[2:]):
      if it not in arr:
        if last_ch==None:
          arr[0]=it
          last_ch=0
        else:
          if last_ch==0:
            arr[1]=it
            last_ch=1
          elif last_ch==1:
            arr[0]=it
            last_ch=0
        final1+=1
    for itr in (a[2:]):
      if itr not in arre:
        if last_ch2==None:
          arre[1]=itr
          last_ch2=1
        else:
          if last_ch2==1:
            arre[0]=itr
            last_ch2=0
          elif last_ch2==0:
            arre[1]=itr
            last_ch2=1
        final2+=1
    print(min(final1,final2))
        
        
        