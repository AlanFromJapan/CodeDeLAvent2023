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



lcount = 0
renum = re.compile(r"\d+")
resym = re.compile(r"\*")
lines = []
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

        lines.append(l)        

lcount = 0
results = []
for l in lines:
    lineGears = []
    for m in resym.finditer(l):
        # for each star
        gears = []

        #check same line
        for n in renum.finditer(l):
            if m.start() == n.start() -1 or m.start() == n.end() :
                gears.append(int(n.group(0)))
                continue

        #check previous line
        if lcount > 0:
            for n in renum.finditer(lines[lcount-1]):
                if m.start() >= n.start() -1 and m.end() <= n.end() +1:
                    gears.append(int(n.group(0)))
                    continue

        #check next line
        if lcount < len(lines)-1:
            for n in renum.finditer(lines[lcount+1]):
                if m.start() >= n.start() -1 and m.end() <= n.end() +1:
                    gears.append(int(n.group(0)))
                    continue
        
        if len(gears) == 2:
            results.append( gears[0] * gears[1])
            lineGears.append(gears)
        if len(gears) > 2:
            print(f"ERROR: more than 2 gears found for star {m.group(0)} in line {lcount}")
            print(f"ERROR: gears: {gears}")
            print(f"ERROR: line: {l}")
            print(f"ERROR: previous line: {lines[lcount-1]}")
            print(f"ERROR: next line: {lines[lcount+1]}")
            exit(1)


    lcount = lcount + 1
    print(f"{lcount}: {l} -> {lineGears}") 

print(f"results: {results}")
print(f"Results: {sum(results)}")
