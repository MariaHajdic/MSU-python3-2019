def fcounter(*args):
    cl = args[0]

    cattr = list(filter(lambda x: not x.startswith("_"), dir(args[0])))
    cm = list(filter(lambda x: callable(getattr(cl, x)), cattr))
    cf = list(filter(lambda x: not callable(getattr(cl, x)), cattr))

    obj = cl(*args[1:])
    oattr = list(filter(lambda x: not x.startswith("_"), dir(obj)))
    om = list(filter(lambda x: callable(getattr(obj, x)) and x not in cm, oattr))
    of = list(filter(lambda x: not callable(getattr(obj, x)) and x not in cf, oattr))
    return cm, cf, om, of

lines = []
try:
    while True:
        lines.append(input())
except EOFError:
    pass

exec("\n".join(lines))
