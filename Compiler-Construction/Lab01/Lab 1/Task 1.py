class DFA:
    current_state = None

    def __init__(self, states, alphabet, transition_function, start_state, accept_states):  #5-tupple
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states
        self.current_state = start_state
        return

    def transition_to_state_with_input(self, input_value):
        if ((self.current_state, input_value) not in self.transition_function.keys()):
            self.current_state = None
            return
        self.current_state = self.transition_function[(self.current_state, input_value)]
        return

    def in_accept_state(self):
        if self.current_state in accept_states:
            print("String Accepted")
        else:
            print("String Rejected")

    def go_to_initial_state(self):
        self.current_state = self.start_state
        return

    def run_with_input_list(self, input_list):
        self.go_to_initial_state()
        for inp in input_list:
            self.transition_to_state_with_input(inp)
            continue
        return self.in_accept_state()

    pass

    def validity(self,input_list):   #checking whether the input string is valid
        for a in input_list:
            if a in alphabet:
                continue
            else:
                print("Invalid String")
                return 0
        return 1

states = {0, 1, 2, 3, 4}
alphabet = {'a', 'b', 'c'}

tf = dict()   #defining the transition rules
tf[(0, 'a')] = 1
tf[(0, 'b')] = 4
tf[(0, 'c')] = 4
tf[(1, 'a')] = 4
tf[(1, 'b')] = 2
tf[(1, 'c')] = 4
tf[(2, 'a')] = 4
tf[(2, 'b')] = 1
tf[(2, 'c')] = 3
tf[(3, 'a')] = 4
tf[(3, 'b')] = 4
tf[(3, 'c')] = 4
tf[(4, 'a')] = 4
tf[(4, 'b')] = 4
tf[(4, 'c')] = 4

start_state = 0
accept_states = {3}

d = DFA(states, alphabet, tf, start_state, accept_states)

for a in range(1000):
    string = input("Enter the string (Enter 0 to exit) : ")
    if string=='0':
        exit()
    val=d.validity(string)
    if val==0:
        continue
    d.run_with_input_list(string)
