import os

def write_file(working_directory, file_path, content):
    # get working directory absolute path
    working_dir_abs = os.path.abspath(working_directory)
    # construct the full path to the target directory
    target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
    # check if target_dir falls within the absolute path of working_dir - will be True or False
    valid_target_path = os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs
    is_dir = os.path.isdir(target_path)

    if not valid_target_path:
        return (f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')
    
    if is_dir:
        return (f'Error: Cannot write to "{file_path}" as it is a directory')
    
    os.makedirs(os.path.dirname(target_path), exist_ok=True)

    try:
        with open(target_path, "w") as f:
            f.write(content)
        
        return (f'Successfully wrote to "{file_path}" ({len(content)} characters written)')
    
    except Exception as e:
        return f"Error: {e}"