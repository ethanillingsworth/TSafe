

def type_safe(func):
    """
    Wrapper function to force a function to be type safe
    """

    def force_safety(*args, **kwargs):
        flag = True
        for argType in [args, kwargs.values()]:
            for index in range(0, len(argType)):
                arg = args[index]
                reqType = list(func.__annotations__.values())[index]
                
                if type(arg) == reqType or reqType == object:
                    return
                else:
                    flag = False
                    raise Exception(f"argument {arg} is not type of {reqType}")
                    break
        
        if flag:
            func(*args, **kwargs)

    return force_safety

safe = type_safe

