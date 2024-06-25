# Dynamic Syscall Filtering Tool

## Description

*This is part of the [TU Delft](https://github.com/TU-Delft-CSE) CSE3000 [Research Project](https://github.com/TU-Delft-CSE/Research-Project) (Q4 2024)*

This repo contains a script (`filter.py`) which collects and analyses syscalls from
a tracer's output(s). It also contains the source code of both "Hello World!" programs,
outputs of both [Binalyzer](https://github.com/felacek/Chestnut/tree/binalyzer-fix)
and [Callander](https://github.com/rpetrich/callander/releases/tag/v0.3)
(Dockerfile available in this repo), and the traces produced by running
all four programs in the specified scenarios, as well as the outputs from the script.

Programs tested include two "Hello World!" binaries whose source code can be found
in `hello-world`, `ls` version 9.5 and Openbox 3.6.1.
All outputs and the directory structure used for tracing ls can be found in `outputs`.

## How to run

First, record a trace using the command:

```sh
strace -tT -o output.trace <binary>
```

Use Python 3.8 or newer. Tested with Python 3.8.19 and Python 3.12.4

```sh
python filter.py [-f] <trace file> [<trace file> ...]
Option -f: Include the initial execve syscall in the output
```

The script produces a firejail command that one can use to run the binary in, as well as
a map from syscall to array of arguments that can be used in another seccomp application.

## Callander

There is a Dockerfile included for Callander, to run the container use the commands:

```sh
docker build -t callander .
docker run -it --rm -e DISPLAY=:1 -v /tmp/.X11-unix/X1:/tmp/.X11-unix/X1:rw -v ./out:/out --cap-drop=ALL --security-opt=no-new-privileges callander
```

Inside it, you can test any program you want:

```sh
callander --show-permitted asm 2> /out/asm.txt
```

To get the list of syscalls from a callander output file (no arguments),
use the provided python script (edit the first line of the file
to specify filename):

```sh
python callander_extraction.py
```

## Openbox

To run Openbox, create a Xephyr window:

```sh
Xephyr -br -ac -noreset -screen 800x600 :1  -extension MIT-SHM -extension XTEST
```

then run it either on bare metal:

```sh
DISPLAY=:1 strace -tT -o openbox.trace openbox
```

or inside the callander docker container:

```sh
callander --block-exec --ignore-dlopen --show-permitted openbox 2> /out/openbox.txt
```

