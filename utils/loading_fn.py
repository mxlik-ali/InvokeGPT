import time
from rich.console import Console


def animation(text):
    console = Console()
    for i in range(1, 5):  # Change the range to control the number of dots
        console.print(f'[green]{text}[/green]' + "." * i, end='\r', style='bright_white')
        time.sleep(1)  # Adjust the speed of the animation here
    console.print(' ' * (len(text) + 4), end='\r')  # Clear the line
