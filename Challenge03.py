def friend(x):
    b = []
    for friend in range(0, len(x)):
        if x[friend] in '1234567890':
            pass
        else:
            if len(x[friend]) <= 4:
                b.append(x[friend])
    return b

friends = ['zvOc', 'VX', 'fCTRFzkSPVs', 'qCaQ', 'HRSS', '', 'ZCBySYcfkfcbbYrLKJtG', 'inBlLQpnTCWd']
print(friend(friends))