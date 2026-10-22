from pathlib import Path
def count_by_extension(paths):
    res = {}
    for file in paths:
        file = Path(file)
        res[file.suffix[1:]] = res.get(file.suffix[1:], 0) + 1
    return res

def deepest_path(paths):
    res = ''
    for file in paths:
        if file.count('/') > res.count('/'):
            res = file
        elif file.count('/') == res.count('/'):
            if file < res:
                res = file
    return res

def human_size(n):
    i = 0
    did = False
    while n >= 1024:
        n /= 1024
        i += 1
        did = True
    res = f'{n:.1f} ' if did else f'{n} '
    if i == 0:
        res += 'Б'
    elif i == 1:
        res += 'КБ'
    elif i == 2:
        res += 'МБ'
    elif i == 3:
        res += 'ГБ'
    else:
        res += 'ТБ'
    return res

print(human_size(900))
print(human_size(1536))
print(human_size(5 * 1024 * 1024))

