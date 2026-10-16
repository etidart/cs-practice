def parse_event(line):
    s = line.split()
    if len(s) < 3:
        raise ValueError('not enough parts in log line')
    time, level, message = s[0], s[1], ' '.join(s[2:])
    if not level in ('DEBUG', 'INFO', 'WARNING', 'ERROR'):
        raise ValueError('unknown log level')
    return {'time': time, 'level': level, 'message': message}

def count_levels(lines):
    res = {}
    for line in lines:
        try:
            ev = parse_event(line)
            res[ev['level']] = res.get(ev['level'], 0) + 1
        except ValueError:
            res['BROKEN'] = res.get('BROKEN', 0) + 1
    return res

def top_errors(lines, n):
    res = {}
    for line in lines:
        try:
            ev = parse_event(line)
        except ValueError:
            continue
        if ev['level'] == 'ERROR':
            res[ev['message']] = res.get(ev['message'], 0) + 1
    return sorted(list(res.items()), key=lambda x: (x[1], x[0]), reverse=True)[:n]

def format_report(counts, errors):
    res = "Отчёт по журналу\n\n"
    counts = sorted(list(counts.items()), key=lambda x: x[0])
    for level, count in counts:
        res += f'{level}: {count}\n'
    res += "\nЧастые ошибки:\n"
    for err, count in errors:
        res += f'- {err} — {count}\n'
    return res
