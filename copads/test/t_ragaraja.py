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
            # Testing 006, 044
            11: {'in_source': '044006',
                 'array': [4,13,-3,0,0,0,5,0,-5,0],
                 'apointer': 9,
                 'inputdata': [],
                 'output': [],
                 'out_source': '00800800800800000001101101100400400400401101101\
1011011000000000008008008001009002005010043003044006',
                 'spointer': 99},
            # Testing 012, 013, 032, 033
            12: {'in_source': '012032013033',
                 'array': [4,13,-3,0,0,0,5,0,-5,-10],
                 'apointer': 9,
                 'inputdata': [],
                 'output': [],
                 'out_source': '00800800800800000001101101100400400400401101101\
1011011000000000008008008001009002005010043003044006012032013033',
                 'spointer': 111},
            # Testing 061, 062
            13: {'in_source': '004004004061004062',
                 'array': [4,13,-3,0,0,0,5,0,-5,-10],
                 'apointer': 6,
                 'inputdata': [],
                 'output': [],
                 'out_source': '00800800800800000001101101100400400400401101101\
1011011000000000008008008001009002005010043003044006012032013033004004004061004\
062',
                 'spointer': 129},
            # Testing 016, 018
            14: {'in_source': '016018',
                 'array': [4,13,-3,0,0,0,5,0,-5,-10],
                 'apointer': 6,
                 'inputdata': [],
                 'output': [],
                 'out_source': '00800800800800000001101101100400400400401101101\
1011011000000000008008008001009002005010043003044006012032013033004004004061004\
062016018',
                 'spointer': 135},
            # Testing 017, 019
            15: {'in_source': '017019',
                 'array': [4,13,-3,0,0,0,5,0,-5,-10],
                 'apointer': 6,
                 'inputdata': [],
                 'output': [],
                 'out_source': '00800800800800000001101101100400400400401101101\
1011011000000000008008008001009002005010043003044006012032013033004004004061004\
062016018017019',
                 'spointer': 141},
            # Testing 046
            16: {'in_source': '046046',
                 'array': [4,13,-3,0,0,0,5,0,-5,-10],
                 'apointer': 6,
                 'inputdata': [],
                 'output': [],
                 'out_source': '00800800800800000001101101100400400400401101101\
1011011000000000008008008001009002005010043003044006012032013033004004004061004\
062016018017019046046',
                 'spointer': 147},
            # Testing 081, 133
            17: {'in_source': '081133',
                 'array': [4,13,-3,0,0,0,0,-10,-5,5],
                 'apointer': 6,
                 'inputdata': [],
                 'output': [],
                 'out_source': '00800800800800000001101101100400400400401101101\
1011011000000000008008008001009002005010043003044006012032013033004004004061004\
062016018017019046046081133',
                 'spointer': 153},
            # Testing 084, 085, 086
            18: {'in_source': '000084000085000086000097000098',
                 'array': [3.14159265358979323846,2.718281828459045,
                           -3,0,0,0,0,0,-1,1],
                 'apointer': 1,
                 'inputdata': [],
                 'output': [],
                 'out_source': '00800800800800000001101101100400400400401101101\
1011011000000000008008008001009002005010043003044006012032013033004004004061004\
062016018017019046046081133000084000085000086000097000098',
                 'spointer': 183},
            # Testing 120, 121, 122
            19: {'in_source': '004120000121000122',
                 'array': [1,1,1,0,0,0,0,0,-1,1],
                 'apointer': 2,
                 'inputdata': [],
                 'output': [],
                 'out_source': '00800800800800000001101101100400400400401101101\
1011011000000000008008008001009002005010043003044006012032013033004004004061004\
062016018017019046046081133000084000085000086000097000098004120000121000122',
                 'spointer': 201},
            # Testing 065, 068, 071, 115
            20: {'in_source': '004004008004008071065068000008115',
                 'array': [6,1,1,0,0,0,0,0,-1,-4],
                 'apointer': 0,
                 'inputdata': [],
                 'output': [],
                 'out_source': '00800800800800000001101101100400400400401101101\
1011011000000000008008008001009002005010043003044006012032013033004004004061004\
0620160180170190460460811330000840000850000860000970000980041200001210001220040\
04008004008071065068000008115',
                 'spointer': 234},
            # Testing 021, 022, 038, 042, 047
            21: {'in_source': '021022047000038042',
                 'array': [6,0,1,0,0,0,0,0,-1,-4],
                 'apointer': 1,
                 'inputdata': [],
                 'output': [237],
                 'out_source': '00800800800800000001101101100400400400401101101\
1011011000000000008008008001009002005010043003044006012032013033004004004061004\
0620160180170190460460811330000840000850000860000970000980041200001210001220040\
04008004008071065068000008115021022047000038042',
                 'spointer': 252},
           }

tests = testdata.keys()
tests.sort()

source = ''

def comparator(data, result):
    if data == result: return 'PASSED:'
    else: return 'FAILED:'
    
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
    #(array, apointer, inputdata, output, 
    #    source, spointer) = N.interpreter(isource, [], array, 30)
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