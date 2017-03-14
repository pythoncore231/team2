text = raw_input("Input text : ")

finde = raw_input("Input find : ")

i=0
kount=0
while i < len(text)-len(finde):
    x = text[i:i+len(finde)]
    if x == finde:
        print "Yes"
        kount = kount + 1
#    else: print "No"
    print "Count = {}".format(kount)
    i=i+1