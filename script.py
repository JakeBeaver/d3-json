from random import randint
import json

class person(object):
	def __init__(self, name, mom, dad):
		self.name = name
		self.dad = dad
		self.mom = mom
		self.out = {'name': self.name, 'children': [self.mom,self.dad]}
		
class oldest(person):
	def __init__(self, name):
		self.name = name
		self.out = {'name': self.name}
		
	
ggrandma = []
ggrandpa = []
for i in range(4):
	ggrandma.append(oldest('great grandma').out)
	ggrandpa.append(oldest('great grandpa').out)
	
grandma = []
grandpa = []
for i in range(2):
	grandma.append(person('grandma',ggrandma[i], ggrandpa[i]).out)
	grandpa.append(person('grandpa',ggrandma[3-i], ggrandpa[3-i]).out)
	
mom = person('mom',grandma[0],grandpa[0]).out
dad = person('dad',grandma[1],grandpa[0]).out

me = person('me', mom, dad).out


with open('flare.json', 'w') as output:
	json.dump(me, output)

