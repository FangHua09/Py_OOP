# for i in range(1234,4322):
#     s= str(i)
#     if '1' in s and '2' in s and '3' in s and '4' in s :
#         print(s)

count=0
for s in [str(s) for s in range(1234,4322)]:
    if '1' in s and '2' in s and '3' in s and '4' in s :
        count+=1
        print(s,end='\n' if count%5==0 else '\t')