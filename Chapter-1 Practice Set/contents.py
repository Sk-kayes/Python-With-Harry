import os

def print_directory_contents(path="."):
    try:
        for item in os.listdir(path):
            print(item)
    except Exception as e:
        print(f"Error: {e}")

# Specify the directory path (default is current directory)
print_directory_contents()
