

execution_commands = {
    'python': 'python {filename}',  # Replace {filename} with the actual file name
    'javascript': 'node {filename}',
    'java': 'javac {filename} && java {main_class}',  # Replace {filename} and {main_class} with actual names
    'c++': 'g++ {filename} -o {output} && ./{output}',  # Replace {filename} and {output} with actual names
    'ruby': 'ruby {filename}',
    'c#': 'csc {filename} && ./{output}',  # Replace {filename} and {output} with actual names
    'go': 'go run {filename}',
    'swift': 'swift {filename}',
    'kotlin': 'kotlinc {filename} -include-runtime -d {output}.jar && java -jar {output}.jar',  # Replace {filename} and {output} with actual names
    'typescript': 'tsc {filename} && node {output}.js',  # Replace {filename} and {output} with actual names
    'php': 'php {filename}',
    'rust': 'rustc {filename} && ./{output}',  # Replace {filename} and {output} with actual names
    'objective-c': 'clang -framework Foundation {filename} -o {output} && ./{output}',  # Replace {filename} and {output} with actual names
    'dart': 'dart {filename}',
    'bash': 'bash {filename}',  # or './{filename}' for executable scripts
    'perl': 'perl {filename}',
    'haskell': 'ghc -o {output} {filename} && ./{output}',  # Replace {filename} and {output} with actual names
    'lua': 'lua {filename}',
    'scala': 'scalac {filename} && scala {main_class}',  # Replace {filename} and {main_class} with actual names
    'r': 'Rscript {filename}',
    'julia': 'julia {filename}',
    'powershell': 'powershell {filename}',
    'elixir': 'elixir {filename}',
    'groovy': 'groovy {filename}',
    'objective-c++': 'clang++ -framework Foundation {filename} -o {output} && ./{output}',  # Replace {filename} and {output} with actual names
    'ada': 'gnatmake {filename} && ./{output}',  # Replace {filename} and {output} with actual names
    'clojure': 'clojure -M -m {main_class}',  # Replace {main_class} with actual name
    'erlang': 'erlc {filename} && erl -noshell -s {main_module} start -s init stop',  # Replace {filename} and {main_module} with actual names
    'f#': 'fsharpc {filename} && mono {output}.exe',  # Replace {filename} and {output} with actual names
    'matlab': 'matlab -r "run(\'{filename}\')"',
    'octave': 'octave {filename}',
    'd': 'dmd {filename} && ./{output}',  # Replace {filename} and {output} with actual names
    'cobol': 'cobc -x -o {output} {filename}',  # Replace {filename} and {output} with actual names
    'fortran': 'gfortran -o {output} {filename} && ./{output}',  # Replace {filename} and {output} with actual names
    'forth': 'gforth {filename}',
    'scheme': 'csi -script {filename}',
    'prolog': 'swipl -s {filename}',
    'smalltalk': 'gst {filename}',
    'coq': 'coqc {filename}',
    'verilog': 'iverilog -o {output} {filename} && vvp {output}',  # Replace {filename} and {output} with actual names
    'vhdl': 'ghdl -a {filename} && ghdl -e {module} && ghdl -r {module}',  # Replace {filename} and {module} with actual names
    'tcl': 'tclsh {filename}',
    'ocaml': 'ocamlc -o {output} {filename} && ./{output}',  # Replace {filename} and {output} with actual names
    'pl/i': 'pli {filename}',
    'haxe': 'haxe -main {main_class} --interp',  # Replace {main_class} with actual name
    'cobolscript': 'cobc -x -o {output} {filename}',  # Replace {filename} and {output} with actual names
    'racket': 'racket {filename}',
    'kornshell': 'ksh {filename}',
    'dart_flutter': 'flutter run',
    'powershell_core': 'pwsh {filename}',
    'ada_gnat': 'gnatmake {filename} && ./{output}',  # Replace {filename} and {output} with actual names
    'julia2': 'julia {filename}',
    'rust_cargo': 'cargo run'
}

# Usage example:
# Replace 'python' with the desired language key and '{filename}' with the actual file name.

