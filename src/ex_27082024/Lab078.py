def outer_function():
    var1 = 30  # local int variable
    var2 = 20

    def inner_function():
        print(var1)

    def inner_function2():
        print(var1)
        print(var2)

    inner_function()
    inner_function2()

outer_function()