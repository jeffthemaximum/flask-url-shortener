import random
from random import shuffle
import pudb


url = 'www.google.com'
short = []
my_dict = {}

for i in range(0,2):

	upper = random.randint(65, 90)
	short.append(str(unichr(int(upper))))
	lower = random.randint(97, 122)
	short.append(str(unichr(int(lower))))
	num = random.randint(10, 99)
	short.append(str(num))

shuffle(short)
new_url = "".join(short)
my_dict[url] = new_url
print my_dict