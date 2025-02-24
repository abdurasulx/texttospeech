import  numtotxt
import  sys
import re


def chech_nums(s):
    full=''
    dotc=False
    cs=''
    last=''
    for i in s:
        if i in ['0','1','2','3','4','5','6','7',"8","9"]:
            cs=cs+i
        else:
            if cs!=''  and i!='.':
                if dotc==False:
                    full=full+ numtotxt.inttostr (int(cs))
                    cs=''
                else:
                    full = full + numtotxt.inttostr(float(cs))
                    cs = ''
                    dotc=False
            if i!='.':
                full = full + i
            if i=='-':
                a=[]
        if i=='.':
            # if  dotc==True and cs!='':
            #     full = full + numtotxt.inttostr(float(cs))
            #     cs=''
            if (cs!='') and (dotc==False):
                cs=cs+i
                dotc=True
    return full
#print(numtotxt.inttostr(3.89))
a="Stiv Jobs (Steven Paul Jobs) — dunyoga mashhur amerikalik biznesmen, ishlab chiqaruvchi va Apple kompaniyasining asoschilaridan biri bo'lgan. U 1955-yil 24-fevralda San-Fransiskoda tug‘ilgan va 2011-yil 5-oktabrda vafot etgan. Jobs texnologiya va dizayn sohasida katta ta'sir ko'rsatgan shaxs bo'lib, Apple kompaniyasini dunyoning eng muvaffaqiyatli texnologiya brendlaridan biriga aylantirdi."

b=a.split()

# for i in b:
#     print(i)
print(chech_nums(a))