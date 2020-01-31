def conditional_decorator(dec, condition):
    #print(f"condition {condition} {type(condition)}")
    def decorator(func):
        #print(f"condition {condition} {type(int(condition))}")
        if int(condition) == 0:
            #print("Plain w/o dec")
            # Return the function unchanged, not decorated.
            return func
        #print("w/ dec")
        return dec(func)
    return decorator