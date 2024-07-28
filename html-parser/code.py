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

def INSIDE_TAG_NAME_handler(char, context):
    
    context["tag_name"] += char
    
def START_TAG_NAME_handler(char, context):
    
    context["tag_name"] += char
    
def START_TAG_CONTENT_handler(_, context):
    
    context["tags"].append({
        "name": context["tag_name"],
        "attributes": []
    })
    
    context["tag_name"] = ''

DFA_change_handlers = {
    State.IN_TAG_NAME: START_TAG_NAME_handler,
    State.IN_TAG_CONTENT: START_TAG_CONTENT_handler
}

DFA_steady_state_handlers = {
    State.IN_TAG_NAME: INSIDE_TAG_NAME_handler,
}
# do state transition
def transition(char, context):
    
    new_state = None
    
    if char in DFA[context["state"]]:
        new_state = DFA[context["state"]][char]
    
    else:
        if OTHERWISE in DFA[context["state"]]:
            new_state = DFA[context["state"]][OTHERWISE]
    
    if new_state:   
        if new_state in DFA_change_handlers:
            DFA_change_handlers[new_state](char, context)
        
        context["state"] = new_state
    elif context["state"] in DFA_steady_state_handlers:
            DFA_steady_state_handlers[context["state"]](char, context)
        
    
def html_parse(html, context):
    
    # traverse the string
    for char in "".join(html):
        transition(char, context)
        
    return context
                    
def get_input():
    # read the html
    html = []

    N = int(input("Enter number of lines: "))

    for _ in range(N):
        line = input()
        html.append(line)
        
    return "".join(html)
 

if __name__ == '__main__':
    html = get_input()
    
    context = {
        "state": State.NULL,
        "tags": [],
        "tag_name": ''
    }
    
    html_parse(html, context)
    