from numbers import Number

lst = ['cat', 2, 'dog', 3.1, 'Chopin', 17]

for item in lst:
    #if str(item).isnumeric() :
    if isinstance(item, Number):
        print(item)

print('done')
