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
resym = re.compile(r"[^0-9.]+")
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
    nums = []
    for m in renum.finditer(l):
        #print(m.start(), m.group(0))
        #check same line
        if resym.search(l[max (0, m.start()-1) : min (len(l), m.end()+1)]):
            nums.append(int(m.group(0)))
            continue
        if resym.search(l[max (0, m.start()-1) : min (len(l), m.end()+1)]):
            nums.append(int(m.group(0)))
            continue
        
        #check previous line
        if lcount > 0:
            if resym.search(lines[lcount-1] [max (0, m.start()-1) : min (len(l), m.end()+1)]):
                nums.append(int(m.group(0)))
                continue
        #check next line
        if lcount < len(lines)-1:
            if resym.search(lines[lcount+1] [max (0, m.start()-1) : min (len(l), m.end()+1)]):
                nums.append(int(m.group(0)))
                continue

    lcount = lcount + 1
    print(f"{lcount}: {l} -> {nums}") 
    results.extend(nums)

print(f"Results: {sum(results)}")
    