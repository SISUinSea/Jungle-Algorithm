def exp(b, n):
    if n == 0:
        return 1
    return b * exp(b, n - 1)


def fast_exp(b, n):
    if n == 0:
        return 1

    if n % 2 == 0:
        aux = fast_exp(b, n//2)
        return aux * aux
    else:
        return b * fast_exp(b, n - 1)