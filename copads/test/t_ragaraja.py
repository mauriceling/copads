'''
Testing Ragaraja Interpreter
Date created: 20th August 2012
Licence: Python Software Foundation License version 2

The tests are executed in sequence from test 1 to test N where the test N 
specific code is added on the the concatenated codes/instructions from the
previous test in the form of

code(N) = code(N-1) + code(N)

Although it is possible to use unittest, it is probably mind-boggling to
try to understand long stretches of codes. It is probably easier to gradually
build up on the code and knowledge/state of the previous instructions. This
means that it is not possible to pass test N but fail test N-1.

Sample test case/scenario capsule -

1: {'restart': False                
    'in_source': '008008008008',    
    'forcedinarray': [0]*10
    'array': [4,0,0,0,0,0,0,0,0,0], 
    'apointer': 0,
    'forcedindata': []
    'inputdata': [],
    'output': [],
    'out_source': '008008008008',
    'spointer': 12
   }
   
containing 10 options:
1. 'restart' - determines if the tester should clear concatenated instructions 
    so far. Default = False, which means keep the clear concatenated 
    instructions so far and add on the current instructions to execute.
    Not used unless to clean out concatenated instructions so far.
2. 'in_source' - the list of specific instructions to execute in this test,
    which will be appended to the list of concatenated instructions so far.
3. 'forcedinarray' - array/tape to be fed into register machine before code
    execution (code = concatenated instructions so far + in_source). If not
    defined, it will be set to [0,0,0,0,0,0,0,0,0,0].
4. 'array' - array/tape at the end of execution.
5. 'apointer' - array pointer at the end of execution.
6. 'forcedindata' - input data list to be fed into register machine before 
    code execution (code = concatenated instructions so far + in_source). 
    If not defined, it will be set to [].
7. 'inputdata' - input data list (defined by 'forcedindata') at the end of
    execution.
8. 'output' - output list at the end of execution.
9. 'out_source': concatenated instructions so far + in_source.
10. 'spointer': source pointer at the end of execution on 'out_source'.
'''

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
            # Testing 080, 116
            22: {'in_source': '009004116080',
                 'array': [7,5,1,0,0,0,0,0,-1,-4],
                 'apointer': 0,
                 'inputdata': [],
                 'output': [237],
                 'out_source': '00800800800800000001101101100400400400401101101\
1011011000000000008008008001009002005010043003044006012032013033004004004061004\
0620160180170190460460811330000840000850000860000970000980041200001210001220040\
04008004008071065068000008115021022047000038042009004116080',
                 'spointer': 264},
            # Testing 077, 087, 089, 088, 090, 094, 095, 096, 105, 108, 109, 117
            23: {'in_source': '077087009089088090094108096109117105095080',
                 'array': [8,5,1,0,0,0,0,0,-1,-4],
                 'apointer': 0,
                 'inputdata': [],
                 'output': [237],
                 'out_source': '00800800800800000001101101100400400400401101101\
1011011000000000008008008001009002005010043003044006012032013033004004004061004\
0620160180170190460460811330000840000850000860000970000980041200001210001220040\
0400800400807106506800000811502102204700003804200900411608007708700908908809009\
4108096109117105095080',
                 'spointer': 306},
            # Testing 091, 092, 093, 099, 100, 101, 102, 103, 104, 112, 113
            24: {'in_source': '000000091093099101092100102103104112113105080',
                 'array': [8,5,50,0,0,0,0,0,-1,-4],
                 'apointer': 2,
                 'inputdata': [],
                 'output': [237],
                 'out_source': '00800800800800000001101101100400400400401101101\
1011011000000000008008008001009002005010043003044006012032013033004004004061004\
0620160180170190460460811330000840000850000860000970000980041200001210001220040\
0400800400807106506800000811502102204700003804200900411608007708700908908809009\
4108096109117105095080000000091093099101092100102103104112113105080',
                 'spointer': 351},
            # Pushing [1,2,3,4,5,6,7,8,9] as input data into the test system
            25: {'in_source': '',
                 'array': [8,5,50,0,0,0,0,0,-1,-4],
                 'apointer': 2,
                 'forcedindata': [1,2,3,4,5,6,7,8,9],
                 'inputdata': [1,2,3,4,5,6,7,8,9],
                 'output': [237],
                 'out_source': '00800800800800000001101101100400400400401101101\
1011011000000000008008008001009002005010043003044006012032013033004004004061004\
0620160180170190460460811330000840000850000860000970000980041200001210001220040\
0400800400807106506800000811502102204700003804200900411608007708700908908809009\
4108096109117105095080000000091093099101092100102103104112113105080',
                 'spointer': 351},
            # Testing 066, 067, 069, 070, 072, 073, 075, 076
            26: {'in_source': '066000067000069000070005000072073076075',
                 'array': [8,5,51,9,1,9,0,0,-1,-4],
                 'apointer': 1,
                 'inputdata': [1,2,3,4,5,6,7,8,9],
                 'output': [237],
                 'out_source': '00800800800800000001101101100400400400401101101\
1011011000000000008008008001009002005010043003044006012032013033004004004061004\
0620160180170190460460811330000840000850000860000970000980041200001210001220040\
0400800400807106506800000811502102204700003804200900411608007708700908908809009\
4108096109117105095080000000091093099101092100102103104112113105080066000067000\
069000070005000072073076075',
                 'spointer': 390},
           }

tests = testdata.keys()
tests.sort()

source = ''

def comparator(data, result):
    if data == result: return 'PASSED:'
    else: return 'FAILED:'
    
for t in tests:
    # ----------------------------
    # ------- PREPARE TEST -------
    # ----------------------------
    
    # Step 1: Check to concatenate source or restart source
    try: 
        if testdata[t]['restart'] == True: source = ''
    except KeyError: pass
     
    isource = source + testdata[t]['in_source']
    
    # Step 2: Get input data list from test (if any)
    try: inputdata = testdata[t]['forcedindata']
    except KeyError: inputdata = []
    
    # Step 3: get pre-execution tape (array) from test (if any)
    try: array = testdata[t]['forcedinarray']
    except KeyError: array = [0]*10
    
    # Step 4: Get expected results after execution
    oarray = testdata[t]['array']            # tape (array) after execution
    oapointer = testdata[t]['apointer']      # tape pointer
    oinputdata = testdata[t]['inputdata']    # input data list
    ooutput = testdata[t]['output']          # output list
    osource = testdata[t]['out_source']      # source
    ospointer = testdata[t]['spointer']      # source pointer
    
    # ----------------------------
    # ------- EXECUTE TEST -------
    # ----------------------------
    
    (array, apointer, inputdata, output, source, spointer) = \
        r.interpret(isource, N.ragaraja, 3, inputdata, array, 10)
    
    # ---------------------------------------------------
    # ------- COMPARE EXPECTED RESULTS AFTER TEST -------
    # ---------------------------------------------------
    
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

# ---------------------------------------------
# --------- TESTING RANDOM OPERATIONS --------- 
# ---------------------------------------------

print
print '===== Testing random operations ====='
print 'Testing 050 051 052 053 054 055 056 057 058 059 060'
print
random_source = '050051052053054055056057058059060'
random_source = random_source + random_source + random_source + \
                random_source + random_source + random_source
for x in range(20):
    tape = r.interpret(random_source, N.ragaraja, 3, [], [0]*10, 10)[0]
    print 'Test #' + str(x+1) + ', Tape: ' + str(tape)
print '===== End of random operations testing ====='

# ---------------------------
# --------- SUMMARY --------- 
# ---------------------------

isource = isource + random_source
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