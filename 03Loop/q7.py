#password

import time

user_pass="PASSWORD"

max_attem=5
attem=1
await_time=1

while attem < max_attem:
    password=input("Enter password: ")
    if password==user_pass:
        print("Successfully Login")
        break
    else:
        print("Try Again: ")
        time.sleep(await_time)
        await_time*=2


    

