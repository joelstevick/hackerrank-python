vowels = {
           'A': True,
           'E': True,
           'I': True,
           'O': True,
           'U': True
}
stuart = 0
kevin = 0

COUNT = "@*c*@"

def is_vowel(string): 
    return vowels.get(string[0]) == True
    
root = {}

def add_node(char, parent):
    node = parent.get(char)
    if node == None:
        node = {
            COUNT : 1
        }
        parent[char] = node
    else:
        node[COUNT] += 1
    
    return node

        
def build_tree(string):
    global root
    global stuart
    global kevin

    for i in range(len(string)):
        parent = None
        for j in range(len(string) - i):
            char = string[i+j]
            
            if not parent:
                parent = add_node(char, root)
            else:
                parent = add_node(char, parent)

def traverse(char, parent):
    node = parent.get(char)
    count = node[COUNT]

    for _, char in enumerate(node.keys()):
        if char == COUNT:
            continue
        
        count += traverse(char, node)

    return count

def minion_game(string):
    build_tree(string)
    
    global stuart
    global kevin
    global root
    
    for _, key in enumerate(root.keys()):
        if is_vowel(key):
            kevin += traverse(key, root)
        else:
            stuart += traverse(key, root)

    if stuart > kevin:
        print(f"Stuart {stuart}")
    elif stuart < kevin:
        print(f"Kevin {kevin}")
    else:
        print("Draw")
        
        
if __name__ == '__main__':
    s = input()
    minion_game(s)
