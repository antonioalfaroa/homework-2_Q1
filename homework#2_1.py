def division(x, y):
    x = list(x)  # Convert string to list for easier manipulation
    y = list(y)
    z = len(y)

    for i in range(len(x) - z + 1):
        if x[i] == '1':
            for j in range(z):
                x[i + j] = str(int(x[i + j]) ^ int(y[j]))

    # Remove leading zeros
    remainder = ''.join(x).lstrip('0')

    if remainder == '':
        remainder = '0'  # If remainder is empty, set it to '0'

    return remainder

def XoRFunction(x, y):
    res = [str(int(xi) ^ int(yi)) for xi, yi in zip(x, y)]
    return ''.join(res)

def encoding(msg, poly):
    # Append zeros equal to the degree of the polynomial
    msg = msg + '0' * (len(poly) - 1)

    # Perform polynomial division
    remainder = division(msg, poly)

    # Combine original message and remainder to get the encoded output
    encoded_output = msg[:-len(remainder)] + remainder

    return encoded_output


def decoding(rcv, poly):
    # Perform polynomial division on the received signal
    decode = division(rcv.replace(' ', ''), poly)

    # Check for errors
    if '1' in decode:
        return "Error"
    else:
        return "No error"

# Test Cases
org_sig1 = '1010'
poly = '100101'
x = encoding(org_sig1, poly)
print(x)

org_sig2 = '1100'
poly2 = '100101'
x2 = encoding(org_sig2, poly2)
print(x2)

received_sig1 = '1010 00111'
y1 = decoding(received_sig1, poly)
print(y1)

received_sig2 = '1100 01111'
y2 = decoding(received_sig2, poly2)
print(y2)

received_sig3 = '1100 11001' 
poly = '100101'
y3 = decoding (received_sig3, poly) 
print(y3)

received_sig4 = '1100 11111' 
poly = '100101'
y4 = decoding (received_sig4, poly) 
print(y4)
