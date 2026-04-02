def my_validator(func):
    def my_wrapper(world):
        print(f"Entering {func.__name__} with {world} argument")
        if ("Pluto" == world):
            print("Pluto is not a planet!")
        else:
            return func(world)
    return my_wrapper

@my_validator
def my_func(planet):
    print(f"Hello, {planet}!")

my_func("World")
my_func("Pluto")