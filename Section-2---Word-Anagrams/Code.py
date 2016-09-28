word = open('/Users/nickwalker/Downloads/Ex_Files_Intro_Analysis_Python/Exercise Files/Ch3/03_02/words', 'r')
wordlist = word.readlines()
print (wordlist[:10])
print (len(wordlist))
'Aaron/n'.strip()
'Aaron'.lower()
wordclean = [word.strip().lower() for word in wordlist]
print (wordclean[:10])

# to remove duplicates, turn the list into a Python set which is a container that can only have one instance of any given object
# and then turn it back into a list
wordunique = list(set(wordclean))
print(wordunique[:10])
wordunique.sort()
print(wordunique[:10])

# to be consise with all that above.. you could write:
wordclean = sorted(list(set([word.strip().lower() for word in open('/Users/nickwalker/Downloads/Ex_Files_Intro_Analysis_Python/Exercise Files/Ch3/03_02/words', 'r')])))
print (wordclean[:10])

print (sorted('lives'))
print (sorted('lives') == sorted('elvis'))
print (sorted('love') == sorted('hate'))

def signature(word):
    return ''.join(sorted(word))
print (signature('lives'))

print('/'.join(['a','b','c']))

def anagram(myword):
    return [word for word in wordclean if signature(word) == signature(myword)]
print (anagram('dictionary'))
            
# now we could create a dict of all the words indexed by their signature
    # if we have that, then getting an anagram for myword would be as simple as looking up the dictionary element for the signature of myword
    # every item in the dictionary will have a signature as the key and a list of words as the value

# words_bysig = {}
# for word in wordclean:
#    words_bysig[signature(word)].append(word)

import collections

words_bysig = collections.defaultdict(list)

for word in wordclean:
    words_bysig[signature(word)].append(word)

def anagram_fast(myword):
    return words_bysig[signature(myword)]

print (anagram_fast('nicholas'))



OUTPUT

['A\n', 'a\n', 'aa\n', 'aal\n', 'aalii\n', 'aam\n', 'Aani\n', 'aardvark\n', 'aardwolf\n', 'Aaron\n']
235886
['a', 'a', 'aa', 'aal', 'aalii', 'aam', 'aani', 'aardvark', 'aardwolf', 'aaron']
['starlite', 'hemautography', 'desired', 'inspiration', 'planospiral', 'territorialization', 'triode', 'unentrenched', 'deforester', 'inwale']
['a', 'aa', 'aal', 'aalii', 'aam', 'aani', 'aardvark', 'aardwolf', 'aaron', 'aaronic']
['a', 'aa', 'aal', 'aalii', 'aam', 'aani', 'aardvark', 'aardwolf', 'aaron', 'aaronic']
['e', 'i', 'l', 's', 'v']
True
False
eilsv
a/b/c
['dictionary', 'indicatory']
['lichanos', 'nicholas']
