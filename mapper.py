import sys


def _format_and_split(line, sep='\t'):
    return line.strip().split(sep)


def _emit(elements, sep='\t'):
    elements_as_string = map(str, elements)
    output_string = sep.join(elements_as_string)
    print(output_string)


def mapper():
    for line in sys.stdin:
        line_elements = _format_and_split(line)
        if len(line_elements) < 6:
            continue

        data, time, store, item, cost, payment_method = line_elements
        _emit([store, cost])


if __name__ == '__main__':
    mapper()
