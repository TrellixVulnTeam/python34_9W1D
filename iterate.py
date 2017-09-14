lst = ['Chopin', 'Bizet', 'Ravel', \
       'Beethoven', 'Brahms', 'Dutilleaux']

print('-------')
#BAD !!!
x = lst[0]
print(x + ' was a composer')

x = lst[1]
print(x + ' was a composer')

x = lst[2]
print(x + ' was a composer')
print('-------')

#use a for each loop:

for name in lst:
    print(name + ' was a composer')

    
