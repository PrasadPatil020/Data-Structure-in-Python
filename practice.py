mylist =  [1,2,3,4,5]
for num in mylist:
    print(num,end  = ' ')

#finding even and odd numbers
for num in mylist:
    if num % 2 == 0:
        print(f'Even Number:{num}',end='')
    else:
        print(f'\nOdd Number:{num}')

#addition of list numbers
addition = 0
for num in mylist:
    addition = addition + num
print(f'\nAddition:{addition}')

#reading string using for loop
for letter in 'Hi Prasad':
    print(letter,end='')
#tuples
tup = (1,2,3,4,5)
for num in tup:
    print('\n',num,end='')

#tuple packing
tup = [(1,2),(3,4),(5,6)]
for num in tup:
    print('\n',num)

tup = [(1,2,3),(4,5,6)]
for a,b,c in tup:
    print(b)

#Dictionary
d = {'k1':1,'k2':2,'k3':3}
for num in d.items():
    print(num)
for a,b in d.items():
    print(b)