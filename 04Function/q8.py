# Problem: Create a function that accepts any number of keyword arguments and prints them in the format
# key: ValUe.

def key_value(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")

key_value(title="Islam",name="Panda")
key_value(title="Islam",name="Panda",village="kustore")