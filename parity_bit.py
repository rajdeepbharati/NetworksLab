import sys


def detect_parity_bit_error(data, parityBit):
    """
    Checks (validated) parity bit at the receiver's end.
    Returns True if sender has sent correct parity bit,
    else returns False.
    """
    onesCount = 0
    for d in data:
        if d == '1':
            onesCount += 1
        elif d == '0':
            pass
        else:
            print('Data is not in binary!!!')
            sys.exit()
    if onesCount % 2 == 0:
        pB = 0
    else:
        pB = 1
    if pB == parityBit:
        return True
    else:
        return False


if __name__ == '__main__':
    print('Enter data (binary): ', end='')
    data = input()
    print('Enter parity bit (0 or 1) from sender: ', end='')
    parityBit = int(input())
    valid = detect_parity_bit_error(data, parityBit)
    if valid:
        print('Data is accepted')
    else:
        print('Data is rejected')
