import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.getcwd()), 'copads'))
import n_bf as N

import register_machine as r

testdata = {1: {'in_source': 'AAAA',
                'array': [4,0,0,0,0,0,0,0,0,0],
                'apointer': 0,
                'inputdata': [],
                'output': [],
                'out_source': 'AAAA',
                'spointer': 4},
            2: {'in_source': 'GG',
                'array': [4,0,0,0,0,0,0,0,0,0],
                'apointer': 2,
                'inputdata': [],
                'output': [],
                'out_source': 'AAAAGG',
                'spointer': 6},
            3: {'in_source': 'TTT',
                'array': [4,0,-3,0,0,0,0,0,0,0],
                'apointer': 2,
                'inputdata': [],
                'output': [],
                'out_source': 'AAAAGGTTT',
                'spointer': 9},
            4: {'in_source': 'CCCC',
                'array': [4,0,-3,0,0,0,0,0,0,0],
                'apointer': 8,
                'inputdata': [],
                'output': [],
                'out_source': 'AAAAGGTTTCCCC',
                'spointer': 13},
            5: {'in_source': 'TTTTT',
                'array': [4,0,-3,0,0,0,0,0,-5,0],
                'apointer': 8,
                'inputdata': [],
                'output': [],
                'out_source': 'AAAAGGTTTCCCCTTTTT',
                'spointer': 18},
            6: {'in_source': 'GGG',
                'array': [4,0,-3,0,0,0,0,0,-5,0],
                'apointer': 1,
                'inputdata': [],
                'output': [],
                'out_source': 'AAAAGGTTTCCCCTTTTTGGG',
                'spointer': 21},
            7: {'in_source': 'AAA',
                'array': [4,3,-3,0,0,0,0,0,-5,0],
                'apointer': 1,
                'inputdata': [],
                'output': [],
                'out_source': 'AAAAGGTTTCCCCTTTTTGGGAAA',
                'spointer': 24},
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
        source, spointer) = r.interpret(isource, N.nBF, 1, [], array, 10)
    print(' '.join(['Test number:', str(t), 
                    ', Original source code:', str(source)]))
    print(' '.join(['    ', str(comparator(oarray, array)), 'array.', 
                    'Expected array:', str(oarray),
                    'Actual array:', str(array)]))
    print(' '.join(['    ', str(comparator(oapointer, apointer)), 
                    'array pointer.', 
                    'Expected array pointer:', str(oapointer),
                    'Actual array pointer:', str(apointer)]))
    print(' '.join(['    ', str(comparator(oinputdata, inputdata)), 
                    'input data list.', 
                    'Expected input data list:', str(oinputdata),
                    'Actual input data list:', str(inputdata)]))
    print(' '.join(['    ', str(comparator(ooutput, output)), 
                    'output list.', 
                    'Expected output list:', str(ooutput),
                    'Actual output list:', str(output)]))
    print(' '.join(['    ', str(comparator(osource, source)), 
                    'source code after execution.', 
                    'Expected source:', str(osource),
                    'Actual source:', str(source)]))
    print(' '.join(['    ', str(comparator(ospointer, spointer)), 
                    'source code pointer after execution.', 
                    'Expected source pointer:', str(ospointer),
                    'Actual source pointer:', str(spointer)]))
    print('==========================================================')