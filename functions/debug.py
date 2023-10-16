from functools import wraps
def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Running Function',func.__name__)
        print('positional arguments',args)
        print('keyword arguments',kwargs)
        result = func(*args, **kwargs)
        print('result',result)
        return result
    return wrapper
@debug
def main(name):
    return 'Hello '+name
main('Afzal')

