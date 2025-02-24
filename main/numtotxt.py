''' slom hammaga men 19 yoshdaman '''
def a2b(a,b,src):
    s=''
    src=src[::-1]
    for i in range(a,b,-1):
        s+=src[i]
    return s
def int2strdef(x):
    els=['','ming ',' million ' ,' milyard',' trillion']
    a=[["","bir ","ikki ","uch ", "to'rt ","besh ","olti ","yetti ","sakkiz ","to'qqiz "],
["", "o'n ","yigirma ","o'ttiz ","qirq ","ellik ","oltmish ","yetmish ","sakson ","to'qson "],
["","bir yuz ","ikki yuz ","uch yuz ","to'rt yuz ", "besh yuz ", "olti yuz ", "yetti yuz ","sakkiz yuz ","to'qqiz yuz "]]
    numb=''
    ind=0
    xs=str(x)
    ln=len(xs)
    for i in xs[::-1]:
        ct=''
        ind+=1
        nd=ind-1
        if ind%3==1:
            if ind+2<ln:
                st = ind + 1
                stop = ind - 2
                ct= ['', els[ind // 3]][bool(int(a2b(st, stop, xs)))]
            else:
                ct=els[ind//3]
        numb=a[nd%3][int(i)]+ct+numb 
    return numb
def inttostr(x):
    a=['','bir ','o\'n ','yuz ']
    els = ['','ming ', 'million ', 'milyard ', 'trillion ']
    xs=str(x)
    s=''
    xs=xs.split('.')
    if len(xs)==2:
        ln=len(xs[1])
        n=(ln%3)+1
        if xs[0]=='0':
            s='nol butun '+a[n]+els[ln//3]+'dan '+int2strdef(int(xs[1]))
        else:
            s=int2strdef(int(xs[0]))+'butun '+a[n]+els[ln//3]+'dan '+int2strdef(int(xs[1]))
    if len(xs)==1:
        s=int2strdef(xs[0])
    return s

print(inttostr(0))