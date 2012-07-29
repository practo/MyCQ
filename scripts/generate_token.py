import sys
import random
from mycq import user_store

if len(sys.argv) > 1:
    count = int(sys.argv[1])
else:
    count = 20

while count > 0:
    token = '{token:06d}'.format(token=random.randint(0, 999999))
    if user_store.sadd('signup_tokens', token) == 0:
        continue
    print token
    count -= 1
