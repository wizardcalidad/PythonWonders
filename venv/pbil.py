'''
word = "alphabetical"
i =0
for i in range(12):
    if i % 3 ==0:
        print(word.index, end=' ')
    else:
        continue
'''
word = "alphabetical"

# for i,j in enumerate(word,1):
#     if(i%3==0):
#         print(j,end='')

for i,j in enumerate("alphabetical", 1):
    if(i%3==0):
        print(j,end='')