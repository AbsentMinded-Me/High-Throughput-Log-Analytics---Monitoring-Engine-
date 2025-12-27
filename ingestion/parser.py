import re

def parse_log_line(line):
    log_pattern = re.compile(r'^(?P<timestamp>\S+ \S+) (?P<level>\S+) (?P<service>\S+) (?P<message>.+)$')
    match = log_pattern.match(line)
    if match:
        return match.groupdict()
    else:
        return None