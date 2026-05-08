import os

def get_file_content(working_directory, file_path):
    # get working directory absolute path
    working_dir_abs = os.path.abspath(working_directory)
    # construct the full path to the target directory
    target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
    # check if target_dir falls within the absolute path of working_dir - will be True or False
    valid_target_path = os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs
    is_file = os.path.isfile(target_path)

    if not valid_target_path:
        return (f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')

    if not is_file:
        return (f'Error: File not found or is not a regular file: "{target_path}"')
    
    MAX_CHARS = 10000

    try:
        with open(target_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)

        # After reading the first MAX_CHARS check the next char to see if it exists
        if f.read(1):
            file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            

    except Exception as e:
        return f"Error: {e}"