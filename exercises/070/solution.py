import string
alpha = string.lowercase
for n in range(0, len(alpha)):
    for m in range(1, len(alpha) -1):
        print( "%s%s" % (alpha[n], alpha[m]))
