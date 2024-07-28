# Enter your code here. Read input from STDIN. Print output to STDOUT

from enum import Enum

class Delimiter(Enum):
    TAG = 1
    QUOTE  = 2
    
delimiters = {
    Delimiter.TAG: ['<']
}
def html_parse():
    # read the html
    html = []

    N = int(input())

    for _ in range(N):
        line = input()
        html.append(line)
 
    print("".join(html))
            
        
    

if __name__ == '__main__':
    html_parse()