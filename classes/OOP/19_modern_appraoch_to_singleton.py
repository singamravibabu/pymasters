def singleton(cls):
    instances = {}
    
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class SingletonClass:
    pass

# Testing Singleton
obj1 = SingletonClass()
obj2 = SingletonClass()

print(obj1 is obj2) # Output: True