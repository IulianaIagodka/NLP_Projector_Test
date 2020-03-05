
text = "(asciitree (sometimes you) (just (want to draw)) trees (in (your terminal)))"
text_tokens = text.split(" ")
#print (text_tokens[1])

class Node(object):
    def __init__(self, value, children = []):
        self.value = value
        self.children = children
    def add_child (self, obj):
        self.children.append(obj)

Node(asciitree)

#for t in text_tokens:
    #print (Node(t))
l = 0
for l in range(len(text_tokens)):
    t = text_tokens[l]
    if "(" in t:
        node = (Node(t).value)

    elif "(" or ")" not in t:
        Node(t).add_child()
    l += 1

#enclosed = Forward()
#nestedParens = nestedExpr('(', ')', content=enclosed)
#enclosed << (Word(alphanums+'.') | ',' | nestedParens)


#tokens = nltk.word_tokenize(text)
# remove punctuation
#tokens = [word.replace("-"," ") for word in tokens if word not in string.punctuation]
#print (tokens)