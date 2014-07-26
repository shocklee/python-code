import random

def getWord(filename, number):
    fin = open(filename)
    wlist = []
    word = []
    for line in fin:
        words = line.strip()
        word = words.split(' ')  # Split on whitespace
        wlist.append(word[0])
    fin.close()
    random.shuffle(wlist)
    return wlist[0: number]

def aOrAn(adjList):
    aan = []
    for word in adjList:
        if(word[0] in ['a', 'e', 'i', 'o', 'u']):
           aan.append('An')
        else:
           aan.append('A')
    return aan    

def makePoem():
    """Create a poem imspired by the structure suggested by Clifford Piclover"""
    adjFile = r"C:\Users\shockma\Documents\Special\Python\extract\adj.txt"
    advFile = r"C:\Users\shockma\Documents\Special\Python\extract\adv.txt"
    nounFile = r"C:\Users\shockma\Documents\Special\Python\extract\noun.txt"
    prepFile = r"C:\Users\shockma\Documents\Special\Python\extract\prepositions.txt"
    verbFile = r"C:\Users\shockma\Documents\Special\Python\extract\verb.txt"
    adj = getWord(adjFile, 3)
    adv = getWord(advFile, 1)
    noun = getWord(nounFile, 3)
    prep = getWord(prepFile, 2)
    verb = getWord(verbFile, 3)
    aan = aOrAn(adj)
    return aan[0] + ' ' + adj[0] \
        + ' ' + noun[0] + '\n\n' \
        + aan[0] + ' ' + adj[0] \
        + ' ' + noun[0] \
        + ' ' + verb[0] \
        + ' ' + prep[0] \
        + ' the ' + adj[1] \
        + ' ' + noun[1] + '\n' \
        + adv[0] \
        + ', the ' + noun[0] \
        + ' ' + verb[1] + '\n'\
        + 'the ' + noun[1] \
        + ' ' + verb[2] \
        + ' ' + prep [1] \
        + ' ' + aan[2].lower() + ' ' + adj[2] \
        + ' ' + noun[2]
    
print makePoem()
