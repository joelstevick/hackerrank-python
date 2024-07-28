# Assumes valid HTML

from enum import Enum

OTHERWISE = ''
class State(Enum):
    NULL = 1
    HAVE_OPEN_ANGLE = 2
    HAVE_EXCLAMATION = 3
    IN_COMMENT  = 4
    IN_TAG_NAME = 5
    IN_TAG_CONTENT = 6
    IN_ATTRIBUTE_KEY = 7
    IN_ATTRIBUTE_VALUE = 8
    
   
DFA = {
    State.NULL: {
        '<': State.HAVE_OPEN_ANGLE,
    },
    State.HAVE_OPEN_ANGLE: {
        '!': State.IN_COMMENT,
        '/': State.NULL,
        OTHERWISE: State.IN_TAG_NAME
    },
    State.HAVE_EXCLAMATION: {
        '>': State.NULL,
        OTHERWISE: State.IN_COMMENT
    },
    State.IN_COMMENT: {
        '!': State.HAVE_EXCLAMATION,
    },
    State.HAVE_EXCLAMATION: {
        '>': State.NULL,
        OTHERWISE: State.IN_COMMENT
    },
    State.IN_TAG_NAME: {
        '>': State.IN_TAG_CONTENT
    },
    State.IN_TAG_CONTENT: {
        '<': State.HAVE_OPEN_ANGLE
    }
}
state = State.NULL

def transition(char):
    global state
    
    print(f"{state}: checking: {char}")
    if char in DFA[state]:
        newState = DFA[state][char]
    
        if newState:
            print(f"{state} => {newState}")
        
            state = newState
    
def html_parse():
    # read the html
    html = []

    N = int(input("Enter number of lines: "))

    for _ in range(N):
        line = input()
        html.append(line)
 
    
    # traverse the string
    for char in "".join(html):
        transition(char)

if __name__ == '__main__':
    html_parse()