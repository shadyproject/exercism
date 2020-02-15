def slices(series, length):
    subseries = []

    if series == "":
        raise ValueError("Cannot get slice from empty series")

    if length <=  0:
        raise ValueError("Cannot get slice of negatice or 0 length")

    if len(series) < length:
        raise ValueError("Cannot get subseries with length longer than series")

    for i in range(0, len(series)):
        sub = series[i:length+i]
        if len(sub) < length:
            break
        subseries.append(sub)

    return subseries
