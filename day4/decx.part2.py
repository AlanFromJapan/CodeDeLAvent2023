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


rex = re.compile(r"(\d+)")
cardcount = {  }
total = 0
lcount = 0
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
        l = l.split(":")[1]

        lwinners = l.split("|")[0]
        lmynums = l.split("|")[1]

        #edit me v v v v v  
        winners = [int(x) for x in rex.findall(lwinners)]
        mynums = [int(x) for x in rex.findall(lmynums)]

        win = 0
        for n in mynums:
            if n in winners:
                win = win + 1

        #add self
        if lcount not in cardcount:
            cardcount[lcount] = 1

        if win > 0:
            for i in range(win):
                cardcount[lcount + i +1] = cardcount[lcount] + (cardcount[lcount + i +1] if (lcount + i + 1) in cardcount else 1)

        print(f"{lcount}: {l} -> win {win} -> {cardcount}") 

total = sum(cardcount.values())
print(f"Total = {total}")