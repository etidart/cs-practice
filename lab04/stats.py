def parse_record(line):
    res = {}
    split = line.split(";")
    if len(split) != 3:
        raise ValueError("полей не ровно 3")
    if split[0] == "":
        raise ValueError("город пустой")
    if split[2] == "":
        raise ValueError("дата пустая")
    try:
        temp = float(split[1])
        res["city"] = split[0]
        res["temp"] = temp
        res["date"] = split[2]
        return res
    except ValueError:
        raise ValueError("температура не число")

def read_valid(lines):
    res = []
    for line in lines:
        if line == "":
            continue
        try:
            res.append(parse_record(line))
        except ValueError:
            continue
    return res

def average_by_city(records):
    total = {}
    count = {}
    for rec in records:
        total[rec["city"]] = total.get(rec["city"], 0) + rec["temp"]
        count[rec["city"]] = count.get(rec["city"], 0) + 1
    res = {}
    for city in total:
        res[city] = total[city] / count[city]
    return res

def warmest_city(records):
    avg = average_by_city(records)
    best = ""
    for city in avg:
        if best == "" or avg[city] > avg[best] or (avg[city] == avg[best] and city < best):
            best = city
    return best
