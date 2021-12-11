import pytest
import sys
from math import floor, ceil
def abrir_archivo(name: str) -> list:
    data = []
    with open(name,"r") as archivo:
        for line in archivo:
            data.append(line.rstrip("\n"))
    return data

def score(data: list) -> int:
    close_keys = {")": 1, "]":2, "}": 3, ">": 4}
    keys = {"(": ")", "[": "]", "{": "}", "<": ">"}
    alt_keys = {")": "(", "]": "[", "}": "{", ">": "<"}
    uncompleted = []
    suma = 0
    for line in data:
        pairs = []
        scored_brackets = []
        for c in line:
            if c in alt_keys:
                _c = pairs[len(pairs) - 1]
                if _c == alt_keys[c]:
                    pairs.pop()
                else:
                    scored_brackets.append(c)
                    pairs.pop()
            else:
                pairs.append(c)

        if len(scored_brackets) > 0:
            continue
        uncompleted.append(pairs)

    scores = []
    for line in uncompleted:
        for c in line:
            print(c,end="")
        print("")
    for line in uncompleted:
        line_score = 0
        for c in range(len(line) - 1, -1, -1):
            line_score *= 5
            line_score += close_keys[keys[line[c]]]
        scores.append(line_score)
    scores.sort()
    suma = scores[floor(len(scores) / 2)]
    print(scores)
    print(suma)
    return suma

def test():
    archivo = abrir_archivo("dia10/dia10_t.txt")
    data = score(archivo)
    ok_data = 288957 
    assert data == ok_data, "No son los mismos tipos"
    print("ok data:", ok_data)
if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1] == "t":
            test()
    else:
        score(abrir_archivo("dia10/dia10.txt"))
