import random,string

def random_generator(size=8,chars=string.ascii_lowercase+string.digits):#generates 8 characters with letters and digits
    return ''.join(random.choice(chars) for x in range(size))

email = random_generator()+'@gmai.com'
print(email)
