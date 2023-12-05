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


rex = re.compile(r"(\d+) (\d+) (\d+)")
lcount = 0
seeds = []
direct = []
currentDict = -1
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
        
        if l == "":
            continue

        if lcount == 1:
            #first line
            l = l.split(":")[1].strip()
            seeds = [int(x) for x in l.split(" ")]
            print(f"seeds: {seeds}")
            continue
        
        if l.endswith("map:"):
            #new map!
            currentDict = currentDict + 1
            direct.append([])
            continue

        #should be real data to add to current dict
        m = rex.match(l)
        if m:
            source = int(m.group(2))
            cnt = int(m.group(3))
            dest = int(m.group(1))

            direct[currentDict].append([source, cnt, dest])
        
        #edit me v v v v v  
        #print(f"{lcount}: {l}") 


seed2location = {}
for s in range(int(len(seeds)/2)):
    firstSeed = seeds[s *2]
    lastSeed = seeds[s *2] + seeds[s *2 +1] -1
    print(f"firstSeed: {firstSeed}, lastSeed: {lastSeed}")

    for i in range(firstSeed, lastSeed+1):
        v = i
        for j in range(len(direct)):
            #in that map (j)
            for k in range(len(direct[j])):
                source, cnt, dest = direct[j][k]
                if v in range(source, source+cnt):
                    v = v - source + dest
                    break
        seed2location[i] = v

print(f"seed2location: {seed2location}")
print(f"min location: {min(seed2location.values())}")
