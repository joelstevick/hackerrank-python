# Assumes valid HTML

from enum import Enum

OTHERWISE = '***default***'
class State(Enum):
    CONTINUE_SCAN = 1
    HAVE_OPEN_ANGLE = 2
    HAVE_EXCLAMATION = 3
    IN_COMMENT  = 4
    IN_TAG_NAME = 5
    IN_TAG_CONTENT = 6
    IN_ATTRIBUTE_KEY = 7
    IN_ATTRIBUTE_VALUE = 8
    
   
DFA = {
    State.CONTINUE_SCAN: {
        '<': State.HAVE_OPEN_ANGLE,
    },
    State.HAVE_OPEN_ANGLE: {
        '!': State.IN_COMMENT,
        '/': State.CONTINUE_SCAN,
        OTHERWISE: State.IN_TAG_NAME
    },
    State.HAVE_EXCLAMATION: {
        '>': State.CONTINUE_SCAN,
        OTHERWISE: State.IN_COMMENT
    },
    State.IN_COMMENT: {
        '!': State.HAVE_EXCLAMATION,
    },
    State.HAVE_EXCLAMATION: {
        '>': State.CONTINUE_SCAN,
        OTHERWISE: State.IN_COMMENT
    },
    State.IN_TAG_NAME: {
        '>': State.IN_TAG_CONTENT
    },
    State.IN_TAG_CONTENT: {
        '<'
    }
}
def html_parse():
    # read the html
    html = []

    N = int(input("Enter number of lines: "))

    for _ in range(N):
        line = input()
        html.append(line)
 
    
        
    

if __name__ == '__main__':
    html_parse()