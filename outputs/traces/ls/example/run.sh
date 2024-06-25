strace -tT -o out/1.trace ls full
strace -tT -o out/2.trace ls full -a
strace -tT -o out/3.trace ls full -A
strace -tT -o out/4.trace ls full -l
strace -tT -o out/5.trace ls full -l --author
strace -tT -o out/6.trace ls full -lh
strace -tT -o out/7.trace ls full -la
strace -tT -o out/8.trace ls full -lA
strace -tT -o out/9.trace ls full -li
strace -tT -o out/0.trace ls full -lr
strace -tT -o out/a.trace ls full -lR
strace -tT -o out/b.trace ls full -lU
strace -tT -o out/c.trace ls full -la --author
strace -tT -o out/d.trace ls full -lah
strace -tT -o out/e.trace ls full -lai
strace -tT -o out/f.trace ls full -lar
strace -tT -o out/g.trace ls full -laR
strace -tT -o out/h.trace ls full -laU
strace -tT -o out/i.trace ls full -lah --author
strace -tT -o out/j.trace ls full -lai --author
strace -tT -o out/k.trace ls full -lar --author
strace -tT -o out/l.trace ls full -laR --author
strace -tT -o out/m.trace ls full -laU --author
strace -tT -o out/n.trace ls full -laih
strace -tT -o out/o.trace ls full -larh
strace -tT -o out/p.trace ls full -laRh
strace -tT -o out/q.trace ls full -laUh
strace -tT -o out/r.trace ls full -lair
strace -tT -o out/s.trace ls full -laiR
strace -tT -o out/t.trace ls full -laiU
strace -tT -o out/u.trace ls full -larR
strace -tT -o out/v.trace ls full -laih --author
strace -tT -o out/w.trace ls full -larh --author
strace -tT -o out/x.trace ls full -laRh --author
strace -tT -o out/y.trace ls full -laUh --author
strace -tT -o out/z.trace ls full -lair --author
strace -tT -o out/A.trace ls full -laiR --author
strace -tT -o out/B.trace ls full -laiU --author
strace -tT -o out/C.trace ls full -larR --author
strace -tT -o out/D.trace ls full -laihr
strace -tT -o out/E.trace ls full -laihR
strace -tT -o out/F.trace ls full -laihU
strace -tT -o out/G.trace ls full -lairR
strace -tT -o out/H.trace ls full -laihr --author
strace -tT -o out/I.trace ls full -laihR --author
strace -tT -o out/J.trace ls full -laihU --author
strace -tT -o out/K.trace ls full -lairR --author
strace -tT -o out/L.trace ls full -larhR
strace -tT -o out/M.trace ls full -larhR --author
strace -tT -o out/N.trace ls full -laRhU
strace -tT -o out/O.trace ls full -laRhU --author
