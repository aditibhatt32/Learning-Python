chars=['A','B','C']
fruit=('apple','banana','mango')
dict={'name':'Aditi','ref':'python','branch':'cse'}
print('element:',end='')
for item in chars:
    print(item,end='')
    for item in enumerate(chars):
     print(item)
     for itwm in zip(chars,fruit):
         print(item,end='')
         for key,value in dict.items():
             print(key,'=',value)
         
