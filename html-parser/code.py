# Enter your code here. Read input from STDIN. Print output to STDOUT

from enum import Enum

class State(Enum):
    INIT = 1
    HAVE_OPEN_ANGLE = 2
    HAVE_EXCLAMATION = 2
    IN_COMMENT  = 3
    IN_TAG_NAME = 4
    IN_TAG_CONTENT = 4
    IN_ATTRIBUTE_KEY = 5
    IN_ATTRIBUTE_VALUE = 5
    
   
DFA = {
    State.INIT: {
        '<': State.HAVE_OPEN_ANGLE,
    },
    State.HAVE_OPEN_ANGLE: {
        '!': State.IN_COMMENT,
        '*': State.IN_TAG
    },
    State.IN_COMMENT: {
        '!': State.HAVE_EXCLAMATION,
    },
    State.HAVE_EXCLAMATION: {
        '>': State.INIT,
        '*': State.IN_COMMENT
    }
}
def html_parse():
    # read the html
    html = []

    N = int(input())

    for _ in range(N):
        line = input()
        html.append(line)
 
    
        
    

if __name__ == '__main__':
    html_parse()