def func1(name):
    return f"hello{name}"

def func2(name):
    return f"{name}, how you doin?"

def func3(func4):
    return func4('dear student')

print(func3(func1))
print(func3(func2))