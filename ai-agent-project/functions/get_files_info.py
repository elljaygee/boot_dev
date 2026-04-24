import os

def get_files_info(working_directory, directory="."):
    # get working directory absolute path
    working_dir_abs = os.path.abspath(working_directory)
    # construct the full path to the target directory
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
    # check if target_dir falls within the absolute path of working_dir - will be True or False
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
    is_dir = os.path.isdir(target_dir)

    if not valid_target_dir:
        return (f'Error: Cannot list "{directory}" as it is outside the permitted working directory')

    if not is_dir:
        return (f"Error: {directory} is not a directory")
        
    try:
        lines = []
        for entry in os.listdir(target_dir):
            full_path = os.path.join(target_dir, entry)
            is_entry_dir = os.path.isdir(full_path)
            file_size = os.path.getsize(full_path)
            lines.append(f"- {entry}: file_size={file_size} bytes, is_dir={is_entry_dir}")
        return "\n".join(lines)
    except Exception as e:
        return f"Error: {e}"
