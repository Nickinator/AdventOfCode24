import os

def read_input_file(day_dir, file_name="input.txt"):
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, day_dir, file_name)
    with open(file_path) as f:
        return f.read().splitlines()
