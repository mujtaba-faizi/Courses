import DFA as nfa   # we'll be using the dfa class as our nfa (since we wont be requiring all states to be using all alphabets
# for transition)

reserved=[ 'break', 'case', 'char', 'const', 'continue', 'default', 'double', 'else', 'enum', 'extern', 'float',
'for', 'goto', 'if', 'int', 'long', 'return', 'short', 'static', 'struct', 'switch', 'void', 'while', 'printf', 'scanf' ]
letter = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digit="0123456789"
arithmetric_op=[ '+' , '-' ,'*', '/' , '%' ,'++' , '--']
punctuators=['{','}' , '(',')' , '[',']',  '=' , ','  ,'.' , ';' , ':']
relational_op=[ '==' , '!',   '>'  , '<' , '>=' , '<=' ]

def if_reserved(a):
    if a in reserved:
        return 1
    else:
        return 0

def get_token(string):
    token_name=[]
    token_value=[]
    while(len(string)>0):
        token, accept_state= transition_diagram(string)
        if token=="Omitted":
            string = string[1:]
            continue
        length=len(token)
        string=string[length:]
        if accept_state==2 or accept_state==1:
            if if_reserved(token)==1:
                token_name.append("RESERVED")
            else:
                token_name.append("ID")
        elif accept_state==5 or accept_state==6 or accept_state==4:
            token_name.append("INT_CONST")
        elif accept_state==9 or accept_state==10 or accept_state==8:
            token_name.append("FLOAT_CONST")
        elif accept_state==13 or accept_state==16:
            token_name.append("ASSIGN_OP")
        elif accept_state==14 or accept_state==20 or accept_state==17 or accept_state==18 or accept_state==19 or accept_state==12 or accept_state==15:
            token_name.append("OP")
        elif accept_state==23 or accept_state==25 or accept_state==27 or accept_state==29 or accept_state==30 or accept_state==31 or accept_state==24 or accept_state==26:
            token_name.append("REL_OP")
        elif accept_state==33 or accept_state==34 or accept_state==35 or accept_state==36 or accept_state==37 or accept_state==38 or accept_state==39 or accept_state==40 or accept_state==41 or accept_state==42 or accept_state==43:
            token_name.append("PUNC")
        token_value.append(token)
    return token_name,token_value

def transition_diagram(string):
    retracting_states=[]
    alphabet = []
    tf = dict()  # for defining the transition rules
    if string[0] in letter:   # dfa for keywords and identifiers
        start_state=0
        states = {0, 1, 2}
        accept_states = {2}
        retracting_states={2}
        other = "~`!@#$%^&*()_-+=|\}][{<>,.?/;:' "
        for a in range(52):
            alphabet.extend(letter[a])
            tf[(0, letter[a])] = 1
            tf[(1, letter[a])] = 1
        for a in range(10):
            alphabet.extend(digit[a])
            tf[(1, digit[a])] = 1
        for a in range(32):
            alphabet.extend(other[a])
            tf[(1, other[a])] = 2

    elif string[0] in digit:    # dfa for integers and floating point numbers
        start_state = 3
        states = {3,4,5,6,7,8,9,10}
        accept_states = {5,6,9,10}
        retracting_states={6,9}
        qualifier_int = "uUIL"
        qualifier_float = "fFIL"
        other_int = "abcdeghijklmnopqrstvwxyzABCDEGHJKMNOPQRSTVWXYZ~`!@#$%^&*()_-+=|\}][{<>,?/;:' "   # correct by adding f, F
        other_float = "abcdeghijklmnopqrstvwxyzABCDEGHJKMNOPQRSTVWXYZ~`!@#$%^&*()_-+=|\}][{<>,?/;:' "  # correct by adding u, U

        for a in range(10):
            alphabet.extend(digit[a])
            tf[(3, digit[a])] = 4
            tf[(4, digit[a])] = 4
            tf[(7, digit[a])] = 8
            tf[(8, digit[a])] = 8
        for a in range(77):
            alphabet.extend(other_int[a])
            tf[(4, other_int[a])] = 6
        for a in range(77):
            tf[(8, other_float[a])] = 9
        for a in range(4):
            alphabet.extend(qualifier_int[a])
            tf[(4, qualifier_int[a])] = 5
        for a in range(4):
            tf[(8, qualifier_float[a])] = 10
        alphabet.extend('.')
        alphabet.extend('f')
        alphabet.extend('F')
        tf[(4, '.')] = 7

    elif string[0] in arithmetric_op:  # dfa for arithmetric operators
        start_state = 11
        states = {11,12,13,14,15,16,17,18,19,20}
        accept_states = {20,16,13,14,17,19,18}
        retracting_states={14,20}
        other = letter+digit+"~`!@#$^&()_=|}][{<>,.?;:' "  #create seperate other_plus and other_minus
        alphabet.extend('+')
        alphabet.extend('-')
        alphabet.extend('/')
        alphabet.extend('%')
        alphabet.extend('*')

        for a in range(88):
            alphabet.extend(other[a])
            tf[(15, other[a])] = 20
            tf[(12, other[a])] = 14
        tf[(11, '+')] = 12
        tf[(12, '+')] = 13
        tf[(11, '-')] = 15
        tf[(15, '-')] = 16
        tf[(11, '/')] = 18
        tf[(11, '*')] = 17
        tf[(11, '%')] = 19

    elif string[0] in punctuators:  # dfa for punctuators
        if len(string)>1:
            if (string[0]+string[1]=="=="):    # for distinction in "=" & "=="
                return "==",23   # entering token value and accepting state manually just for "==" to avoid inconvinience with "="
        start_state = 32
        states = {32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43}
        accept_states = {33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43}
        alphabet = ['(', ')', '{', '}', '[', ']', ',', '=', '.', ';', ':']

        tf[(32, '(')] = 33
        tf[(32, ')')] = 34
        tf[(32, '[')] = 35
        tf[(32, ']')] = 36
        tf[(32, '{')] = 37
        tf[(32, '}')] = 38
        tf[(32, ',')] = 39
        tf[(32, '=')] = 40
        tf[(32, ';')] = 41
        tf[(32, ':')] = 42
        tf[(32, '.')] = 43

    elif string[0] in relational_op:   # dfa for relational operators
        start_state = 21
        states = {21,22,23,24,25,26,27,28,29,30,31}
        accept_states = {23,25,27,29,30,31}
        retracting_states={30,31}
        other = letter+digit+"~`-@#$^&()_+|}<>!][{/*%,.?;:' "
        alphabet=['!','=','<','>']

        for a in range(92):
            alphabet.extend(other[a])
            tf[(24, other[a])] = 30
            tf[(26, other[a])] = 31
        tf[(21, '=')] = 22
        tf[(22, '=')] = 23
        tf[(21, '>')] = 24
        tf[(24, '=')] = 25
        tf[(21, '<')] = 26
        tf[(26, '=')] = 27
        tf[(21, '!')] = 28
        tf[(28, '=')] = 29


    else:
        return "Omitted", "Omitted"
    d = nfa.DFA(states, alphabet, tf, start_state, accept_states,retracting_states)
    token, end_state=d.run_with_input_list(string)
    return token, end_state