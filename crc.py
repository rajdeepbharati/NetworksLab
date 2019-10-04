"""
Author: Rajdeep Bharati

Program to get a dataword and generator polynomial from stdin
and create corresponding Cyclic Redundancy Check (CRC) codeword.
"""


def xor(a, b):
    result = []

    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')

    return ''.join(result)


def divide(divisor, dividend):
    pick = len(divisor)

    temp = dividend[0:pick]  # pick first len_key chars

    while pick < len(dividend):
        if temp[0] == '1':
            temp = xor(divisor, temp) + dividend[pick]
        else:
            temp = xor('0' * pick, temp) + dividend[pick]

        pick += 1

    if temp[0] == '1':
        temp = xor(divisor, temp)
    else:
        temp = xor('0' * pick, temp)

    checksum = temp
    return checksum


if __name__ == '__main__':

    print('Enter dataword: ', end='')
    dataWord = input()
    print('Enter generatorPolynomial as binary number: ', end='')
    generatorPolynomial = input()

    len_key = len(generatorPolynomial)

    checksum = divide(generatorPolynomial, dataWord + '0' * (len_key-1))

    codeWord = dataWord + checksum
    print(f'codeword is: {codeWord}')
