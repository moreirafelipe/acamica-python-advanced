from mailbox import NotEmptyError
import sys

if len(sys.argv) != 2:
    raise SystemExit('Usage: reading_file.py filename')

filename = sys.argv[1]

account = None
total = 0.0
total_items = 0

with open(filename) as f:
    header = next(f)
    for i, line in enumerate(f):
        line = line.strip()
        parts = line.split(',')
        parts[1] = parts[1].strip('"')
        parts[2] = int(parts[2])
        parts[6] = float(parts[6])

        if account is None:
            account = parts[1]
        
        total_items += parts[2]
        total += parts[2] * parts[6]

print("Account Name: {}".format(account))
print("Total items: {:<5}".format(total_items))
print("Total: {:<10.2f}".format(total))
print("Number of lines processed: {:<5}".format((i+1)))