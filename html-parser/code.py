# Enter your code here. Read input from STDIN. Print output to STDOUT

from enum import Enum

class State(Enum):
    INIT = 1
    IN_COMMENT  = 2
    IN_TAG = 3
    IN_QUOTE = 4
   
def html_parse():
    # read the html
    html = []

    N = int(input())

    for _ in range(N):
        line = input()
        html.append(line)
 
    for char in "".join(html):
        print(char)             
        
    

if __name__ == '__main__':
    html_parse()