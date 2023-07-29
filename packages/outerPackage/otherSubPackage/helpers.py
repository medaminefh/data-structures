def pretty(func):
    def inner(a, b):
        a += b
        return func(a, b)
    
    return inner

@pretty
def first(a, b):
    print(f"a: {a}, b: {b}")


@pretty
def second(a, b):
    print(f"a: {a}, b: {b}")

