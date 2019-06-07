f=open("dict4.txt",'w')
chars=[
                '0','1','2','3','4','5','6','7','8','9',
                'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
#                'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
            ]
base=len(chars) #62
end=len(chars)**4
j = 0
for i in range(0,end):
    n=i
    ch0=chars[n%base]
    t1 = (n%base)>=10
    n=n/base
    ch1=chars[n%base]
    t2 = (n%base)>=10
    n=n/base
    ch2=chars[n%base]
    t3 = (n%base)>=10
    n=n/base
    ch3=chars[n%base]
    t4 = (n%base)>=10
    if (not t1 and t2 and t3 and t4) or (t1 and not t2 and t3 and t4) \
    or (t1 and t2 and not t3 and t4) or (t1 and t2 and t3 and not t4):
        j = j + 1
        print j,ch3,ch2,ch1,ch0
        f.write(ch3+ch2+ch1+ch0+"\n")
f.close()
