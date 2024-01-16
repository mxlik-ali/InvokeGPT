import subprocess
from threading import Thread
from rich import print as printc
from . import lang
from . import loading_fn

 
def get_file_type(filename):
    # Mapping of file extensions to programming languages
    file_extension_mapping = {
        'py': 'python',
        'js': 'javascript',
        'java': 'java',
        'cpp': 'c++',
        'rb': 'ruby',
        'cs': 'c#',
        'go': 'go',
        'swift': 'swift',
        'kt': 'kotlin',
        'ts': 'typescript',
        'php': 'php',
        'rs': 'rust',
        'm': 'objective-c',
        'dart': 'dart',
        'sh': 'bash',
        'pl': 'perl',
        'hs': 'haskell',
        'lua': 'lua',
        'scala': 'scala',
        'r': 'r',
        'jl': 'julia',
        'ps1': 'powershell',
        'exs': 'elixir',
        'groovy': 'groovy',
        'mm': 'objective-c++',
        'adb': 'ada',
        'clj': 'clojure',
        'erl': 'erlang',
        'fs': 'f#',
        'matlab': 'matlab',
        'm': 'octave',
        'd': 'd',
        'cob': 'cobol',
        'f': 'fortran',
        'fs': 'forth',
        'scm': 'scheme',
        'pl': 'prolog',
        'st': 'smalltalk',
        'v': 'coq',
        'v': 'verilog',
        'vhdl': 'vhdl',
        'tcl': 'tcl',
        'ml': 'ocaml',
        'pli': 'pl/i',
        'hx': 'haxe',
        'cbs': 'cobolscript',
        'rkt': 'racket',
        'ksh': 'kornshell',
        'dart_flutter': 'dart_flutter',
        'ps1': 'powershell_core',
        'ada_gnat': 'ada_gnat',
        'julia2': 'julia2',
        'rust_cargo': 'rust_cargo'
    }

    # Extract the file extension
    _, extension = filename.rsplit('.', 1)


    # Check if the extension is in the mapping
    if extension in file_extension_mapping:
        return file_extension_mapping[extension]
    else:
        raise ValueError("Unsupported file type")

# Usage example:
# file_type = get_file_type(arg1.file_name)
# print(file_type)

def error(file_name):
    def terminal_error():
        try:
            filetype = get_file_type(file_name)
            command = lang.execution_commands[filetype].format(filename = file_name)
            traceback = subprocess.run(command,stderr=subprocess.PIPE, text=True)
            if len(traceback.stderr) == 0:
                printc("[red]No error was detected while running the program[/red]")
                sys.exit(1)

            else:
                return traceback.stderr

        except Exception as e:
            printc(f"[red]Something went wrong[/red]\n {e}")

    animation_running = True
    animation_thread = Thread(target=loading_fn.animation, args=("Processing the error",))
    animation_thread.start()

  # Call your_function here
    traceback = terminal_error()

  # Set the flag to stop the animation
    animation_running = False
    animation_thread.join()
    return traceback

