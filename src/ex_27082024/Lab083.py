import time


def time_decorator(func):
    def wrapper():
        start_time = time.time()
        print("This is start time: ", start_time)
        print("*********************")
        func()
        print("*********************")
        end_time = time.time()
        print("This is end time: ", end_time)
        print("*********************")
        print(f"Time take by function {end_time - start_time}")


    return wrapper()


@time_decorator
def test_ui_1():
    print("Add a function, time taken by this function")
    time.sleep(2) # wait for 2 seconds

print("********************")

@time_decorator
def test_ui_2():
    print("Add a function, time taken by this function")
    time.sleep(5)