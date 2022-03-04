def data_reverse(data):
    output = []
    lenght = len(data) // 8
    for bytes in range(8, lenght*8+1, 8):
        output.append(data[bytes-8:bytes])
    output = output[::-1]
    x = []
    for byte in output:
        x += byte
    return x
    

print(data_reverse([1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]))