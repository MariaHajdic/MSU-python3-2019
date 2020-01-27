def nonify(f):
    def wrapper(*args, **kwargs):
        if not f(*args, **kwargs):
            return None
        return f(*args, **kwargs)
    return wrapper
