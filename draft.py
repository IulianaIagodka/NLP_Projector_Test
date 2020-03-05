current_parent = None
indent_increase = 1


class Node(object):
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)
        obj.parent = self.data

    def __repr__(self):
        global current_parent
        global indent_increase

        if self.children:
            print_data = ""
            print_data += str(self.data) + "\n"
            indent = "    "

            for child in self.children:
                if current_parent != child.parent:
                    current_parent = child.parent
                    indent_increase += 1
                    print_data += ((indent * indent_increase) + "+--" + str(child) + "\n")
                else:
                    print_data += ((indent * indent_increase) + "+--" +  str(child) + "\n")

            indent_increase = 1
            current_parent = 0
            return print_data
        else:
            return str(self.data)


'''
a = Node("asciitree")
b = Node("sometimes")
c = Node("you")
d = Node("just")
e = Node("want")
f = Node("to")
g = Node("draw")
h = Node("trees")
j = Node("in")
k = Node("your")
l = Node ("terminal")'''

text = "(asciitree (sometimes you) (just (want to draw)) trees (in (your terminal)))"
text_tokens = text.split(" ")
#print (text_tokens)

root = Node(text_tokens [0])
#print (root)

l = 1
while l < len(text_tokens):
    if "(" in text_tokens[l]:


        root.add_child(Node(text_tokens[l]))

        root = Node(text_tokens[l])

    elif "(" and ")" not in text_tokens[l]:
        root.add_child(Node(text_tokens[l]))
        #print (root.children)
        #root = Node(text_tokens[l])
    l += 1
    print(root)
#print(root.children)


'''a.add_child(b)
a.add_child(d)
a.add_child(h)
a.add_child(j)

b.add_child(c)

d.add_child(e)
e.add_child(f)
e.add_child(g)

j.add_child(k)
k.add_child(l)

print(a)'''