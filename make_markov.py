from collections import defaultdict, Counter
from pprint import pprint

# phrase = 'if you only read the books that everyone else is reading you can only think what everyone else is thinking'
# phrase = 'happiness is a gift and the trick is not to expect it but to delight in it when it comes'
# phrase = 'the difference between the right word and the almost right word is the difference between lightning and a lightning bug'
# phrase = 'We the People of the United States in Order to form a more perfect Union establish Justice insure domestic Tranquility provide for the common defence promote the general Welfare and secure the Blessings of Liberty to ourselves and our Posterity do ordain and establish this Constitution for the United States of America'
phrase = 'The studio was filled with the rich odour of roses and when the light summer wind stirred amidst the trees of the garden there came through the open door the heavy scent of the lilac or the more delicate perfume of the pink flowering thorn'

phrase = phrase.lower().split(' ')
chain = defaultdict(lambda: defaultdict(int))

for i in range(len(phrase)-1):
    chain[phrase[i]][phrase[i+1]] += 1
chain = dict(chain)
non_def = dict()
for k, v in chain.items():
    for key, val in val.items():
        chain[k][key] = val
    
pprint(chain)