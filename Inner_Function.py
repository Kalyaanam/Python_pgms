def func():
    print("First Function")
    def func1():
        print("First Child Function")
    def func2():
        print("Second Child Function")
    func2()
    func1()
func()