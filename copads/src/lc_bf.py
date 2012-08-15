import register_machine as r

def increment(array, apointer, inputdata, output, source, spointer):
    array[apointer] = array[apointer] + 1
    return (array, apointer, inputdata, output, source, spointer)

def decrement(array, apointer, inputdata, output, source, spointer):
    array[apointer] = array[apointer] - 1
    return (array, apointer, inputdata, output, source, spointer)

def forward(array, apointer, inputdata, output, source, spointer):
    return (array, apointer + 1, inputdata, output, source, spointer)

def backward(array, apointer, inputdata, output, source, spointer):
    return (array, apointer - 1, inputdata, output, source, spointer)

def call_out(array, apointer, inputdata, output, source, spointer):
    output.append(array[apointer])
    return (array, apointer, inputdata, output, source, spointer)

def accept_predefined(array, apointer, inputdata, output, source, spointer):
    if len(inputdata) > 0: array[apointer] = inputdata.pop(0)
    else: array[apointer] = 0
    return (array, apointer, inputdata, output, source, spointer)

def cbf_start_loop(array, apointer, inputdata, output, source, spointer):
    if array[apointer] > 0:
        return (array, apointer, inputdata, output, source, spointer)
    else:
        count = 1
        try:
            while count > 0:
                spointer = spointer + 1
                if source[spointer] == ']':
                    count = count - 1
                if source[spointer] == '[':
                    count = count + 1
        except IndexError:
            spointer = len(source) - 1
    return (array, apointer, inputdata, output, source, spointer)

def cbf_end_loop(array, apointer, inputdata, output, source, spointer):
    temp = spointer
    if array[apointer] < 1:
        return (array, apointer, inputdata, output, source, spointer + 1)
    else:
        count = 1
        try:
            while count > 0:
                spointer = spointer - 1
                if source[spointer] == ']':
                    count = count + 1
                if source[spointer] == '[':
                    count = count - 1
        except IndexError:
            spointer = temp
    return (array, apointer, inputdata, output, source, spointer)

LCBF = {'+': increment,
        '-': decrement,
        '>': forward,
        '<': backward,
        '.': call_out,
        ',': accept_predefined,
        '[': cbf_start_loop,
        ']': cbf_end_loop,
        }

if __name__ == '__main__':
    print r.interpret('++++++++++[>+++++<.-]', LCBF)
    print r.interpret('++[>+++++<.-]>>>+++.', LCBF)
    print r.interpret('++>+++++<.-]>>>+++.', LCBF)
    print r.interpret('++>[+++++<.->>>+++.', LCBF)
    print r.interpret('+++++[>++++[>+++.<-].<-]', LCBF)
