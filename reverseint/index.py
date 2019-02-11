def reverse_int(n):
    if n >= 0:
        return int(str(n)[::-1])
    return int(str(abs(n))[::-1]) * -1
