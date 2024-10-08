for _ in range(int(input())):
    n=int(input())
    s=list(map(int,input().split(" ")))
    d=s
    count=0
    if len(s)!=n:
        print("not a valid inp")
    
    else:
        ss=max(set(s), key=s.count)
        for i in s:
          if ss==i:
            count+=1
        print(len(d)-count)  
        
            