from parser import parse
from interpreter import Interpreter
from core.stdlib import AVAILABLE_FUNCTIONS

def run_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        code = f.read()
    lines = code.strip().split('\n')
    parsed_lines = parse(lines)
    interpreter = Interpreter(AVAILABLE_FUNCTIONS)
    interpreter.run(parsed_lines)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Kullanım: python main.py <dosya.simpli>")
    else:
        run_file(sys.argv[1])
