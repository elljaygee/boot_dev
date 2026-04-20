def new_resizer(max_width, max_height):
    
    def min_func(min_width=0, min_height=0):
        if (min_width > max_width) or (min_height > max_height):
            raise Exception ("minimum size cannot exceed maximum size")

        def width_func(width, height):
            new_width = min(max(width, min_width), max_width)
            new_height = min(max(height, min_height), max_height)
            return new_width, new_height

        return width_func

    return min_func
    