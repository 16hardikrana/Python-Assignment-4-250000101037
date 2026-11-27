value = "global value"

def show_value():
    value = "local value"
    print("Inside function:", value)

show_value()
print("Outside function:", value)
