class DFA:
    current_state = None
    token_value=""

    def __init__(self, states, alphabet, transition_function, start_state, accept_states, retracting_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states
        self.current_state = start_state
        self.retracting_states = retracting_states
        return

    def transition_to_state_with_input(self, input_value):
        if ((self.current_state, input_value) not in self.transition_function.keys()):
            self.current_state = None
            return
        self.current_state = self.transition_function[(self.current_state, input_value)]
        return

    def in_accept_state(self):
        if self.current_state in self.accept_states:
            return self.token_value, self.current_state
        else:
            return self.token_value,self.current_state

    def go_to_initial_state(self):
        self.current_state = self.start_state
        return

    def run_with_input_list(self, input_list):
        self.go_to_initial_state()
        for inp in input_list:
            self.transition_to_state_with_input(inp)
            if self.current_state not in self.retracting_states:
                self.token_value = self.token_value + inp
            if self.current_state in self.accept_states:
                break
        return self.in_accept_state()

    pass

    def validity(self,input_list):   #checking whether the input string is valid
        for a in input_list:
            if a in self.alphabet:
                continue
            else:
                print("Invalid String")
                return 0
        return 1

