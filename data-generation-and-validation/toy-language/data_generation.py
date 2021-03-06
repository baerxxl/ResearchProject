import random
import argparse
import os

class ProgramGen:
    def __init__(self, _seed):
        self.params = {
            "variables": ["v1", "v2", "v3", "v4"],
            "numbers": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
            "expressions": ["<", "<=", ">", ">=", "==", "!="],
            "operators": ["+", "-", "*", "/"]
        }
        self.tpl = {
            "while": ('while( {exprhelper} ){{\n    {code}\n}}\n'),
            "if": ('if( {exprhelper} ){{\n    {code}\n}}\n'),
            "declaration": ('{var} = {declhelper};\n')
        }
        self.helper = {
            "expr": ('{var} {expr} {varnr}'),
            "decl": ('{varnr} {operator} {varnr2}')
        }
        self.end = ('return {};')
        random.seed(_seed)

    def generateHelper(self, _batchsize=100):  # creates 100 combinations of expr. and decl.
        declarations = []
        expressions = []
        varnr = self.params["variables"] + self.params["numbers"]
        operators = self.params["operators"]
        for i in range(_batchsize):
            rnd = int(round(random.uniform(0, 1)))
            if rnd == 0:  # extend declaration with operator and number/var
                declarations.append(self.helper["decl"].format(varnr=random.choice(varnr),
                                                               operator=random.choice(operators),
                                                               varnr2=random.choice(varnr)))
            else:
                declarations.append(self.helper["decl"].format(varnr=random.choice(varnr), operator='', varnr2='').strip())

        for i in range(_batchsize):
            expressions.append(self.helper["expr"].format(var=random.choice(self.params["variables"]),
                                                          expr=random.choice(self.params["expressions"]),
                                                          varnr=random.choice(varnr)))

        return expressions, declarations

    def createRndProgramm(self, _count=50, _loc=10):
        expression, declarations = self.generateHelper()
        programms = []
        for i in range(_count):
            lines = ""
            rLinesOfDeclaration = int(round(random.uniform(2, 6)))
            for j in range(rLinesOfDeclaration):
                lines += self.tpl["declaration"].format(var=random.choice(self.params["variables"]),
                                                        declhelper=random.choice(declarations))
            for j in range(_loc):
                element = random.choice(list(self.tpl.keys()))
                rnd = int(round(random.uniform(0, 1)))
                if element == "while" or element == "if":
                    if rnd == 0:
                        lines += self.tpl[element].format(exprhelper=random.choice(expression),
                                                          code=random.choice(self.params["variables"]) + " = " +
                                                          random.choice(declarations) + ";")
                    else:
                        lines += self.tpl[element].format(exprhelper=random.choice(expression),
                                                          code=(random.choice(self.params["variables"]) + " = " +
                                                                random.choice(declarations) + ";\n    " +
                                                                random.choice(self.params["variables"]) + " = " +
                                                                random.choice(declarations) + ";"))
                else:
                    lines += self.tpl[element].format(var=random.choice(self.params["variables"]),
                                                      declhelper=random.choice(declarations))
            programms.append(lines + self.end.format("true"))
        return programms

    def isValidCode(self, _code=''):
        vars = []
        lines = _code.splitlines()
        for line in lines:
            for var in self.params["variables"]:
                if (var + " = " in line):  # init found
                    if (var not in vars):
                        vars.append(var)
                        if (var in line.split(" = ")[1]):
                                # var used on the right side, without being declared
                            return False
            for var in self.params["variables"]:
                if (var in line):
                    if (var not in vars):
                        return False
        return True



def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--valid', required=True,
                        help='number of valid programs')
    parser.add_argument('--invalid', required=True,
                        help='number of invalid programs')
    parser.add_argument('--out', required=True,
                        help='outputfolder for generated programs')
    parser.add_argument('--seed', required=False,
                        help='outputfolder for generated programs')
    return parser.parse_args()

def main():
    args=get_args()

    nrOfValidPrograms = int(args.valid)
    nrOfInvalidPrograms = int(args.invalid)
    seed = int(args.seed) if args.seed is not None else None
    countOfValidPrograms = 0
    countOfInvalidPrograms = 0

    if not os.path.isdir(args.out+"/valid"):
        os.makedirs(args.out+"/valid")
    if not os.path.isdir(args.out+"/invalid"):
        os.makedirs(args.out+"/invalid")

    while (countOfValidPrograms < nrOfValidPrograms or countOfInvalidPrograms < nrOfInvalidPrograms):
        tmp = ProgramGen(seed)
        myProgram = tmp.createRndProgramm(100, 15)
        for item in myProgram:
            if tmp.isValidCode(item):
                countOfValidPrograms += 1
                if countOfValidPrograms <= nrOfValidPrograms:
                    tmpfile = open(args.out+"/valid/" + str(countOfValidPrograms) + ".txt", 'w')
                    tmpfile.write("%s\n" % item)
            else:
                countOfInvalidPrograms += 1
                if countOfInvalidPrograms <= nrOfInvalidPrograms:
                    tmpfile = open(args.out+"/invalid/" + str(countOfInvalidPrograms) + ".txt", 'w')
                    tmpfile.write("%s\n" % item)


if __name__ == '__main__':
    main()
