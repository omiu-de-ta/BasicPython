def judge(n):
    i=2#割る数
    flag=0#判定フラグ

    while i < n:
        if n%i == 0:
            flag = 1
            break
        else :
            i += 1    
    if flag==0:
        return True
    else:        
        return False
    
k=judge(61)
if k:
        print('素数です')
else:
        print('素数ではない')
k = judge(10)
if k:
        print('素数です')
else:
        print('素数ではない')           