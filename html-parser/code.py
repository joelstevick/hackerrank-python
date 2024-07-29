# Assumes valid HTML

from enum import Enum

OTHERWISE = ''
class State(Enum):
    NULL = 1
    HAVE_OPEN_ANGLE = 2
    HAVE_EXCLAMATION = 3
    PARSE_COMMENT  = 4
    PARSE_TAG_NAME = 5
    PARSE_ATTRIBUTE_NAME = 6
    PARSE_TAG_CONTENT = 8
    IN_ATTRIBUTE_NAME = 9
    IN_ATTRIBUTE_VALUE = 10
    PARSE_ATTRIBUTE_ASSIGNMENT_OPERATOR = 11
    PARSE_ATTRIBUTE_VALUE = 12

   
DFA = {
    State.NULL: {
        '<': State.HAVE_OPEN_ANGLE,
    },
    State.HAVE_OPEN_ANGLE: {
        '!': State.PARSE_COMMENT,
        '/': State.NULL,
        OTHERWISE: State.PARSE_TAG_NAME
    },
    State.PARSE_COMMENT: {
        '!': State.HAVE_EXCLAMATION,
    },
    State.HAVE_EXCLAMATION: {
        '>': State.NULL,
        OTHERWISE: State.PARSE_COMMENT
    },
    State.PARSE_TAG_NAME: {
        '>': State.PARSE_TAG_CONTENT,
        ' ': State.PARSE_ATTRIBUTE_NAME
    },
    State.PARSE_TAG_CONTENT: {
        '<': State.HAVE_OPEN_ANGLE
    },
    State.PARSE_ATTRIBUTE_NAME: {
        '"': State.PARSE_ATTRIBUTE_ASSIGNMENT_OPERATOR
    },
    State.PARSE_ATTRIBUTE_ASSIGNMENT_OPERATOR: {
    },
}

# state transition handlers
def START_TAG_NAME_handler(char, context):
    
    context["tag_name"] += char

def START_TAG_NAME_handler(char, context):
    
    context["tag_name"] += char
    
def START_ATTRIBUTE_NAME_handler(char, context):
    context["attribute_name"] = ''

def START_ATTRIBUTE_VALUE_handler(char, context):
    context["attribute_value"] = ''

def START_TAG_CONTENT_handler(_, context):
    
    context["tags"].append({
        "name": context["tag_name"],
        "attributes": []
    })
    
    context["tag_name"] = ''

DFA_change_handlers = {
    State.PARSE_TAG_NAME: START_TAG_NAME_handler,
    State.PARSE_TAG_CONTENT: START_TAG_CONTENT_handler,
    State.PARSE_ATTRIBUTE_NAME: START_ATTRIBUTE_NAME_handler,
    State.PARSE_ATTRIBUTE_VALUE: START_ATTRIBUTE_VALUE_handler
}

DFA_steady_state_handlers = {
    State.PARSE_TAG_NAME: START_TAG_NAME_handler,
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
        "tag_name": '',
        "attribute_name": '',
    }
    
    html_parse(html, context)
    