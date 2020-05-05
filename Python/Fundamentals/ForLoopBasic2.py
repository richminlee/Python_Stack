#1
# def biggie(y):
#     for x in range (0,len(y),1):
#         if y[x]>=0:
#             y[x]="big"
#     return y
# z=biggie([-1,3,5,-5])
# print(z)
#2
# def count(x):
#     y=[]
#     for i in range(0,len(x),1):
#         if x[i]>0:
#             y.append(x[i])
#     x[len(x)-1]=len(y)
#     return x
# z=count ([1,6,-4,-2,-7,-2])
# print(z)
#3
# def sum(x):
#     sum=0
#     for i in range(0,len(x),1):
#         sum+=x[i]
#     return sum
# z=sum([6,3,-2])
# print(z)
#4
# def ave(x):
#     aver=0
#     for i in range(0,len(x),1):
#         aver+=x[i]
#     aver/=len(x)
#     return aver
# z=ave([1,2,3,4])
# print(z)
#5
# def leng(x):
#     return len(x)
# z=leng([])
# print(z)
#6
# def mini(x):
#     if len(x)==0:
#         return False
#     else:
#         for i in range (0,len(x),1):
#             y=x[0]
#             if x[i]<y:
#                 y=x[i]
#         return y
# z=mini([37,2,1,-9])
# print(z)
#7
# def max(x):
#     if len(x)==0:
#         return False
#     else:
#         for i in range (0,len(x),1):
#             y=x[0]
#             if x[i] >y:
#                 y=x[i]
#         return y
# z=max([37,2,1,-9])
# print(z)
#8
# def ana(x):
#     sumTotal=0
#     average=0
#     minimum=x[0]
#     maximum=x[0]
#     length=len(x)
#     y={}
#     for i in range (0,len(x),1):
#         sumTotal+=x[i]
#         average=sumTotal/len(x)
#         if x[i]<minimum:
#             minimum=x[i]
#         if x[i]>maximum:
#             maximum=x[i]
#     y={'sumTotal':sumTotal, 'average': average,'minimum':average,'minimum':minimum,'maximum':maximum,'length':length}
#     return y
# z=ana([37,2,1,-9])
# print(z)
#9
def reverse(x):
    for i in range(len(x)-1,-1,-1):
        x.append(x[i])
    y=int(len(x)/2)
    for i in range(0,y,1):
        x.pop(0)
    return x    
z=reverse([37,2,1,-9])
print(z)