import sys
import os
import re
from utils.loading_fn import *
from utils.errorlog import *
from utils.extract_code import *
import api_config.api
from utils.file_reader import *
from utils.errorlog import *
from rich import print as printc

arg = sys.argv[1]
file_name = sys.argv[2]

def file_output(output):
  def gen_output(output):
    separator = "\n--------------------------------------------------------------------------------------------\n"
    with open('gpt.txt', 'a') as gpt:
        gpt.write(f"{output}, {separator}")

  animation_running = True
  animation_thread = Thread(target=animation, args=("Retrieving data from the server",))
  animation_thread.start()

  # Call your_function here
  gen_output(output)

  # Set the flag to stop the animation
  animation_running = False
  animation_thread.join()
  


def file_output1(output):
  with open (file_name,'w') as gpt:
    gpt.write(str(output))

def readme_creator(output):
  with open ('Readme.md','w') as gpt:
    gpt.write(output)

def custom(output):
  print(output)


def command(file_name):

  try:
    if arg == 'debug':
      x = read(file_name)      
      res = api_config.api.response('find the error in the code and provide corrected code{}'.format(x))
      file_output(res)
      code = extract(res,file_name)
      file_output1(code)
      printc("[green]The debugged code has been updated within the provided file as specified in the argument.[/green]")
      printc("[green]A comprehensive explanation of the code is available in the 'gpt.txt' file located in your current directory.[/green]")

    elif arg == 'refractor':
      x = read(file_name)
      res = api_config.api.response('refractor this code and tell me what did you change {}'.format(x))
      file_output(res)
      printc("[green]The refracted code has been updated within the provided file as specified in the argument.[/green]")
      printc("[green]A comprehensive explanation of the code is available in the 'gpt.txt' file located in your current directory.[/green]")

    elif arg == 'addtest':
      x = read(file_name)
      res = api_config.api.response('add test to the following code{}'.format(x))
      file_output(res)

    elif arg == 'customprompt':
      x = input()
      res = api_config.api.response(x)
      custom(res)

    elif arg == 'readme':
      x = readme()
      res = api_config.api.response('generate a readme.md {}'.format(x))
      readme_creator(res) 
      
    elif arg == 'error':
      x = error(file_name)
      res = api_config.api.response('solve the error in my terminal that has been occured {}'.format(x))
      file_output(res)

    else:
      raise ValueError
    
  except ValueError as ve:
    printc("[yellow]You entered an argument which is not defined[/yellow]")




command(file_name)

