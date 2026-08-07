def replacer(old, new):
    
    def replace(decorated_func):

        def wrapper(text):
            new_string = text.replace(old, new)

            return decorated_func(new_string)

        return wrapper

    return replace


@replacer("&", "&amp;")
@replacer("<", "&lt;")
@replacer(">", "&gt;")
@replacer('"', "&quot;")
@replacer("'", "&#x27;")
def tag_pre(text):
    return f"<pre>{text}</pre>"