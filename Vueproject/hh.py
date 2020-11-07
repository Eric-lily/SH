a=int(input('请输入第一个数'))
b=int(input('请输入第二个数'))
greater=0
def zuixiao(a,b):
    if a>=b:
        greater=a
    else :
        greater=b
    while(True):
        if(greater%a==0 and greater%b==0):
            break
        else:
            greater+=1
            
    print('%d和%d的最小公倍数为%d'%(a,b,greater))
zuixiao(a,b)