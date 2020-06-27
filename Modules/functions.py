import math as mt


def distance(x, y) -> float:
    rt = 6373            ## radio aproximado de la tierra
    lat1 = mt.radians(x[0])
    lon1 = mt.radians(x[1])
    lat2 = mt.radians(y[0])
    lon2 = mt.radians(y[1])
    if lat1 == lat2 and lon1 == lon2:
        return 0
    else:
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = mt.sin(dlat / 2) ** 2 + mt.cos(lat1) * mt.cos(lat2) * mt.sin(dlon / 2) ** 2
        c = 2 * mt.atan2(mt.sqrt(a), mt.sqrt(1 - a))
        d = rt * c * 1000
        return d
