# x = [ [5,2,3], [10,8,9] ] 
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]
# x[1][0]=15
# print(x)
# students[0]['last_name'] = 'Bryant'
# print(students)
# sports_directory['soccer'][0]='Andres'
# print(sports_directory)
# z[0]['y']=30
# print(z)


# students = [
#         {'first_name':  'Michael', 'last_name' : 'Jordan'},
#         {'first_name' : 'John', 'last_name' : 'Rosales'},
#         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#         {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]
# for i in range(0,len(students),1):
#         print("first_name - "+ students[i]['first_name'] + ", "+"last_name - " + students[i]['last_name'])


# iterateDictionary(students) 
# # should output: (it's okay if each key-value pair ends up on 2 separate lines;
# # bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel
# students = [
#         {'first_name':  'Michael', 'last_name' : 'Jordan'},
#         {'first_name' : 'John', 'last_name' : 'Rosales'},
#         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#         {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]

# def iterateDictionary2(a,b):
#         for i in range(0,len(b),1):
#                 print(b[i][a])
# iterateDictionary2('first_name',students)
# iterateDictionary2('last_name',students)
# dojo = {
#    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }
# def printInfo(a):
#         for k in a:
#                 print(len(a[k]), str.upper(k))
#                 for i in range(0,len(a[k]),1):
#                         print(a[k][i])
# printInfo(dojo)
# arr = [1,3,5,7]
# arr[0], arr[3] = arr[3], arr[0]
# arr[1], arr[2] = arr[2], arr[1]
# print(arr)
arr=[8,1,5,3,2,0]

def bubbleSort(arr):
        print('came here')
bubbleSort(arr)