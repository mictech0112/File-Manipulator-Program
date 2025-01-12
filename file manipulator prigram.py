import sys

def read_contents(pathname):
    with open(pathname) as f:
        return f.read()

def reverse_contents(input_path, output_path):
    with open(output_path, 'w') as f:
        f.write(read_contents(input_path)[::-1])

def copy_contents(input_path, output_path):
    with open(output_path, 'w') as f:
        f.write(read_contents(input_path))

def duplicate_contents(input_path, output_path, n):
    with open(output_path, 'w') as f:
        f.write(read_contents(input_path) * n)

def replace_string(input_path, output_path, needle, newstring):
    with open(output_path, 'w') as f:
        f.write(read_contents(input_path).replace(needle, newstring))

if __name__ == "__main__":
    commands = {
        'reverse': reverse_contents,
        'copy': copy_contents,
        'duplicate-contents': duplicate_contents,
        'replace-string': replace_string
    }

    if len(sys.argv) < 4:
        print("Error: Invalid number of arguments")
        sys.exit(1)

    command_name, input_path, output_path = sys.argv[1:4]
    extra_args = sys.argv[4:]

    if command_name not in commands:
        print("Error: Invalid command")
        sys.exit(1)

    if len(sys.argv) != len(commands[command_name].__code__.co_varnames):
        print("Error: Invalid number of arguments for the command")
        sys.exit(1)

    commands[command_name](input_path, output_path, *extra_args)
