text = raw_input("Input text : ")

finde = raw_input("Input find : ")

i=0
while i < len(text)-len(finde):
    x = text[i:i+len(finde)]
    if x == finde:
        print "Yes"
        exit()
    else: print "No"
    i=i+1
