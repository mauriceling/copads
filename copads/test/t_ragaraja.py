import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.getcwd()), 'src'))
import ragaraja as N

import register_machine as r

testdata = {
            # Tests 1-7 are the same tests as for NucleotideBF (t_n_bf.py)
            # Testing 000, 004, 008, 011
            1: {'in_source': '008008008008',
                'array': [4,0,0,0,0,0,0,0,0,0],
                'apointer': 0,
                'inputdata': [],
                'output': [],
                'out_source': '008008008008',
                'spointer': 12},
            2: {'in_source': '000000',
                'array': [4,0,0,0,0,0,0,0,0,0],
                'apointer': 2,
                'inputdata': [],
                'output': [],
                'out_source': '008008008008000000',
                'spointer': 18},
            3: {'in_source': '011011011',
                'array': [4,0,-3,0,0,0,0,0,0,0],
                'apointer': 2,
                'inputdata': [],
                'output': [],
                'out_source': '008008008008000000011011011',
                'spointer': 27},
            4: {'in_source': '004004004004',
                'array': [4,0,-3,0,0,0,0,0,0,0],
                'apointer': 8,
                'inputdata': [],
                'output': [],
                'out_source': '008008008008000000011011011004004004004',
                'spointer': 39},
            5: {'in_source': '011011011011011',
                'array': [4,0,-3,0,0,0,0,0,-5,0],
                'apointer': 8,
                'inputdata': [],
                'output': [],
                'out_source': '008008008008000000011011011004004004004011011011\
011011',
                'spointer': 54},
            6: {'in_source': '000000000',
                'array': [4,0,-3,0,0,0,0,0,-5,0],
                'apointer': 1,
                'inputdata': [],
                'output': [],
                'out_source': '008008008008000000011011011004004004004011011011\
011011000000000',
                'spointer': 63},
            7: {'in_source': '008008008',
                'array': [4,3,-3,0,0,0,0,0,-5,0],
                'apointer': 1,
                'inputdata': [],
                'output': [],
                'out_source': '008008008008000000011011011004004004004011011011\
011011000000000008008008',
                'spointer': 72},
            # Testing 001, 009
            8: {'in_source': '001009',
                'array': [4,3,-3,0,0,0,5,0,-5,0],
                'apointer': 6,
                'inputdata': [],
                'output': [],
                'out_source': '008008008008000000011011011004004004004011011011\
011011000000000008008008001009',
                'spointer': 78},
            # Testing 002, 005
            9: {'in_source': '002005010',
                'array': [4,13,-3,0,0,0,5,0,-5,0],
                'apointer': 1,
                'inputdata': [],
                'output': [],
                'out_source': '008008008008000000011011011004004004004011011011\
011011000000000008008008001009002005010',
                'spointer': 87},
            # Testing 003, 043
            10: {'in_source': '043003',
                 'array': [4,13,-3,0,0,0,5,0,-5,0],
                 'apointer': 6,
                 'inputdata': [],
                 'output': [],
                 'out_source': '00800800800800000001101101100400400400401101101\
1011011000000000008008008001009002005010043003',
                 'spointer': 93},
           }

tests = testdata.keys()
tests.sort()

source = ''

def comparator(data, result):
    if data == result: return 'Passed'
    else: return 'FAILED'
    
for t in tests:
    isource = source + testdata[t]['in_source']
    oarray = testdata[t]['array']
    oapointer = testdata[t]['apointer']
    oinputdata = testdata[t]['inputdata']
    ooutput = testdata[t]['output']
    osource = testdata[t]['out_source']
    ospointer = testdata[t]['spointer']
    array = [0]*10
    (array, apointer, inputdata, output, 
        source, spointer) = r.interpret(isource, N.ragaraja, 3, [], array, 10)
    print ' '.join(['Test number:', str(t), 
                    ', Original source code:', str(isource)])
    print ' '.join(['    ', str(comparator(oarray, array)), 'array.', 
                    'Expected array:', str(oarray),
                    'Actual array:', str(array)])
    print ' '.join(['    ', str(comparator(oapointer, apointer)), 
                    'array pointer.', 
                    'Expected array pointer:', str(oapointer),
                    'Actual array pointer:', str(apointer)])
    print ' '.join(['    ', str(comparator(oinputdata, inputdata)), 
                    'input data list.', 
                    'Expected input data list:', str(oinputdata),
                    'Actual input data list:', str(inputdata)])
    print ' '.join(['    ', str(comparator(ooutput, output)), 
                    'output list.', 
                    'Expected output list:', str(ooutput),
                    'Actual output list:', str(output)])
    print ' '.join(['    ', str(comparator(osource, source)), 
                    'source code after execution.', 
                    'Expected source:', str(osource),
                    'Actual source:', str(source)])
    print ' '.join(['    ', str(comparator(ospointer, spointer)), 
                    'source code pointer after execution.', 
                    'Expected source pointer:', str(ospointer),
                    'Actual source pointer:', str(spointer)])
    print '=========================================================='
    
instruction_set = {}
for i in range(0, len(isource), 3): instruction_set[isource[i:i+3]] = ''
instruction_set = instruction_set.keys()
instruction_set.sort()
print 
print 'Instruction set tested: '
print ' '.join(instruction_set)
print
print 'Number of instructions tested :' + str(len(instruction_set))
print
print '----- End of test -----'