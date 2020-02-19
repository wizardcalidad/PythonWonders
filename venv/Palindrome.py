# name = input('Type str: ')
# new_name = ""
# for c in name:
#     if c != "'" and c!= " ":
#         new_name += c
# new_name = new_name.lower()
# print(new_name == new_name[::-1])










'''method two of solving this'''
name = input('Type here: ')

new_name = ''
for c in name:
    new_name = c + new_name

#print('name ={}, new_name = {}, is palidrome = {}'.format(name,new_name,name==new_name))
print('name =%s, new_name = %s, is palidrome = %r'%(name,new_name,name==new_name))
