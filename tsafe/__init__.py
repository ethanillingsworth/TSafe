from inspect import signature

class StringList():
    REQTYPE = str
    def __init__(self):
        return

class IntList():
    REQTYPE = int
    def __init__(self):
        return

class FloatList():
    REQTYPE = float
    def __init__(self):
        return

class ComplexList():
    REQTYPE = complex
    def __init__(self):
        return

class BoolList():
    REQTYPE = float
    def __init__(self):
        return

def type_safe(func):
    """
    Wrapper function to force a function to be type safe
    """
    def force_safety(*args, **kwargs):
        flag = True
        classCheck = False
        for argType in [args, kwargs.values()]:
            for index in range(0, len(argType)):
                arg = argType[index]

                if classCheck:
                    reqType = list(func.__annotations__.values())[index - 1]
                else:
                    reqType = list(func.__annotations__.values())[index]


                # skip self if in class
                if func.__qualname__ and 'self' in signature(func).parameters and not classCheck:
                    classCheck = True
                    continue
                    
                listTypes = [StringList, IntList, FloatList, ComplexList, BoolList]

                if type(arg) == reqType or reqType == object:
                    continue
                else:
                    flag = False
                    

                for l in listTypes:
                    
                    if (reqType == l and all(type(x) == l.REQTYPE for x in arg)) or reqType == list:
                        flag = True
                        break
                    else:
                        flag = False
                

                if not flag:
                    raise Exception(f"argument {arg} is not type of {reqType}")
                    break

        if flag:
            return func(*args, **kwargs)

    return force_safety

safe = type_safe

class Hello():
    @safe
    def __init__(self, x: int):
        print(x)

    @safe
    def hello(self, b: StringList, c: bool=True):
        print(1)

Hello(10).hello(["world"], False)