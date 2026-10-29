import csv, json, io
def csv_to_records(text):
    reader = csv.DictReader(io.StringIO(text))
    answ = []
    for row in reader:
        answ.append(row)
    return answ

def convert_type(s):
    if all(map(str.isdigit, s)):
        return int(s)
    if all(map(lambda x: (str.isdigit(x) or x == '.'), s)) and s.count('.') == 1:
        return float(s)
    if s in ['true', 'yes']:
        return True
    if s in ['false', 'no']:
        return False
    return s

def parse_settings(lines):
    res = {}
    cur_key = ""
    for line in lines:
        line = line.split('#')[0].strip()
        if line != "":
            if cur_key == "":
                line = line.split(':')
                cur_key = line[0].strip()
                line = line[1].strip()
                if line != "":
                    res[cur_key] = convert_type(line)
                    cur_key = ""
                else:
                    res[cur_key] = []
            else:
                if line.find('-') != -1:
                    res[cur_key].append(line.split('-')[1].strip())
                else:
                    line = line.split(':')
                    cur_key = line[0].strip()
                    line = line[1].strip()
                    if line != "":
                        res[cur_key] = convert_type(line)
                        cur_key = ""
                    else:
                        res[cur_key] = []
    return res

def merge_by_key(rows, extra, key):
    for row in rows:
        if row[key] in extra.keys():
            row.update(extra[row[key]])
    return rows

def records_to_json(records):
    return json.dumps(records, ensure_ascii=False, indent=2, sort_keys=True)

