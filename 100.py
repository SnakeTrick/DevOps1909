import datetime
from mydep import test as mydep_test
from My_Other_dep import test
mydep_test()
test()

def wait_for_print():
    from time import sleep
    sleep(3)
    print("Hello World")

wait_for_print()
print(datetime.datetime.now())
import requests

