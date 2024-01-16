import openai
import sys
from rich import print as printc
from threading import Thread
from utils import loading_fn

openai.api_key = "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"
openai.api_base = "http://localhost:1337"


def response (prompt):
  def chatgpt(prompt):
    try:
      chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        maxtoken = 100,
      )
      if isinstance(chat_completion, dict):
            # not stream
            return(chat_completion.choices[0].message.content)
      else:
          # stream
          for token in chat_completion:
              content = token["choices"][0]["delta"].get("content")
              if content != None:
                print(content, end="", flush=True)

    except Exception as e:
      printc(f"[red]An Error occured to connect to the server (server overload)[/red]")
      sys.exit(1)

  animation_running = True
  animation_thread = Thread(target=loading_fn.animation, args=("Connecting with the server",))
  animation_thread.start()

  # Call your_function here
  content = chatgpt(prompt)

  # Set the flag to stop the animation
  animation_running = False
  animation_thread.join()
  return content 


