from random import randint


class Roll:
    def __init__(self, tok):
        nums = tok.split('d')
        self.numDice = int(nums[0])
        self.diceTotal = int(nums[1])

    def eval(self):
        ret_str = "Rolling "+str(self.numDice)+"d"+str(self.diceTotal)+":"
        total = 0
        for i in range(0, self.numDice):
            val = randint(1, self.diceTotal)
            if i == self.numDice - 1:
                ret_str += str(val)
                print(val, end="")
            else:
                ret_str += str(val) + "+"
            total += val
        ret_str += "="+str(total)+"\n"
        return (total, ret_str)


def parseRollArgs(toks, adv, disadv):
    ret_str = ""
    for i in range(0, len(toks)):
        if "d" in toks[i]:
            roll = Roll(toks[i])
            if adv:
                r1 = roll.eval()
                r2 = roll.eval()
                toks[i] = max(r1[0], r2[0])
                ret_str += r1[1] if toks[i] == r1[0] else r2[1]
            elif disadv:
                r1 = roll.eval()
                r2 = roll.eval()
                toks[i] = min(r1[0], r2[0])
                ret_str += r1[1] if toks[i] == r1[0] else r2[1]
            else:
                r = roll.eval()
                toks[i] = r[0]
                ret_str += r[1]
        elif toks[i].isnumeric():
            toks[i] = int(toks[i])
            ret_str += "Modifier: " + str(toks[i]) + "\n"
        elif isinstance(toks[i], bool):
            toks.pop(i)
        elif not (isinstance(toks[i], int) or toks[i] == "+" or toks[i] == "-"):
            print("roller.py roll: error: invalid token")
            return
    total = 0
    for i in range(0, len(toks)):
        if i == 0:
            if toks[i] == '+' or toks[i] == '-':
                return "roller.py roll: error: invalid syntax, need a dice roll first"
            else:
                total += toks[i]
        elif toks[i] == "+":
            if isinstance(toks[i + 1], int):
                total += toks[i + 1]
            else:
                return "roller.py roll: error: invalid syntax, need a dice roll or number after operator"
        elif toks[i] == "-":
            if isinstance(toks[i + 1], int):
                total -= toks[i + 1]
            else:
                return "roller.py roll: error: invalid syntax, need a dice roll or number after operator"
    ret_str += "Total: " + str(total)
    return ret_str
