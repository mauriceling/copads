'''
One dimensional tape/register machine
Date created: 15th August 2012
Licence: Python Software Foundation License version 2

The machine consists of the following elements:
1. Array/Tape: A circular tape for operations to occur
2. Source: The program
3. Input List: A list of data given to the machine at initialization.
4. Output List: A list of output from the execution. This may also be 
used as a secondary tape. 

When the program terminates, all 4 elements are returned, and the 
machine terminates itself. 
'''

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
            cmd = source[spointer:spointer+function_size]
            #print cmd
            (array, apointer, inputdata, output,
                source, spointer) = functions[cmd](array, apointer,
                                                   inputdata, output,
                                                   source, spointer)
        except KeyError:
            print ' '.join(['Unknown function: ', cmd,
                            'at source position', str(spointer)])
        if apointer > size - 1:
            apointer = apointer - size
        if apointer < 0:
            apointer = size + apointer
        spointer = spointer + function_size
    return (array, apointer, inputdata, output, source, spointer)
