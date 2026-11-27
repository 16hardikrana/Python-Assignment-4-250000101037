def show_local():
    message = "I am local to show_local()"
    print(message)

show_local()
try:
    print(message)
except NameError:
    print("Local variable is not accessible outside the function")
