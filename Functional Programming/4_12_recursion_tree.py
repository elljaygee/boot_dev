def list_files(parent_directory, current_filepath=""):
    files_list = []
    for key, value in parent_directory.items():
        new_file_path = current_filepath + "/" + key
        if value == None:
            files_list.append(new_file_path)
        else:
            files_list.extend(list_files(value, new_file_path))

    return files_list

"""
bootdev solution:

def list_files(parent_directory, current_filepath=""):
    file_list = []
    for key in parent_directory:
        new_filepath = current_filepath + "/" + key
        val = parent_directory[key]
        if val is None:
            file_list.append(new_filepath)
        else:
            file_list.extend(list_files(val, new_filepath))
    return file_list

"""