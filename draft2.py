text = "(asciitree (sometimes you) (just (want to draw)) trees (in (your terminal)))"

new_token = []
tokens_list = []
tokens_list_of_list = []

for t in text:
    if t in "(":
        if tokens_list!= 0 and tokens_list not in tokens_list_of_list:
            tokens_list_of_list.append(tokens_list)
        else:
            tokens_list = []

    elif t.isalpha():
        new_token.append(t)

    elif t == " " and len(new_token) != 0:
        new_token = "".join(new_token)
        #print("".join(new_list))
        tokens_list.append(new_token)
        new_token = []

    elif t in ")" and len(tokens_list) != 0:
        new_token = "".join(new_token)
        #print("".join(new_list))
        tokens_list.append(new_token)
        tokens_list_of_list.append(tokens_list)
        #print (tokens_list)
        tokens_list = []
        new_token = []

print ("" + tokens_list_of_list[0][0])
for x in tokens_list_of_list[1: ]:
    print("+--" + x[0])
    for r in x[1: ]:
        print("|    +--" + r)


#print(tokens_list)
