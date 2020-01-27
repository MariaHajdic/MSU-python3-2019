def Stringer(cls):
    def wrap(fn):
        def func(*args, **kwargs):
            r = fn(*args, **kwargs)
            if type(r) is str:
                return DivStr(r)
            return r
        return func

    for key, val in str.__dict__.items():
        if callable(val):
            setattr(cls, key, wrap(val))
    return cls

@Stringer
class DivStr(str):
    def __truediv__(self, n):
        return self[: len(self) // n]
