import pytest
import sys
def abrir_archivo(name: str) -> list:
    data = []
    with open(name,"r") as archivo:
        for line in archivo:
            data.append(line.rstrip("\n"))
    return data

def score(data: list) -> int:
    close_keys = {")": 3, "]": 57, "}": 1197, ">": 25137}
    keys = {")": "(", "]": "[", "}": "{", ">": "<"}
    suma = 0
    for line in data:
        final_score = 0
        pairs = []
        scored_brackets = []
        for c in line:
            if c in keys:
                _c = pairs[len(pairs) - 1]
                if _c == keys[c]:
                    pairs.pop()
                else:
                    scored_brackets.append(c)
                    pairs.pop()
            else:
                pairs.append(c)

        for c in  scored_brackets:
            final_score += close_keys[c]

        suma += final_score
    print(suma)
    return suma

def test():
    archivo = abrir_archivo("dia10/dia10_t.txt")
    data = score(archivo)
    ok_data = 26397
    assert data == ok_data, "No son los mismos tipos"
    print("ok data:", ok_data)
if __name__ == "__main__":
    for arg in range(len(sys.argv)):
        if arg == 1:
            if sys.argv[arg] == "t":
                test()
        else:
            score(abrir_archivo("dia10/dia10.txt"))
