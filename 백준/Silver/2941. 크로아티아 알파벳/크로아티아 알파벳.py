word = input()
word_list = ['c=','c-','dz=','d-','lj','nj','s=','z=']
cnt = 0

for i in word_list:
    word = word.replace(i,'_')
print(len(word))