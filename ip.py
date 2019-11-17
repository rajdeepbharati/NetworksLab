def compute_class(dottedDecimalIP):
    arr = dottedDecimalIP.split('.')[0]
    ip = int(arr)

    if ip >= 1 and ip <= 126:
        return 'A'
    elif ip >= 128 and ip <= 191:
        return 'B'
    elif ip >= 192 and ip <= 223:
        return 'C'
    elif ip >= 224 and ip <= 239:
        return 'D'
    else:
        return 'E'


def split(dottedDecimalIP, ipClass):
    if ipClass == 'A':
        network = dottedDecimalIP.split('.')[0]
        host = '.'.join(dottedDecimalIP.split('.')[1:])
        print('Network ID is', network)
        print('Host ID is', host)
    elif ipClass == 'B':
        network = '.'.join(dottedDecimalIP.split('.')[:2])
        host = '.'.join(dottedDecimalIP.split('.')[2:])
        print('Network ID is', network)
        print('Host ID is', host)
    elif ipClass == 'C':
        network = '.'.join(dottedDecimalIP.split('.')[:3])
        host = '.'.join(dottedDecimalIP.split('.')[3:])
        print('Network ID is', network)
        print('Host ID is', host)
    else:
        print('In this Class, IP address is not\
               divided into Network and Host ID')


if __name__ == '__main__':
    print('Enter IP address in dotted decimal notation: ', end='')
    dottedDecimalIP = input()
    ipClass = compute_class(dottedDecimalIP)

    print('Given IP address belongs to class', ipClass)
    split(dottedDecimalIP, ipClass)
    binaryIP = ''
    for i in dottedDecimalIP.split('.'):
        i = int(i)
        binaryIP += '0'*(8-len(bin(i)[2:])) + bin(i)[2:]
    print('Equivalent Binary IP address is', binaryIP)
