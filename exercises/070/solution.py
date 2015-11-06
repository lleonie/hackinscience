import string
alpha = string.ascii_lowercase
for n in range(0, len(alpha)):
    for m in range(0, len(alpha)):
        if n != m:
            print("%s%s" % (alpha[n], alpha[m]))
