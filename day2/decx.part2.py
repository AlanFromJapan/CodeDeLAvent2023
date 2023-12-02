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


MAXES = {"red": 12, "green": 13, "blue": 14}
REGEX_COLORS = re.compile(r"((?P<blue>\d+)\s+blue|(?P<red>\d+)\s+red|(?P<green>\d+)\s+green)")

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
        l = l.split(":")[1]
        rounds = l.split(";")
        roundmaxes = {"red": 0, "green": 0, "blue": 0}

        for r in rounds:
            colors = r.strip().split(",")
            for c in colors:
                m = REGEX_COLORS.search(c)
                if m:
                    d = m.groupdict()
                    for colorname in MAXES.keys():
                        if d[colorname]:
                            #the color is in the round
                            if int(d[colorname]) > roundmaxes[colorname]:
                                #the color is too high
                                roundmaxes[colorname] = int(d[colorname])

        #now we have the mins for each color, we can calculate the total
        roundtotal = roundmaxes["red"] * roundmaxes["green"] * roundmaxes["blue"]
        total = total + roundtotal

        #edit me v v v v v  
        print(f"{lcount}: {l} (round total {roundtotal}, running total {total})") 

print(f"Total: {total}")