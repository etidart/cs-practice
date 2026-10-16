from logstats import count_levels, top_errors, format_report

log_file = input()
with open(log_file, encoding='utf-8', mode='r') as log:
    lines = 0
    for line in log:
        lines += 1
    print(lines)
    log.seek(0)
    cl = count_levels(log)
    print(cl['ERROR'])
    print(cl['BROKEN'])
    log.seek(0)
    te = top_errors(log, 3)
    with open('report.txt', mode='w+', encoding='utf-8') as report:
        report.write(format_report(cl, te))
