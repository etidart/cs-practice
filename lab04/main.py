import sys
from stats import average_by_city, read_valid, warmest_city

lines = sys.stdin.read().splitlines()
recs = read_valid(lines)
avg = average_by_city(recs)
warmest = warmest_city(recs)
print(len(recs), len(lines) - len(recs), f'{avg[warmest]:.1f}', sep='\n')
