class Interpreter:
    def __init__(self, functions):
        self.variables = {}
        self.functions = functions

    def evaluate(self, expr):
        try:
            return eval(expr, {}, self.variables)
        except:
            return expr.strip('"')

    def run(self, lines):
        for line in lines:
            if line.startswith("degisken"):
                _, name, _, value = line.split(None, 3)
                self.variables[name] = self.evaluate(value)
            elif line.startswith("yaz"):
                expr = line[4:]
                print(self.evaluate(expr))
            elif "(" in line and ")" in line:
                fname = line.split("(")[0].strip()
                args = line.split("(", 1)[1].rsplit(")", 1)[0].split(",")
                args = [self.evaluate(arg.strip()) for arg in args]
                if fname in self.functions:
                    print(self.functions[fname](args))
