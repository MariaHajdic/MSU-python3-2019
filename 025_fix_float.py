def fix(prec):
    def func(f):
        def newFunc(*args, **kwargs):
            newArgs = []
            for arg in args:
                if isinstance(arg, float):
                    newArgs.append(round(arg, prec))
            for k, v in kwargs.items():
                if isinstance(v, float):
                    kwargs[k] = round(v, prec)
            return round(f(*newArgs, **kwargs), prec)
        return newFunc
    return func

lines = []
try:
    while True:
        lines.append(input())
except EOFError:
    pass

exec("\n".join(lines))
