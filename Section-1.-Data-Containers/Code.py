nephews = ['Huey', 'Dewey', 'Louie']
print (nephews[0])
print (nephews[2])
print (len(nephews))

mix_it_up = [1,[2,3],'alpha']
print (mix_it_up)

nephews.append('April')
print(nephews)

nephews.extend(['June', 'July'])
print(nephews)

months = nephews + ['August']
print(months)

months.sort()
print(months)

print (months[-1])


# Dictionaries


capitals = {'United States': 'Washington, DC', 'France': 'Paris', 'Italy': 'Rome'}
print (capitals['Italy'])
capitals['Spain'] = 'Madrid'
print (capitals['Spain'])

morecapitals = {'Germany': 'Berlin', 'United Kingdom': 'London'}
capitals.update(morecapitals)
print (capitals)


# Comprehensions

squares = []
for i in range(10):
    squares.append(i**2)
print (squares)
    
squares = [i**2 for i in range(10)]
print (squares)
    # this is a much more concise way to write it

squares3 = [i**2 for i in range(30) if i % 3 == 0]
print (squares3)

squares3_dict = {i: i**2 for i in range(30) if i % 3 == 0}
print (squares3_dict)

# To transpose:
capitals_bycapital = {capitals[key]: key for key in capitals}
print (capitals_bycapital)





# OUTPUT

Huey
Louie
3
[1, [2, 3], 'alpha']
['Huey', 'Dewey', 'Louie', 'April']
['Huey', 'Dewey', 'Louie', 'April', 'June', 'July']
['Huey', 'Dewey', 'Louie', 'April', 'June', 'July', 'August']
['April', 'August', 'Dewey', 'Huey', 'July', 'June', 'Louie']
Louie
Rome
Madrid
{'United Kingdom': 'London', 'Italy': 'Rome', 'United States': 'Washington, DC', 'Germany': 'Berlin', 'Spain': 'Madrid', 'France': 'Paris'}
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 9, 36, 81, 144, 225, 324, 441, 576, 729]
{0: 0, 18: 324, 3: 9, 21: 441, 6: 36, 24: 576, 9: 81, 27: 729, 12: 144, 15: 225}
{'London': 'United Kingdom', 'Rome': 'Italy', 'Berlin': 'Germany', 'Madrid': 'Spain', 'Paris': 'France', 'Washington, DC': 'United States'}

