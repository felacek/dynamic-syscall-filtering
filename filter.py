import pprint
import json
import sys

class Call:
    def __init__(self, line: str) -> None:
        vals = line.split() 
        self.timestamp = vals[0]
        func, equals = takeWhile(lambda x: x != "=", vals[1:-1])
        self.ret = ' '.join(vals[equals+2 : -1])
        self.duration = vals[-1]
        self.name = func[0].split("(")[0]
        if self.name == "+++" or self.name == "---":
            self.valid = False
            return
        else:
            self.valid = True
        self.args = parseArgs(dropWhile(lambda x: x == '(', ' '.join(func))[1:-1])

# awful basic parser
def parseArgs(line: str):
    ret = []
    outside = 0
    inString = False
    prevSplit = 0
    i = -1
    length = len(line)-1
    prevChar = ''
    #print(line)
    for x in line:
        i += 1
        if i == length:
            ret.append(line[prevSplit:])
        elif outside == 0 and not inString and x == ',':
            #print(line, i, prevSplit)
            assert(prevSplit < i)
            ret.append(line[prevSplit : i])
            prevSplit = i+2

        if not inString and x in "([{":
            outside += 1
        elif not inString and x in ")]}":
            outside -= 1
        elif not inString and x == '"':
            inString = True
        elif inString and prevChar != '\\' and x == '"':
            inString = False
        
        prevChar = x
    #print(outside, inString, line)
    assert(outside == 0)
    assert(inString is False)
    return ret

def takeWhile(predicate, iterable):
    i = -1
    ret = []
    for x in iterable:
        i += 1
        if not predicate(x):
            break
        ret.append(x)
    return (ret, i)

def dropWhile(predicate, iterable):
    i = -1
    for x in iterable:
        i += 1
        if predicate(x):
            break
    return iterable[i:]

def analyse(calls):
    res = {}
    for x in calls:
        if res.get(x.name) == None:
            # 6 is the maximum amount of syscall arguments in an x86-64 system
            # https://www.man7.org/linux/man-pages/man2/syscall.2.html
            res[x.name] = [set() for a in range(6)]
        i = 0
        for arg in res[x.name]:
            if i >= len(x.args):
                break
            arg.add(x.args[i])
            i += 1
    return res

def possibleArgs(analysis):
    for x in analysis.values():
        for arg in x:
            if len(arg) == 0:
                continue
            if all(a[:2] == "0x" for a in arg):
                # all arguments are addresses, allow addresses only
                arg.clear()
                arg.add(0)
            elif len(arg) > 3:
                arg.clear()
                arg.add(1)
    return analysis

def create_docker_profile(calls):
    res = {"defaultAction": "SCMP_ACT_ERRNO",
           "syscalls": [{
               "name": c,
               "action": "SCMP_ACT_ALLOW"
           } for c in calls.keys()]
        }
    with open("profile.json", "w") as f:
        f.write(json.dumps(res))

def create_seccomp_profile(calls):
    res = {"main_thread": {
            "mismatch_action": "kill_process",
            "match_action": "allow",
            "filter": [{"syscall": c} for c in calls.keys()]
        }
    }
    with open("seccomp.json", "w") as f:
        f.write(json.dumps(res))


def main(traces):
    full = traces[0] == "-f"
    if full:
        traces.pop(0)
    if len(traces) == 0:
        print("Usage: python filter.py [-f] <trace file> [<trace file> ...]\nOption -f: Include the initial execve syscall in the output")
        return
    calls = []
    for trace in traces:
        with open(trace, "r") as f:
            if not full:
                f.readline()
            calls += [x for x in (Call(line) for line in f) if x.valid]

    analysis = analyse(calls)
    print("All used syscalls with possible arguments:")
    pprint.pprint(possibleArgs(analysis))
    create_docker_profile(analysis)
    create_seccomp_profile(analysis)

    string = "firejail --noprofile --seccomp.keep="
    for x in analysis.keys():
        string += x + ","

    print("\n\nCommand to run firejail (insert name of binary at the end):")
    print(string[:-1])
    print("\nFound " + str(len(analysis.keys())) + " syscalls.")
    print("Finished running filter script with " + str(len(traces)) + " traces")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python filter.py [-f] <trace file> [<trace file> ...]\nOption -f: Include the initial execve syscall in the output")
    else:
        main(sys.argv[1:])
