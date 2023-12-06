import io
import sys
import re



def listmul(l):
    r = 1
    for i in l:
        r = r * i
    return r

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
Times = []
Distance = []
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
        typ, l = l.split(":")

        if typ.strip() == "Time":
            for m in re.findall(r'\d+', l):
                Times.append(int(m))
        
        if typ.strip() == "Distance":
            for m in re.findall(r'\d+', l):
                Distance.append(int(m))        

#print(f"dists: {duration2distance}")

#formula 
# distance = (total_time - load_time) x load_time

#let's go naive
Results = []
for i in range(len(Times)):
    total_time = Times[i]
    dist = Distance[i]

    success = 0
    for load_time in range(1, total_time):
        if (total_time - load_time) * load_time > dist:
            success = success + 1
    Results.append(success)

print(f"Results: {Results}")
print(f"Result TOTAL: {listmul(Results)}")
