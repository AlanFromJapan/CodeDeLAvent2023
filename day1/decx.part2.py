import io
import sys
import re

filename = "input.txt"
llimit = -1
if len(sys.argv) < 2:
    print("INFO: no filename passed as param, defaulting to 'input.txt'")
else:
    print(f"INFO: 1st param is filename, will process '{sys.argv[1]}'")
    filename = str(sys.argv[1])

if len(sys.argv) >= 3:
    print(f"INFO: 2nd param is limit of lines to process, will process only the first {sys.argv[2]} lines")
    llimit = int(sys.argv[2])


def transform(l: str):
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    #print(f"Transforming {l}")
    s = ""
    done = False
    for c in l:
        s = s + c

        for i in range(0, len(numbers)):
            s2 = re.sub(numbers[i], str(i), s, count=1)
            if len (s2) != len(s):
                l = s2 + l[len(s):]
                done = True
                break
        if done:
            break

    #print(f"Transforming {l}")
    s = ""
    done = False
    for c in l[::-1]:
        s =  c + s #BEWARE ORDER!
        
        for i in range(0, len(numbers)):
            s2 = re.sub(numbers[i], str(i), s)
            if len (s2) != len(s):
                #l = re.sub(numbers[i], str(i), l)
                l = l[:-len(s)] + s2
                done = True
                break
        if done:
            break

    return l


lcount = 0
total = 0
with io.open(filename, "r") as f:
    while True:
        l = f.readline()
        lcount = lcount +1

        if not l:
            #finished!
            break

        if llimit > 0 and lcount > llimit:
            break

        #process!
        l = l.strip()

        #edit me v v v v v  
        orig = l
        l = transform(l)
        
        l = re.sub("\D", "", l)
        v = ""
        v = l[0] + l[-1]
       
        print(f"{lcount}: {orig} => {l} => {v}") 
        total = total + int(v)

print(f"Total: {total}")