def converterTempo(n1, p1, p2):
    if p1 < p2:
        if p1 == 0:
            p1 = 30
            k = p2 / p1
            n2 = n1 * k
            return n2
        if p1 > 0:
            k = p2 / p1
            n2 = n1 / k
            return n2
    if p1 > p2:
        if p2 == 0:
            p2 = 30
            k = p1 * p2
            n2 = n1 * k
            return n2
        if p2 > 0:
            k = p1 / p2
            n2 = n1 * k
            return n2
    if p1 == p2:
        return n1
