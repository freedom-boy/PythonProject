def log(text):
    def decorator(func):
        def wrapper(*args,**kwargs):
            print '%s %s():' % (text,func.__name__)
            return func(*args,**kwargs)
        return wrapper
    return decorator

@log('execute')
def now():
    print '2013-11-25'

now()
