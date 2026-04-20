def configure_plugin_decorator(func):
    def wrapper(*args):
        d = dict(args)

        return func(**d)

    return wrapper

# *args collects tuple pairs
# dict(args) turns them into a dictionary
# func(**d) unpacks that dictionary into keyword arguments
# return wrapper makes the decorator replace the original function with the wrapper