# Assumes valid HTML

from enum import Enum

OTHERWISE = ''
class State(Enum):
    NULL = 1
    HAVE_OPEN_ANGLE = 2
    HAVE_COMMENT_TERMINATOR_1 = 3
    PARSE_COMMENT  = 4
    PARSE_TAG_NAME = 5
    PARSE_ATTRIBUTE_NAME = 6
    PARSE_TAG_CONTENT = 8
    IN_ATTRIBUTE_NAME = 9
    IN_ATTRIBUTE_VALUE = 10
    PARSE_ATTRIBUTE_VALUE = 12
    ADD_ATTRIBUTE = 13
    PARSE_ATTRIBUTE_ASSIGNMENT = 14
    PARSE_ATTRIBUTE_VALUE_QUOTE = 15
    HAVE_COMMENT_TERMINATOR_2 = 16
    ADD_SELF_TERMINATING_TAG = 17

# DFA   
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
        '-': State.HAVE_COMMENT_TERMINATOR_1,
    },
    State.HAVE_COMMENT_TERMINATOR_1: {
        '-': State.HAVE_COMMENT_TERMINATOR_2,
        OTHERWISE: State.PARSE_COMMENT
    },
    State.HAVE_COMMENT_TERMINATOR_2: {
        '>': State.NULL,
        OTHERWISE: State.PARSE_COMMENT
    },
    State.PARSE_TAG_NAME: {
        '>': State.PARSE_TAG_CONTENT,
        '/': State.ADD_SELF_TERMINATING_TAG,
        ' ': State.PARSE_ATTRIBUTE_NAME
    },
    State.PARSE_TAG_CONTENT: {
        '<': State.HAVE_OPEN_ANGLE
    },
    State.PARSE_ATTRIBUTE_NAME: {
        '=': State.PARSE_ATTRIBUTE_ASSIGNMENT
    },
    State.PARSE_ATTRIBUTE_ASSIGNMENT: {
        '"': State.PARSE_ATTRIBUTE_VALUE_QUOTE
    },
    State.PARSE_ATTRIBUTE_VALUE_QUOTE: {
        OTHERWISE: State.PARSE_ATTRIBUTE_VALUE  
    },
    State.PARSE_ATTRIBUTE_VALUE: {
        '"': State.ADD_ATTRIBUTE
    },
    State.ADD_ATTRIBUTE: {
        
    },
    State.ADD_SELF_TERMINATING_TAG: {
        '>': State.NULL
    }
}

# state transition handlers
def PARSE_TAG_NAME_handler(char, context):
    context["tag_name"] += char

def COLLECT_TAG_NAME_handler(char, context):   
    context["tag_name"] += char
    
def PARSE_ATTRIBUTE_NAME_handler(char, context):
    context["attribute_name"] = ''
    
def COLLECT_ATTRIBUTE_NAME_handler(char, context):
    context["attribute_name"] += char
    
def PARSE_ATTRIBUTE_VALUE_handler(char, context):
    context["attribute_value"] = char

def COLLECT_ATTRIBUTE_VALUE_handler(char, context):
    context["attribute_value"] += char
    
def ADD_TAG_handler(_, context):
  
    context["tags"].append({
        "name": context["tag_name"],
        "attributes": context["attributes"]
    })
    
    context["tag_name"] = ''

def ADD_ATTRIBUTE_handler(_, context):
    attribute = {}
    attribute["name"]=context["attribute_name"]
    attribute["value"]=context["attribute_value"]
    
    context["attribute_name"] = ""
    context["attribute_value"] = ""
       
    context["attributes"].append(attribute)
    
    context["state"] = State.PARSE_TAG_NAME
    

DFA_change_handlers = {
    State.PARSE_TAG_NAME: PARSE_TAG_NAME_handler,
    State.PARSE_TAG_CONTENT: ADD_TAG_handler,
    State.ADD_SELF_TERMINATING_TAG: ADD_TAG_handler,
    State.PARSE_ATTRIBUTE_NAME: PARSE_ATTRIBUTE_NAME_handler,
    State.PARSE_ATTRIBUTE_VALUE: PARSE_ATTRIBUTE_VALUE_handler,
    State.ADD_ATTRIBUTE: ADD_ATTRIBUTE_handler
}

DFA_steady_state_handlers = {
    State.PARSE_TAG_NAME: COLLECT_TAG_NAME_handler,
    State.PARSE_ATTRIBUTE_NAME: COLLECT_ATTRIBUTE_NAME_handler,
    State.PARSE_ATTRIBUTE_VALUE: COLLECT_ATTRIBUTE_VALUE_handler,

}
# do state transition
def transition(char, context):
      
    new_state = None
    
    if char in DFA[context["state"]]:
        new_state = DFA[context["state"]][char]
    
    else:
        if OTHERWISE in DFA[context["state"]]:
            new_state = DFA[context["state"]][OTHERWISE]
    
    # print(f"{context['state']} => {new_state}, char='{char}'")

    if new_state:   

        context["state"] = new_state

        if new_state in DFA_change_handlers:
            DFA_change_handlers[new_state](char, context)
        
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
        "attribute_value": '',
        "attributes": []
    }
    
    html_parse(html, context)
    