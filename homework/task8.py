def main(num):
    i1 = (num >> 0) & 0xFF
    i2 = (num >> 8) & 0x1FF
    i3 = (num >> 17) & 0xFF
    i4 = (num >> 25) & 0x3FF
    i5 = (num >> 35) & 0x7F

    result = (i1 << 0) | (i5 << 8) | (i3 << 15) | (i2 << 23) | (i4 << 32)

    return hex(result)

print(main(873183797746))