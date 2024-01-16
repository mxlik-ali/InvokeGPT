import os
import sys
from . import loading_fn
from rich import print as printc
from threading import Thread
def read(filename):
    filename = filename
    def file_read(filename):
        try:
            test = filename
            with open (test,'r') as f:
                f_content = f.read()
                if len(f_content) >0:
                    return f_content

                else :
                    printc("[red]No content to read from the file assigned as arg[/red]")
                    sys.exit(1)
    
        except Exception as e:
            printc(f"[red]Can't read the file content due to the following error: {e}. Please ensure the file exists in the current directory or check if it's within a subfolder.[/red]")
            sys.exit(1)

    animation_running = True
    animation_thread = Thread(target=loading_fn.animation, args=("Reading the file content",))
    animation_thread.start()

    # Call your_function here
    content = file_read(filename)

    # Set the flag to stop the animation
    animation_running = False
    animation_thread.join()
    return content


def readme():
    def documentation():
        try:
            curr_dir = os.getcwd()
            for dirpath, dirname, filename in os.walk(curr_dir):
                for file in filename:
                    filename = os.path.join(dirpath,file)
                    with open (filename,'r') as f:
                        f_content = f.read()
                        return(f_content)

        except Exception as e:
            printc("[red]An error occured while reading all the files[/red]")
            sys.exit(1)

    animation_running = True
    animation_thread = Thread(target=loading_fn.animation, args=("Reading the file content",))
    animation_thread.start()

    # Call your_function here
    content = documentation()

    # Set the flag to stop the animation
    animation_running = False
    animation_thread.join()
    return content    