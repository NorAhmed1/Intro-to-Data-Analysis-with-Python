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



OUTPUT

