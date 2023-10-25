import datetime

functionCalls = []

def logger(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            result = f"Error: {str(e)}"
        endTime = datetime.datetime.now()
        callInfo = {
            'timestamp': endTime,
            'function_name': func.__name__,
            'args': args,
            'result': result
        }
        functionCalls.append(callInfo)
        return result
    return wrapper

def getLogs():
    for callInfo in functionCalls:
        yield callInfo

@logger
def multiply(a, b):
    return a * b

multiply(3, 4)
multiply(5, 6)
multiply(14, 56)

log = getLogs()

print(next(log))
print(next(log))
print(next(log))
