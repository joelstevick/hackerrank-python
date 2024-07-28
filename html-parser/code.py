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

tags = []

tag_name = ''

def IN_TAG_NAME_handler(char):
    global tag_name
    
    tag_name += char
    
def IN_TAG_CONTENT_handler(char):
    tags.append({
        "name": tag_name,
        "attributes": []
    })
    
    tag_name = ''

DFA_Handlers = {
    State.IN_TAG_NAME: IN_TAG_NAME_handler,
    State.IN_TAG_CONTENT: IN_TAG_CONTENT_handler
}

def transition(char):
    global state
    
    new_state = state
    
    if char in DFA[state]:
        new_state = DFA[state][char]
    
    else:
        if OTHERWISE in DFA[state]:
            new_state = DFA[state][OTHERWISE]
        
    if new_state != state:
        print(f"{state} => {new_state}")
    
    if new_state in DFA_Handlers:
        DFA_Handlers[new_state](char)
        
        state = new_state
    
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
        
    print(f"tags = {tags}")

if __name__ == '__main__':
    html_parse()