from mycq import user_store
import sys
from time import time
from datetime import timedelta


def add_time(mins=20):
    expiry_time = user_store.get('expiry_time')
    if not expiry_time:
        expiry_time = int(time())
    expiry_time = int(expiry_time) + mins * 60
    user_store.set('expiry_time', expiry_time)
    print "Time remaining: " + str(timedelta(seconds=(expiry_time - time())))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        add_time(int(sys.argv[1]))
    elif len(sys.argv) > 2:
        print("Usage: %s <time-in-minutes>")
        sys.exit(1)
    else:
        add_time()
