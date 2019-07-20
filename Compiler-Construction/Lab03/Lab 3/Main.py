import Lexer

token_name=[]
token_value=[]
hash_value=[]

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

def Show_SymbolTable():
    print("TOKEN NAME","           ","TOKEN VALUE","           ","HASH VALUE")
    for a in range(len(token_name)):
        space1 = " "
        space2 = " "
        length1=len(token_name[a])
        length2=len(token_value[a])
        for b in range(0,21-length1):
            space1=space1+" "
        for b in range(0,24-length2):
            space2=space2+" "
        print(token_name[a],space1,token_value[a],space2,hash_value[a])

def find(a):
    for b in range(0, a):
        if (token_value[a] == token_value[b]):
            return hash_value[b]

def read_file(file):
    with open(file, 'r') as f:
        for line in f:
            line = strip_comments(line)    # to remove comments
            line = line.rstrip()    # to remove blank lines
            if line:
                name, value = Lexer.get_token(line)
                token_name.extend(name)
                token_value.extend(value)

def add_hash(count):
    for a in range(len(token_name)):  # for assigning hash values
        sub = token_value[0:a]
        if token_value[a] in sub:
            hash_value.append(find(a))
        else:
            hash_value.append(count)
            count += 1

read_file('program.c')
add_hash(0)    # to save hash values in a list (starting from 0)
Show_SymbolTable()    # print on screen






