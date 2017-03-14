text = raw_input("Input text : ")

finde = raw_input("Input find : ")

i=0
kount=0

if text.count(finde):
    print "Count = {}".format(text.count(finde))
else:
    print "not"

while i < len(text)-len(finde):
    x = text[i:i+len(finde)]
    if x == finde:
        #print "Yes"
        kount = kount + 1
#    else: print "No"
    i=i+1
print "Kount = {}".format(kount)
