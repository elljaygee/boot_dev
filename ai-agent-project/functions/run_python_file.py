import os
import subprocess
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a specified python file relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to run, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="Optional arguments to pass to the Python file",
            )
        },
        required=["file_path"],
    ),
)

def run_python_file(working_directory, file_path, args=None):
    # get working directory absolute path
    working_dir_abs = os.path.abspath(working_directory)
    # construct the full path to the target directory
    target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
    # check if target_dir falls within the absolute path of working_dir - will be True or False
    valid_target_path = os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs
    is_file = os.path.isfile(target_path)

    if not valid_target_path:
        return (f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')

    if not is_file:
        return (f'Error: "{file_path}" does not exist or is not a regular file')
    
    if not file_path.endswith(".py"):
        return (f'Error: "{file_path}" is not a Python file')
    
    command = ["python", target_path]
    if args: command.extend(args)
    
    try:
        result = subprocess.run(
            command,                      # the ["python", target_path] list
            cwd=working_dir_abs,          # sets the working directory the script runs in
            capture_output=True,          # captures stdout and stderr instead of printing them
            text=True,                    # decodes output to strings instead of bytes
            timeout=30                    # raises an exception if it runs longer than 30 seconds
        )

        output = ""

        if result.returncode != 0:
            output += (f"Process exited with code {result.returncode}")

        if not result.stdout and not result.stderr:
            output += ("No output produced")
        else:
            if result.stdout:
                output += (f"STDOUT: {result.stdout}")
            if result.stderr:
                output += (f"STDERR: {result.stderr}")

        return output
    
    except Exception as e:
        return f"Error: {e}"
