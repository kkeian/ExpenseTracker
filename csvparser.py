def _skip_spaces(line, start_i):
    # skip spaces before an item
    line_len = len(line)
    i = start_i
    while (i < line_len and line[i] == ' '):
        i += 1
    return i


def get_col(line, start_i):
    # return the column item and start index of next column
    i = _skip_spaces(line, start_i)
    line_len = len(line)
    while (i < line_len and line[i] != ','):
        i += 1
    if i == line_len:
        i -= 1 # remove \n - *nix specific
    return (line[start_i:i], i+1)


