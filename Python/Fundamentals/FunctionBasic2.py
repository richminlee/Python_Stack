# # 1
# def acc(x):
#     for y in range(x,0,-1):
#         print(y)
# acc(10)
# # 2
# def printReturn(x,y):
#     print(x)
#     return(y)
# z=printReturn(10,5)
# print(z)
# # 3
# def length(x):
#     sum=len(x)+x[0]
#     return sum
# z=length([1,2,3,4,5])
# print(z)
# # 4
# def valGreat2(x):
#     y=[]
#     for i in range(0,len(x),1):
#         if len(x)<=2:
#             return False
#         if x[i] > x[1]:
#             y.append(x[i])
#     print(len(y))
#     if len(y) >=2:
#         return y
#     else:
#         return False
# z = valGreat2([3])
# print (z)
# 5
def tltv(s,v):
    x=[]
    for i in range(0,s,1):
        x.append(v)
    return x
z=tltv(6,2)
print(z)