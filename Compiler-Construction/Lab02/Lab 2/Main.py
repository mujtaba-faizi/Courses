import Lexer

def strip_comments(line):
    if "/*" in line:
        index1 = line.find("/*")
        index2 = line.find("*/")
        line1 = line[0:index1]
        if len(line[index2:]) > 2:
            line2 = line[index2 + 2:]
            line = line1 + line2
            return line
        else:
            return line1
    elif "//" in line:
        index = line.find("//")
        line=line[0:index]
    return line


token_dict=dict()

with open('program.c', 'r') as f:
    for line in f:
        line = strip_comments(line)    # to remove comments
        line = line.rstrip()    # to remove blank lines
        if line:
            print("\nCODE LINE:-\n", line,"\n")
            print("TOKENS FOUND:-")
            Lexer.get_token(line)




