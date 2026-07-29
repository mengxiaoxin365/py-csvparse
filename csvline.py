"""Parse a single RFC-4180 CSV line. Standard library only."""


def parse_line(line):
    out, field, in_quotes, i = [], [], False, 0
    while i < len(line):
        c = line[i]
        if in_quotes:
            if c == '"':
                if i + 1 < len(line) and line[i + 1] == '"':
                    field.append('"'); i += 1
                else:
                    in_quotes = False
            else:
                field.append(c)
        elif c == '"':
            in_quotes = True
        elif c == ",":
            out.append("".join(field)); field = []
        else:
            field.append(c)
        i += 1
    out.append("".join(field))
    return out
