p = []
n = 7
for i in 'abcdefg':
    for j in 'abcdefg':
        if i == j:
            continue;
        s = i+j
        p.append(s)
p = ['ab','ac','ad','ae','af','ag','bc','bd','be','bf','bg','cd','ce','cf','cg','de','df','dg','ef','eg','fg']
print len(p)
for i1 in p:
    for i2 in p:
        for i3 in p:
            for i4 in p:
                for i5 in p:
                    for i6 in p:
                        for i7 in p:
                            t = set()
                            t.add(i1)
                            t.add(i2)
                            t.add(i3)
                            t.add(i4)
                            t.add(i5)
                            t.add(i6)
                            t.add(i7)
                            if len(t) != n:
                                continue
                            s = i1 + i2 + i3 + i4 + i5 + i6 + i7
                            s1 = list(s)
                            if sorted(s1) !=  list('aabbccddeeffgg'):
                                continue;
                            l = []
                            l.append(i1)
                            l.append(i2)
                            l.append(i3)
                            l.append(i4)
                            l.append(i5)
                            l.append(i6)
                            l.append(i7)
                            print l




