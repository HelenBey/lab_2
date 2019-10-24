def print_result(func):
    def wrapper(*args):
        print(func.__name__)
        data = func(*args)
        if isinstance(data, list):
            [print(i) for i in data]
        elif isinstance(data, dict):
            for i in data:
                [print(i, '=', data[i]) for i in data]
        else:
            print(data)
        return data
    return wrapper
