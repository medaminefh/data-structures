def pretty(fun):
    def inner():
        print("This will get printed when we use the pretty fun")
        fun()
    return inner

@pretty
def that():
    print("print that /")

@pretty
def this():
    print("print this ...")