def interpret(source, functions,
             function_size=1, inputdata=[],
             array=None, size=30):
    spointer = 0
    apointer = 0
    output = list()
    if array == None:
        array = [0] * size
    if len(array) > size:
        array = array[0:size]
    if len(source) % function_size != 0:
        source = source + '!'*(function_size - \
                               len(source) % function_size)
    tokens = functions.keys()
    source = ''.join([x for x in source if x in tokens])
    while spointer < len(source):
        try:
            token = source[spointer:spointer+function_size]
            (array, apointer, inputdata, output,
                 source, spointer) = functions[token](array, apointer,
                                                      inputdata, output,
                                                      source, spointer)
        except KeyError:
            print ' '.join(['Unknown function: ',
                            source[i:i+function_size],
                            'at source position',
                            str(i)])
        if apointer > size:
            apointer = apointer - size
        if apointer < 0:
            apointer = size + apointer
        spointer = spointer + function_size
    return (array, apointer, inputdata, output, source, spointer)


