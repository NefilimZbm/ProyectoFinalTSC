from math import sin, cos, sqrt, atan2, radians


def distance(x, y) -> float:
    rt = 6373.0  ## radio aproximado de la tierra
    lat1 = radians(x[0])
    lon1 = radians(x[1])
    lat2 = radians(y[0])
    lon2 = radians(y[1])
    if lat1 == lat2 and lon1 == lon2:
        return 0
    else:
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        d = rt * c
        return d
