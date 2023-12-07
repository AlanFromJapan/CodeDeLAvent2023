import io
import sys
import functools

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


typesNames = {
    7 : "Five of a kind",
    6 : "Four of a kind",
    5 : "Full house",
    4 : "Three of a kind",
    3 : "Two pair",
    2 : "One pair",
    1 : "High card"
}

class hand:
    cards = ""
    bid = 0
    type = 0

    def __init__(self, cards, bid, type=0):
        self.cards = cards
        self.bid = bid
        self.type = type    

    def __str__(self) -> str:
        return f"[cards: {self.cards}, bid: {self.bid}, type: {typesNames[self.type]}]"
    def __repr__(self) -> str:
        return self.__str__()
    
    def computeType(self):
        #7 = five of a kind, 1 = high card
        cardCount= {}

        for i in self.cards:
            if i in cardCount:
                cardCount[i] = cardCount[i] + 1
            else:
                cardCount[i] = 1

    
        if len(cardCount.keys()) == 1:
            #5 of a kind
            self.type = 7  
            return     
        if len(cardCount.keys()) == 2:
            if list(cardCount.values())[0] in [1,4]:
                #4 of a kind
                self.type = 6  
                return
            else:
                #full house
                self.type = 5  
                return
        if len(cardCount.keys()) == 3:
            max = 0
            for i in cardCount.values():
                if i > max:
                    max = i

            if max == 3:
                #3 of a kind
                self.type = 4  
                return
            else:
                #2 pair
                self.type = 3  
                return
        if len(cardCount.keys()) == 4:  
            #1 pair
            self.type = 2  
            return
        
        #high card
        self.type = 1  

CARDS_ORDER = "23456789TJQKA"

def compareHands (l:hand, r:hand):
    if l.type == r.type:
        #complex
        for i in range(5):
            if l.cards[i] == r.cards[i]:
                continue
            else:
                return -1 if  CARDS_ORDER.index(l.cards[i]) < CARDS_ORDER.index(r.cards[i]) else 1 if CARDS_ORDER.index(l.cards[i]) > CARDS_ORDER.index(r.cards[i]) else 0
    else:
        return -1 if l.type < r.type else 1 if l.type > r.type else 0


lcount = 0
HandList = []
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

        l = l.split(" ")
        h = hand(l[0], int(l[1]))
        h.computeType()
        HandList.append(h)
        #edit me v v v v v  
        #print(f"{lcount}: {l} > {h}") 

#print(f"BEFORE SORTING: {HandList}")
HandList = sorted(HandList, key=functools.cmp_to_key(compareHands))
#print(f"AFTER SORTING: {HandList}")

total = 0
for i in range(len(HandList)):  
    h = HandList[i]
    total = total + h.bid * (i+1)
print(f"The total is {total}")