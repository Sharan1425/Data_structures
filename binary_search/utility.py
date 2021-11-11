import time

def time_it(func):
    
    def wrapper(*args, **kwagrs):
        start = time.time()
        result = func(*args, **kwagrs)
        end = time.time()
        print(func.__name__ + " took " + str(( end-start ) * 1000) + " mil sec ")
        
        return result
    
    return wrapper