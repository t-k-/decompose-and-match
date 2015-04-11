def easy_labels(paths):
    ret = list()
    for p in paths:
        ret.append([0] * len(p))
    return ret

def init_QC(qpaths, dpaths):
    Q = set()
    C = dict()
    for qpath in qpaths:
        q = qpath[len(qpath) - 1]
        Q.add(q)
        C[q] = set()
        for dpath in dpaths:
            d = dpath[len(dpath) - 1]
            if similar(q, d):
                C[q].add(d)
    return (Q, C)

def print_QC(Q, C):
    print 'Q set:'
    for q in Q:
        print 'C_' + str(q) + '=' + str(C[q])

def similar(q, d):
    for i in range(0, len(qpaths)):
        t = qpaths[i]
        if t[len(t) - 1] == q:
            qlabel = qlabels[i]
    for i in range(0, len(dpaths)):
        t = dpaths[i]
        if t[len(t) - 1] == d:
            dlabel = dlabels[i]
    if len(qlabel) != len(dlabel):
        return False
    for i in range(0, len(qlabel)):
       if qlabel[i] != dlabel[i]:
            return False
    return True

def a_path_in(Q):
    for q in Q:
        return q

def lcp(a, b, path_set):
    for apath in path_set:
        if apath[len(apath) - 1] == a:
            break
    for bpath in path_set:
        if bpath[len(bpath) - 1] == b:
            break
    cnt = 0
    for i in range(0, len(apath)):
        if apath[i] == bpath[i]:
            cnt += 1 
        else:
            break
    return cnt

def remove_candidate(d, Q, C):
    for a in Q:
        if len(C[a]) == 0:
            return dict()
        else:
            if d in C[a]: C[a].remove(d)
    return C

def match(a, a_, Q, C):
    P = set()
    subQ = dict()
    print 'reference path ' + str(a) + ' in Q'
    print 'reference path ' + str(a_) + ' in D'
    for b in Q:
        t = lcp(a, b, qpaths)
        if t not in P:
            subQ[t] = set()
        subQ[t].add(b)
        P.add(t)
    for t in P:
        for b in subQ[t]:
            for b_ in C[b].copy():
                if t != lcp(a_, b_, dpaths):
                    C = remove_candidate(b_, subQ[t], C)
                    if len(C) == 0:
                        return False
        if decompose_and_match(subQ[t], C) == False:
            return False
    return True 

def decompose_and_match(Q, C):
    print_QC(Q, C)
    if len(Q) == 0:
        return True
    a = a_path_in(Q)
    Q.remove(a)
    new_Q = Q
    for a_ in C[a]:
        new_C = remove_candidate(a_, new_Q, C)
        if len(new_C) == 0:
            return False
        if match(a, a_, new_Q, new_C) == True:
            return True
    return False

def main():
    (Q, C) = init_QC(qpaths, dpaths)
    print decompose_and_match(Q, C)

qpaths = [
    [0, 2, 6, 13, 27, 55, 111],
    [0, 2, 6, 13, 27, 55, 112],
    [0, 2, 6, 13, 27, 56],
    [0, 2, 6, 14, 29, 60, 121],
    [0, 2, 6, 14, 29, 60, 122, 245],
    [0, 2, 6, 14, 29, 60, 122, 246]]

dpaths = [
    [0, 1, 3],
    [0, 1, 4],
    [0, 2, 5, 12],
    [0, 2, 5, 11, 23],
    [0, 2, 5, 11, 24],
    [0, 2, 6, 14, 30],
    [0, 2, 6, 13, 27, 55, 111],
    [0, 2, 6, 13, 27, 55, 112],
    [0, 2, 6, 13, 27, 56],
    [0, 2, 6, 13, 28, 57],
    [0, 2, 6, 13, 28, 58, 117, 235],
    [0, 2, 6, 13, 28, 58, 117, 236],
    [0, 2, 6, 13, 28, 58, 118],
    [0, 2, 6, 14, 29, 59],
    [0, 2, 6, 14, 29, 60, 121],
    [0, 2, 6, 14, 29, 60, 122, 245],
    [0, 2, 6, 14, 29, 60, 122, 246]]

qlabels = easy_labels(qpaths)
dlabels = easy_labels(dpaths)

main()
