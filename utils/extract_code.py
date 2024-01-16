import re
from . import errorlog

def extract (prompt, file_name):
    prompt = prompt
    lang = errorlog.get_file_type(file_name)
    escaped_lang = re.escape(lang)
    pattern = re.compile(rf'```{escaped_lang}(.*?)```', re.DOTALL)
    code_snippets = pattern.findall(prompt)

    combined_snippets = '\n'.join(code_snippets)
    return combined_snippets

