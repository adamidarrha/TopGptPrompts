import os
import sys

def create_directory_with_files(dir_name):
    # Create the directory with the specified name
    try:
        os.mkdir(dir_name)
    except FileExistsError:
        print(f"Directory '{dir_name}' already exists.")

    # Paths for the files to be created
    prompt_md_path = os.path.join(dir_name, "Prompt.md")
    readme_md_path = os.path.join(dir_name, "README.md")

    # Create and write to Prompt.md
    with open(prompt_md_path, 'w') as file:
        file.write("# Prompt ")

    # Create and write to README.md
    with open(readme_md_path, 'w') as file:
        file.write("# README")

    return f"Directory '{dir_name}' created with files Prompt.md and README.md."

def main():

    if(len(sys.argv) != 2):
        print("Usage: python createDirectory.py <directory name>")
        sys.exit(1)

    # Get the directory name from the command line
    directory_name = sys.argv[1]

    # Get the a directory up from this file
    root_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

    # Create the full path for the new directory
    full_dir_path = os.path.join(root_dir, directory_name)

    create_directory_with_files(full_dir_path)

if __name__ == "__main__":
    main()