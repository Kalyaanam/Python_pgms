def function1(function):
    def wrapper():
        print("hello")
        function()
        print("welcome")
    return wrapper
def function2():
    print("all are")

function2=function1(function2)
function2()