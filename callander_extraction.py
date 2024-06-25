with open("out/openbox.txt") as f:
    calls = {f.readline()[31:].split("(")[0]}
    for line in f:
        c = line.split("(")[0]
        if c == "\n":
            continue
        calls.add(c)
    print(calls)
    print(len(calls))