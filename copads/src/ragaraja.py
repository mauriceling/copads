'''
Ragaraja Interpreter
Date created: 16th August 2012
Licence: Python Software Foundation License version 2

Ragaraja is a derivative and massive extension of Brainfuck. 
This work is influenced by a large number of Brainfuck 
derivatives, other esoteric programming languages, and even 
assembly languages. Probably the most critical difference 
between Ragaraja and other Brainfuck derivatives is the large 
number of commands / instructions - 1000 possible commands / 
instructions, inspired by Nandi (follower of Lord Shiva) who 
was supposed to be the first author of Kama Sutra and wrote it 
in 1000 chapters. 

Etymology: Ragaraja is the name of a Mahayana Buddhist deity 
from Esoteric traditions. The Chinese calls him Ai Ran Ming Wang. 
Ragaraja is one of the Wisdom Kings (a group of Bodhisattvas) 
and represents the state at which sexual excitement or agitation 
can be channeled towards enlightenment and passionate love can 
become compassion for all living things. Hence, I name this 
compilation/derivative/extension of Brainfuck in 1000 
commands/instructions/opcode to signify the epitome, a 
channeling of raw urge to the love and compassion for and 
towards every being. May really be viewed as Brainfuck 
attaining enlightenment or Nirvana. Whoever that can 
remember all 1000 commands and use it, really deserves an award. 

The interpreter environment consists of the following elements:

1. Array/Tape: A circular tape initialized with 30 thousand cells 
each with zero. This can be visualized as a 30,000 cell register 
machine. The number of cells can increase or decrease during runtime.
2. Source: The program
3. Input List: A list of data given to the execution environment at 
initialization.
4. Output List: A list of output from the execution. This may also be 
used as a secondary tape. 

When the program terminates, all 4 elements are returned, and the 
interpreter terminates itself. 

Ref: http://esolangs.org/wiki/Ragaraja
'''
import random
import math
import constants
import register_machine as r
from lc_bf import increment, decrement
from lc_bf import forward, backward
from lc_bf import call_out, accept_predefined
from lc_bf import cbf_start_loop, cbf_end_loop

def tape_move(array, apointer, inputdata, output, source, spointer):
    '''
    Moving tape pointer for more than one increment or decrement.

    Instructions handled:
    001: Move forward by 5 cells on tape. Equivalent to 5 times of 
    "000".
    002: Move forward by 10 cells on tape. Equivalent to 10 times of 
    "000".
    003: Move forward by NxN cells on tape where N is the value of 
    the current cell. If N is a decimal, it will move forward by the 
    floor of NxN. For example, if N is 4.2, this operation will tape 
    pointer forward by 17 cells. As NxN is always a positive number, 
    it does not matter if the value of the current cell is positive 
    or negative.
    005: Move backward by 5 cells on tape. Equivalent to 5 times of 
    "004".
    006: Move backward by 10 cells on tape. Equivalent to 10 times of 
    "004".
    007: Move backward by NxN cells on tape where N is the value of 
    the current cell. This will only work if N is a positive number. 
    If N is a decimal, it will move backward by the floor of NxN. For 
    example, if N is 4.2, this operation will tape pointer backward 
    by 17 cells. 
    043: Move the tape cell pointer to the first cell.
    044: Move the tape cell pointer to the last cell.
    045: Move the tape cell pointer to the location determined by 
    the last value of the output list. For example, the last value 
    of the output list is 5, the tape cell pointer will point to the 
    5th cell on the tape. 
    061: Move forward by the number of cells signified by the current 
    cell.
    062: Move backward by the number of cells signified by the current 
    cell. 
    '''
    cmd = source[spointer:spointer+3]
    if cmd == '001': apointer = apointer + 5
    if cmd == '002': apointer = apointer + 10
    if cmd == '003': 
        move = int(float(array[apointer]) * float(array[apointer]))
        apointer = apointer + move
    if cmd == '005': apointer = apointer - 5
    if cmd == '006': apointer = apointer - 10
    if cmd == '007': 
        move = int(float(array[apointer]) * float(array[apointer]))
        apointer = apointer - move
    if cmd == '043': apointer = 0
    if cmd == '044': apointer = len(array) - 1
    if cmd == '045': apointer = int(output[-1])
    if cmd == '061': 
        apointer = apointer + int(array[apointer])
    if cmd == '062': 
        apointer = apointer - int(array[apointer])
    return (array, apointer, inputdata, output, source, spointer)
	
def accumulations(array, apointer, inputdata, output, source, spointer):
    '''
    Accumulate the tape cell by more than one increment or decrement.
    
    Instructions handled:
    009: Increase value of cell by 5. Equivalent to 5 times of "008".
    010: Increase value of cell by 10. Equivalent to 10 times of "008".
    012: Decrease value of cell by 5. Equivalent to 5 times of "011".
    013: Decrease value of cell by 10. Equivalent to 10 times of "011". 
    032: Double current tape cell value.
    033: Half current tape cell value. 
    '''
    cmd = source[spointer:spointer+3]
    if cmd == '009': 
        array[apointer] = array[apointer] + 5
    if cmd == '010': 
        array[apointer] = array[apointer] + 10
    if cmd == '012': 
        array[apointer] = array[apointer] - 5
    if cmd == '013': 
        array[apointer] = array[apointer] - 10
    if cmd == '032': 
        array[apointer] = 2 * array[apointer]
    if cmd == '033': 
        array[apointer] = 0.5 * array[apointer]
    return (array, apointer, inputdata, output, source, spointer)
	
def nBF_random_op(array, apointer, inputdata, output, source, spointer):
    '''
    NucleotideBF (nBF) random operations - to simulate ambiguous DNA bases.
    
    Instructions handled:
    050: Randomly execute "008" (increment by 1) or "000" (move forward 
    by 1). Equivalent to "R" in NucleotideBF (nBF).
    051: Randomly execute "011" (decrement by 1) or "004" (move backward 
    by 1). Equivalent to "Y" in NucleotideBF (nBF).
    052: Randomly execute "000" (move forward by 1) or "004" (move backward 
    by 1). Equivalent to "S" in NucleotideBF (nBF).
    053: Randomly execute "008" (increment by 1) or "011" (decrement by 1). 
    Equivalent to "W" in NucleotideBF (nBF).
    054: Randomly execute "000" (move forward by 1) or "011" (decrement 
    by 1). Equivalent to "K" in NucleotideBF (nBF).
    055: Randomly execute "004" (move backward by 1) or "008" (increment 
    by 1). Equivalent to "M" in NucleotideBF (nBF).
    056: Randomly execute "000" (move forward by 1) or "004" (move backward 
    by 1) or "011" (decrement by 1). Equivalent to "B" in NucleotideBF (nBF).
    057: Randomly execute "000" (move forward by 1) or "008" (increment by 1) 
    or "011" (decrement by 1). Equivalent to "D" in NucleotideBF (nBF).
    058: Randomly execute "004" (move backward by 1) or "008" (Increment 
    by 1) or "011" (decrement by 1). Equivalent to "H" in NucleotideBF (nBF).
    059: Randomly execute "000" (move forward by 1) or "004" (move backward 
    by 1) or "008" (increment by 1). Equivalent to "V" in NucleotideBF (nBF).
    060: Randomly execute "000" (move forward by 1) or "004" (move backward 
    by 1) or "008" (increment by 1) or "011" (decrement by 1). Equivalent 
    to "N" in NucleotideBF (nBF)
    '''
    cmd = source[spointer:spointer+3]
    r = random.random()
    if cmd == '050' and r < 0.5:
        return increment(array, apointer, inputdata, output, source, spointer)
    elif cmd == '050' and r >= 0.5:
        if (apointer + 1) == len(array): 
            return (array, 0, inputdata, output, source, spointer)
        else:
            return forward(array, apointer, inputdata, output, source, spointer)
    elif cmd == '051' and r < 0.5:
        return decrement(array, apointer, inputdata, output, source, spointer)
    elif cmd == '051' and r >= 0.5:
        if apointer == 0: 
            return (array, len(array) - 1, inputdata, output, source, spointer)
        else:
            return backward(array, apointer, inputdata, output, source, spointer)
    elif cmd == '052' and r < 0.5:
        if (apointer + 1) == len(array): 
            return (array, 0, inputdata, output, source, spointer)
        else:
            return forward(array, apointer, inputdata, output, source, spointer)
    elif cmd == '052' and r >= 0.5:
        if apointer == 0:
            return (array, len(array) - 1, inputdata, output, source, spointer)
        else:
            return backward(array, apointer, inputdata, output, source, spointer)
    elif cmd == '053' and r < 0.5:
        return increment(array, apointer, inputdata, output, source, spointer)
    elif cmd == '053' and r >= 0.5:
        return decrement(array, apointer, inputdata, output, source, spointer)
    elif cmd == '054' and r < 0.5:
        return decrement(array, apointer, inputdata, output, source, spointer)
    elif cmd == '054' and r >= 0.5:
        if (apointer + 1) == len(array): 
            return (array, 0, inputdata, output, source, spointer)
        else:
            return forward(array, apointer, inputdata, output, source, spointer)
    elif cmd == '055' and r < 0.5:
        return increment(array, apointer, inputdata, output, source, spointer)
    elif cmd == '055' and r >= 0.5:
        if apointer == 0: 
            return (array, len(array) - 1, inputdata, output, source, spointer)
        else:
            return backward(array, apointer, inputdata, output, source, spointer)
    elif cmd == '056' and r < 0.33:
        if (apointer + 1) == len(array): 
            return (array, 0, inputdata, output, source, spointer)
        else:
            return forward(array, apointer, inputdata, output, source, spointer)
    elif cmd == '056' and r >= 0.33 and r < 0.67:
        return decrement(array, apointer, inputdata, output, source, spointer)
    elif cmd == '056' and r >= 0.67:
        if apointer == 0:
            return (array, len(array) - 1, inputdata, output, source, spointer)
        else:
            return backward(array, apointer, inputdata, output, source, spointer)
    elif cmd == '057' and r < 0.33:
        return increment(array, apointer, inputdata, output, source, spointer)
    elif cmd == '057' and r >= 0.33 and r < 0.67:
        return decrement(array, apointer, inputdata, output, source, spointer)
    elif cmd == '057' and r >= 0.67:
        if (apointer + 1) == len(array):
            return (array, 0, inputdata, output, source, spointer)
        else:
            return forward(array, apointer, inputdata, output, source, spointer)
    elif cmd == '058' and r < 0.33:
        return increment(array, apointer, inputdata, output, source, spointer)
    elif cmd == '058' and r >= 0.33 and r < 0.67:
        return decrement(array, apointer, inputdata, output, source, spointer)
    elif cmd == '058' and r >= 0.67:
        if apointer == 0:
            return (array, len(array) - 1, inputdata, output, source, spointer)
        else:
            return backward(array, apointer, inputdata, output, source, spointer)
    elif cmd == '059' and r < 0.33:
        return increment(array, apointer, inputdata, output, source, spointer)
    elif cmd == '059' and r >= 0.33 and r < 0.67:
        if (apointer + 1) == len(array):
            return (array, 0, inputdata, output, source, spointer)
        else:
            return forward(array, apointer, inputdata, output, source, spointer)
    elif cmd == '059' and r >= 0.67:
        if apointer == 0:
            return (array, len(array) - 1, inputdata, output, source, spointer)
        else:
            return backward(array, apointer, inputdata, output, source, spointer)
    elif cmd == '060' and r < 0.25:
        return increment(array, apointer, inputdata, output, source, spointer)
    elif cmd == '060' and r >= 0.25 and r < 0.5:
        return decrement(array, apointer, inputdata, output, source, spointer)
    elif cmd == '060' and r >= 0.5 and r < 0.75:
        if (apointer + 1) == len(array): 
            return (array, 0, inputdata, output, source, spointer)
        else:
            return forward(array, apointer, inputdata, output, source, spointer)
    elif cmd == '060' and r >= 0.75:
        if apointer == 0:
            return (array, len(array) - 1, inputdata, output, source, spointer)
        else:
            return backward(array, apointer, inputdata, output, source, spointer)

def tape_size(array, apointer, inputdata, output, source, spointer):
    '''
    Change the length of the tape during runtime.
    
    Instructions handled:
    016: Add one cell to the end of the tape.
    017: Add 10 cells to the end of the tape.
    018: Remove one cell from the end of the tape. If original tape pointer 
    is at the last cell before removal operation, the tape pointer will point 
    to the last cell after removal.
    019: Remove 10 cells from the end of the tape. If original tape pointer 
    is at the last cell before removal operation, the tape pointer will point 
    to the last cell after removal.
    034: Insert a cell after the current tape cell. For example, if current 
    tape cell is 35, a cell initialized to zero will be added as cell 36. As 
    a result, the tape is 1 cell longer.
    035: Delete the current cell. As a result, the tape is 1 cell shorter.
    036: Delete the current and append to the end of the output list. As a 
    result, the tape is 1 cell shorter. 
    '''
    cmd = source[spointer:spointer+3]
    if cmd == '016': array = array + [0]
    if cmd == '017': array = array + [0]*10
    if cmd == '018': array = array[:-1]
    if cmd == '019': array = array[:-10]
    if cmd == '034': array.insert(apointer + 1, 0)
    if cmd == '035': array.pop(apointer)
    if cmd == '036': output.append(array.pop(apointer))
    if apointer >= len(array): apointer = len(array) - 1
    return (array, apointer, inputdata, output, source, spointer)
    
def source_move(array, apointer, inputdata, output, source, spointer):
    '''
    Moving the source without execution.
    
    Instructions handled:
    023: Move source pointer forward by one instruction without execution 
    if the source pointer does not point beyond the length of the source 
    after the move, otherwise, does not move the source pointer.
    024: Move source pointer forward by 5 instruction without execution 
    if the source pointer does not point beyond the length of the source 
    after the move, otherwise, does not move the source pointer.
    025: Move source pointer forward by 10 instruction without execution 
    if the source pointer does not point beyond the length of the source 
    after the move, otherwise, does not move the source pointer.
    026: Move source pointer backward by one instruction without execution 
    if the source pointer does not point beyond the length of the source 
    after the move, otherwise, does not move the source pointer.
    027: Move source pointer backward by 5 instruction without execution 
    if the source pointer does not point beyond the length of the source 
    after the move, otherwise, does not move the source pointer.
    028: Move source pointer backward by 10 instruction without execution 
    if the source pointer does not point beyond the length of the source 
    after the move, otherwise, does not move the source pointer. 
    082: Skip next instruction if current cell is "0". Equivalent to "/" 
    in [[Minimal]]. However, this operation will only execute if there is 
    at least 1 more instruction from the current instruction.
    083: Skip the number of instructions equivalent to the absolute integer 
    value of the current cell if the source pointer does not point beyond 
    the length of the source after the move, otherwise, does not move the 
    source pointer. For example, if current cell is "5.6" or "5", the next 
    5 instructions will be skipped.
    '''
    cmd = source[spointer:spointer+3]
    if cmd == '023' and (spointer + 3) < len(source):
        spointer = spointer + 3
    if cmd == '024' and (spointer + 15) < len(source):
        spointer = spointer + 15
    if cmd == '025' and (spointer + 30) < len(source):
        spointer = spointer + 30
    if cmd == '026' and (spointer - 3) >= 0:
        spointer = spointer - 3
    if cmd == '027' and (spointer - 15) >= 0:
        spointer = spointer - 15
    if cmd == '028' and (spointer - 30) >= 0:
        spointer = spointer - 30
    if cmd == '082' and array[apointer] == 0 and \
    (spointer + 3) <= len(source):
        spointer = spointer + 3
    if cmd == '083' and \
    (spointer + (3 * abs(int(array[apointer])))) < len(source):
        spointer = spointer + (3 * abs(int(array[apointer])))
    return (array, apointer, inputdata, output, source, spointer)
    
def set_tape_value(array, apointer, inputdata, output, source, spointer):
    '''
    Set values into tape cell by over-writing the original value.
    
    Instructions handled:
    084: Set current tape cell to "0".
    085: Set current tape cell to "-1".
    086: Set current tape cell to "1". 
    097: Set the value of the current cell to pi (3.14159265358979323846)
    098: Set the value of the current cell to e (2.718281828459045) 
    '''
    cmd = source[spointer:spointer+3]
    if cmd == '084': array[apointer] = 0
    if cmd == '085': array[apointer] = -1
    if cmd == '086': array[apointer] = 1
    if cmd == '097': array[apointer] = constants.PI
    if cmd == '098': array[apointer] = math.e
    return (array, apointer, inputdata, output, source, spointer)
    
def mathematics(array, apointer, inputdata, output, source, spointer):
    '''
    Performs mathematical and arithmetical operations.
    
    Instructions handled:
    065: Add the value of the current cell (n) and (n+1)th cell, and 
    store the value in the current cell. Array[n] = Array[n] + Array[n+1]
    066: Add the value of the current cell (n) and first of the input 
    list, and store the value in the current cell.
    067: Add the value of the current cell (n) and last of the input 
    list, and store the value in the current cell.
    068: Subtract the value of the current cell (n) from (n+1)th 
    cell, and store the value in the current cell. 
    Array[n] = Array[n+1] - Array[n]
    069: Subtract the value of the current cell (n) from the first 
    of the input list, and store the value in the current cell. 
    Array[n] = InputList[0] - Array[n]
    070: Subtract the value of the current cell (n) from the last 
    of the input list, and store the value in the current cell. 
    Array[n] = InputList[-1] - Array[n]
    071: Multiply the value of the current cell (n) and (n+1)th 
    cell, and store the value in the current cell. 
    Array[n] = Array[n+1] * Array[n]
    072: Multiply the value of the current cell (n) and first of 
    the input list, and store the value in the current cell.
    073: Multiply the value of the current cell (n) and last of 
    the input list, and store the value in the current cell.
    074: Divide the value of the current cell (n) from (n+1)th 
    cell, and store the value in the current cell. 
    Array[n] = Array[n+1] / Array[n]
    075: Divide the value of the current cell (n) from the first 
    of the input list, and store the value in the current cell. 
    Array[n] = InputList[0] / Array[n]
    076: Divide the value of the current cell (n) from the last 
    of the input list, and store the value in the current cell. 
    Array[n] = InputList[-1] - Array[n]
    077: Modulus (remainder after division) the value of the 
    current cell (n) from (n+1)th cell, and store the value in 
    the current cell. Array[n] = Array[n+1] % Array[n]
    078: Modulus (remainder after division) the value of the 
    current cell (n) from the first of the input list, and store 
    the value in the current cell. Array[n] = InputList[0] % Array[n]
    079: Modulus (remainder after division) the value of the 
    current cell (n) from the last of the input list, and store 
    the value in the current cell. Array[n] = InputList[-1] % Array[n]
    080: Floor the value of the current cell. For example, if 
    the value of the current cell is 6.7, it will becomes 6.
    087: Negate the value of the current cell. Positive value will be 
    negative. Negative value will be positive. Equivalent to "_" in L00P
    088: Calculate the sine of the value of the current cell (measured 
    in radians) and replace. Equivalent to "s" in Grin. 
    Array[n] = sine(Array[n])
    089: Calculate the cosine of the value of the current cell 
    (measured in radians) and replace. Equivalent to "c" in Grin. 
    Array[n] = cosine(Array[n])
    090: Calculate the tangent of the value of the current cell 
    (measured in radians) and replace. Equivalent to "t" in Grin. 
    Array[n] = tangent(Array[n])
    091: Calculate the arc sine of the value of the current cell 
    (measured in radians) and replace. Equivalent to "S" in Grin. 
    Array[n] = arcsine(Array[n])
    092: Calculate the arc cosine of the value of the current cell 
    (measured in radians) and replace. Equivalent to "C" in Grin. 
    Array[n] = arccosine(Array[n])
    093: Calculate the arc tangent of the value of the current cell 
    (measured in radians) and replace. Equivalent to "T" in Grin. 
    Array[n] = arctangent(Array[n])
    094: Calculate the reciprocal of the value of the current cell 
    (measured in radians) and replace. Equivalent to "1" in Grin. 
    Array[n] = 1/Array[n]
    095: Calculate the square root of the value of the current cell 
    (measured in radians) and replace. Equivalent to "q" in Grin. 
    Array[n] = sqrt(Array[n])
    096: Calculate the natural logarithm of the value of the current 
    cell (measured in radians) and replace. Equivalent to "l" in Grin. 
    Array[n] = ln(Array[n])
    099: Calculate the hyperbolic sine of the value of the current 
    cell (measured in radians) and replace. Array[n] = sinh(Array[n])
    100: Calculate the hyperbolic cosine of the value of the current 
    cell (measured in radians) and replace. Array[n] = cosh(Array[n])
    101: Calculate the hyperbolic tangent of the value of the current 
    cell (measured in radians) and replace. Array[n] = tanh(Array[n])
    102: Calculate the hyperbolic arc sine of the value of the current 
    cell (measured in radians) and replace. Array[n] = arcsinh(Array[n])
    103: Calculate the hyperbolic arc cosine of the value of the current 
    cell (measured in radians) and replace. Array[n] = arccosh(Array[n])
    104: Calculate the hyperbolic arc tangent of the value of the 
    current cell (measured in radians) and replace. 
    Array[n] = arctanh(Array[n])
    105: Convert the value of the current cell (measured in radians) to 
    degrees and replace.
    106: Convert the value of the current cell (measured in degrees) to 
    radians and replace.
    107: Raise the value of the current cell (n) to e, and store the 
    value in the current cell. Array[n] = Array[n]^e
    108: Raise e to the value of the current cell (n), and store the 
    value in the current cell. Array[n] = e^Array[n]
    109: Raise 10 to the value of the current cell (n), and store the 
    value in the current cell. Array[n] = 10^Array[n]
    110: Raise the value of the current cell (n) to the value of (n+1)th 
    cell, and store the value in the current cell. 
    Array[n] = Array[n]^Array[n+1]
    111: Calculate the n-th root of the value of the current cell (n) 
    where n is the value of (n+1)th cell, and store the value in the 
    current cell. Array[n] = Array[n]^(1/Array[n+1])
    112: Calculate the error function of the value of the current cell 
    and replace. Array[n] = erf(Array[n])
    113: Calculate the complementary error function of the value of the 
    current cell and replace. Array[n] = erfc(Array[n])
    114: Calculate the factorial of the integer value of the current 
    cell (if the integer value is positive) and replace. 
    Array[n] = factorial(Array[n])
    115: Calculate the factorial of the absolute integer value of the 
    current cell and replace. Array[n] = factorial(abs(Array[n]))
    116: Calculate the Euclidean distance (hypotenuse) value of the 
    current cell (n) to the value of (n+1)th cell, and store the value 
    in the current cell. 
    Array[n] = sqrt(Array[n]*Array[n] + Array[n+1]*Array[n+1])
    117: Calculate the logarithm value of the current cell (n) to the
    base of the value of (n+1)th cell, and store the value in the current 
    cell. Array[n] = log(Array[n], base=Array[n+1])
    '''
    cmd = source[spointer:spointer+3]
    if cmd == '065':
        if (apointer + 1) < len(array):
            array[apointer] = array[apointer] + array[apointer+1]
        else:
            array[apointer] = array[apointer] + array[0]
    if cmd == '066' and len(inputdata) > 0:
        array[apointer] = array[apointer] + inputdata[0]
    if cmd == '067' and len(inputdata) > 0:
        array[apointer] = array[apointer] + inputdata[-1]
    if cmd == '068':
        if (apointer + 1) < len(array):
            array[apointer] = array[apointer+1] - array[apointer]
        else:
            array[apointer] = array[0] - array[apointer]
    if cmd == '069' and len(inputdata) > 0:
        array[apointer] = inputdata[0] - array[apointer]
    if cmd == '070' and len(inputdata) > 0:
        array[apointer] = inputdata[-1] - array[apointer]
    if cmd == '071': 
        if (apointer + 1) < len(array):
            array[apointer] = array[apointer+1] * array[apointer]
        else:
            array[apointer] = array[0] * array[apointer]
    if cmd == '072' and len(inputdata) > 0:
        array[apointer] = inputdata[0] * array[apointer]
    if cmd == '073' and len(inputdata) > 0:
        array[apointer] = inputdata[-1] * array[apointer]
    if cmd == '074':
        if (apointer + 1) < len(array):
            array[apointer] = array[apointer+1] / array[apointer]
        else:
            array[apointer] = array[0] / array[apointer]
    if cmd == '075' and len(inputdata) > 0:
        array[apointer] = inputdata[0] / array[apointer]
    if cmd == '076' and len(inputdata) > 0:
        array[apointer] = inputdata[-1] / array[apointer]
    if cmd == '077':
        if (apointer + 1) < len(array):
            array[apointer] = array[apointer+1] % array[apointer]
        else:
            array[apointer] = array[0] % array[apointer]
    if cmd == '078' and len(inputdata) > 0:
        array[apointer] = inputdata[0] % array[apointer]
    if cmd == '079' and len(inputdata) > 0:
        array[apointer] = inputdata[-1] % array[apointer]
    if cmd == '080':
        array[apointer] = int(array[apointer])
    if cmd == '087':
        array[apointer] = -1 * array[apointer]
    if cmd == '088':
        array[apointer] = math.sin(array[apointer])
    if cmd == '089':
        array[apointer] = math.cos(array[apointer])
    if cmd == '090':
        array[apointer] = math.tan(array[apointer])
    if cmd == '091':
        array[apointer] = math.asin(array[apointer])
    if cmd == '092':
        array[apointer] = math.acos(array[apointer])
    if cmd == '093':
        array[apointer] = math.atan(array[apointer])
    if cmd == '094':
        array[apointer] = 1 / array[apointer]
    if cmd == '095':
        array[apointer] = math.sqrt(array[apointer])
    if cmd == '096':
        array[apointer] = math.log(array[apointer], math.e)
    if cmd == '099':
        array[apointer] = math.sinh(array[apointer])
    if cmd == '100':
        array[apointer] = math.cosh(array[apointer])
    if cmd == '101':
        array[apointer] = math.tanh(array[apointer])
    if cmd == '102':
        array[apointer] = math.asinh(array[apointer])
    if cmd == '103':
        array[apointer] = math.acosh(array[apointer])
    if cmd == '104':
        array[apointer] = math.atanh(array[apointer])
    if cmd == '105':
        array[apointer] = math.degrees(array[apointer])
    if cmd == '106':
        array[apointer] = math.radians(array[apointer])
    if cmd == '107':
        array[apointer] = array[apointer] ** math.e
    if cmd == '108':
        array[apointer] = math.e ** array[apointer]
    if cmd == '109':
        array[apointer] = 10 ** array[apointer]
    if cmd == '110': 
        if (apointer + 1) < len(array):
            array[apointer] = array[apointer] ** array[apointer+1]
        else:
            array[apointer] = array[apointer] ** array[0]
    if cmd == '111':
        if (apointer + 1) < len(array):
            array[apointer] = array[apointer] ** (1 / array[apointer+1])
        else:
            array[apointer] = array[apointer] ** (1 / array[0])
    if cmd == '112':
        array[apointer] = math.erf(array[apointer])
    if cmd == '113':
        array[apointer] = math.erfc(array[apointer])
    if cmd == '114' and array[apointer] >= 0:
        array[apointer] = math.factorial(int(array[apointer]))
    if cmd == '115':
        array[apointer] = math.factorial(abs(int(array[apointer])))
    if cmd == '116':
        if (apointer + 1) < len(array):
            array[apointer] = math.hypot(array[apointer], array[apointer+1])
        else:
            array[apointer] = math.hypot(array[apointer], array[0])    
    if cmd == '117':
        if (apointer + 1) < len(array):
            array[apointer] = math.log(array[apointer], array[apointer+1])
        else:
            array[apointer] = math.log(array[apointer], array[0])
    return (array, apointer, inputdata, output, source, spointer)
    
def output_IO(array, apointer, inputdata, output, source, spointer):
    '''
    Using output list as output storage or secondary tape, write and 
    accept values from output list.
    
    Instructions handled:
    021: Output current tape cell location and append to the end of 
    the output list.
    022: Output current source location and append to the end of the 
    output list. 
    037: Replace the current tape cell value with the last value of 
    the output list, and delete the last value from the output list.
    038: Replace the current tape cell value with the last value of 
    the output list, without deleting the last value from the output 
    list.
    039: Replace the current tape cell value with the first value of 
    the output list, and delete the first value from the output list.
    040: Replace the current tape cell value with the first value of 
    the output list, without deleting the first value from the output 
    list.
    041: Remove first value from the output list.
    042: Remove last value from the output list. 
    '''
    cmd = source[spointer:spointer+3]
    if cmd == '021': output.append(apointer)
    if cmd == '022': output.append(spointer)
    if cmd == '037' and len(output) > 0:
        array[apointer] = output.pop(-1)
    if cmd == '038' and len(output) > 0:
        array[apointer] = output[-1]
    if cmd == '039' and len(output) > 0:
        array[apointer] = output.pop(0)
    if cmd == '040' and len(output) > 0:
        array[apointer] = output[0]
    if cmd == '041' and len(output) > 0: output.pop(0)
    if cmd == '042' and len(output) > 0: output.pop(-1)
    return (array, apointer, inputdata, output, source, spointer)

def logic(array, apointer, inputdata, output, source, spointer):
    '''
    Logical operations
    
    Instructions handled:
    120: AND operator: Given positive numbers (>0) as True and zero 
    or negative numbers (<=0) as False, store Array[current] AND 
    Array[current+1] in the current cell (Array[current]) where "0" 
    is False and "1" is True.
    121: OR operator: Given positive numbers (>0) as True and zero 
    or negative numbers (<=0) as False, store Array[current] OR 
    Array[current+1] in the current cell (Array[current]) where "0" 
    is False and "1" is True.
    122: NOT operator: Given positive numbers (>0) as True and zero 
    or negative numbers (<=0) as False, store NOT Array[current] in 
    the current cell (Array[current]) where "0" is False and "1" is 
    True.
    123: LESS-THAN operator: Store Array[current] < Array[current+1] 
    in the current cell (Array[current]) where "0" is False and "1" 
    is True.
    124: MORE-THAN operator: Store Array[current] > Array[current+1] 
    in the current cell (Array[current]) where "0" is False and "1" 
    is True.
    125: EQUAL operator: Store Array[current] = Array[current+1] in 
    the current cell (Array[current]) where "0" is False and "1" is 
    True.
    126: NOT-EQUAL operator: Store Array[current] != Array[current+1] 
    in the current cell (Array[current]) where "0" is False and "1" 
    is True.
    127: LESS-THAN-OR-EQUAL operator: Store Array[current] 
    <= Array[current+1] in the current cell (Array[current]) where 
    "0" is False and "1" is True.
    128: MORE-THAN-OR-EQUAL operator: Store Array[current] => 
    Array[current+1] in the current cell (Array[current]) where "0" 
    is False and "1" is True.
    129: NAND operator: Given positive numbers (>0) as True and 
    zero or negative numbers (<=0) as False, store Array[current] 
    NAND Array[current+1] in the current cell (Array[current]) 
    where "0" is False and "1" is True. Array[current] NAND 
    Array[current+1] is equivalent to NOT (Array[current] AND 
    Array[current+1])
    130: NOR operator: Given positive numbers (>0) as True and 
    zero or negative numbers (<=0) as False, store Array[current] 
    NOR Array[current+1] in the current cell (Array[current]) where 
    "0" is False and "1" is True. Array[current] NOR Array[current+1] 
    is equivalent to NOT (Array[current] OR Array[current+1])
    '''
    cmd = source[spointer:spointer+3]
    xValue = array[apointer]
    if array[apointer] > 0: x = True
    else: x = False
    if (apointer + 1) < len(array):
        yValue = array[apointer+1]
        if array[apointer+1] > 0: y = True
        else: y = False
    else:
        yValue = array[0]
        if array[0] > 0: y = True
        else: y = False
    if cmd == '120': 
        if (x and y) == True: array[apointer] = 1
        else: array[apointer] = 0
    if cmd == '121': 
        if (x or y) == True: array[apointer] = 1
        else: array[apointer] = 0
    if cmd == '122': 
        if not x == True: array[apointer] = 1
        else: array[apointer] = 0
    if cmd == '123': 
        if xValue < yValue: array[apointer] = 1
        else: array[apointer] = 0
    if cmd == '124': 
        if xValue > yValue: array[apointer] = 1
        else: array[apointer] = 0
    if cmd == '125': 
        if xValue == yValue: array[apointer] = 1
        else: array[apointer] = 0
    if cmd == '126': 
        if xValue != yValue: array[apointer] = 1
        else: array[apointer] = 0
    if cmd == '127': 
        if xValue <= yValue: array[apointer] = 1
        else: array[apointer] = 0
    if cmd == '128': 
        if xValue >= yValue: array[apointer] = 1
        else: array[apointer] = 0
    if cmd == '129': 
        if (not (x and y)) == True: array[apointer] = 1
        else: array[apointer] = 0
    if cmd == '130': 
        if (not (x or y)) == True: array[apointer] = 1
        else: array[apointer] = 0
    return (array, apointer, inputdata, output, source, spointer)

def flipping(array, apointer, inputdata, output, source, spointer):
    '''
    Flipping of execution elements.
    
    Instructions handled:
    046: Flip the tape. The original first cell becomes the last 
    cell but the tape pointer does not flip in location.
    047: Flip the output list.
    048: Flip the instruction list (source) but the source pointer 
    does not flip in location.
    '''
    cmd = source[spointer:spointer+3]
    if cmd == '046': array.reverse()
    if cmd == '047': output.reverse()
    if cmd == '048': source = source[::-1]
    return (array, apointer, inputdata, output, source, spointer)

def input_IO(array, apointer, inputdata, output, source, spointer):
    '''
    Write to and accept values from input list.
    
    Instructions handled:
    064: Writes the first value of the input list into the current 
    cell and without removing the value from the input list. If 
    input list is empty, "0" will be written. 
    '''
    cmd = source[spointer:spointer+3]
    if cmd == '064':
        if len(inputdata) == 0: array[apointer] = 0
        else: array[apointer] = inputdata[0]
    return (array, apointer, inputdata, output, source, spointer)

def tape_manipulate(array, apointer, inputdata, output, source, spointer):
    '''
    Manipulating the tape.
    
    Instructions handled:
    081: Swap the value of the current cell (n) and (n+1)th cell. 
    133: Flip the tape from the cell after the current cell to the end of the 
    tape (temporarily breaking the circularity of the tape).
    '''
    cmd = source[spointer:spointer+3]
    if cmd == '081':
        if (apointer + 1) < len(array):
            temp = array[apointer]
            array[apointer] = array[apointer+1]
            array[apointer+1] = temp
        else:
            temp = array[apointer]
            array[apointer] = array[0]
            array[0] = temp
    if cmd == '133' and (apointer + 1) < len(array):
        temp = array[apointer+1:]
        array = array[0:apointer+1]
        temp.reverse()
        array = array + temp
    return (array, apointer, inputdata, output, source, spointer)
    
def source_manipulate(array, apointer, inputdata, output, source, spointer):
    '''
    Manipulating the source instructions.
    
    Instructions handled:
    '''
    cmd = source[spointer:spointer+3]
    if cmd == 'xxx': pass
    return (array, apointer, inputdata, output, source, spointer)
    
def interpreter_manipulate(array, apointer, inputdata, output, source, spointer):
    '''
    Manipulating the interpreter.
    
    Instructions handled:
    '''
    cmd = source[spointer:spointer+3]
    if cmd == 'xxx': pass
    return (array, apointer, inputdata, output, source, spointer)
    
def not_used(array, apointer, inputdata, output, source, spointer):
    '''
    
    Instructions handled:
    '''
    cmd = source[spointer:spointer+3]
    if cmd == 'xxx': pass
    return (array, apointer, inputdata, output, source, spointer)

ragaraja = {'000': forward, '001': tape_move,
            '002': tape_move, '003': tape_move,
            '004': backward, '005': tape_move,
            '006': tape_move, '007': tape_move,
            '008': increment, '009': accumulations,
            '010': accumulations, '011': decrement,
            '012': accumulations, '013': accumulations,
            '014': cbf_start_loop, '015': cbf_end_loop,
            '016': tape_size, '017': tape_size,
            '018': tape_size, '019': tape_size,
            '020': call_out, '021': output_IO,
            '022': output_IO, '023': source_move,
            '024': source_move, '025': source_move,
            '026': source_move, '027': source_move,
            '028': source_move, '029': not_used,
            '030': not_used, '031': not_used,
            '032': accumulations, '033': accumulations,
            '034': tape_size, '035': tape_size,
            '036': tape_size, '037': output_IO,
            '038': output_IO, '039': output_IO,
            '040': output_IO, '041': output_IO,
            '042': output_IO, '043': tape_move,
            '044': tape_move, '045': tape_move,
            '046': flipping, '047': flipping,
            '048': flipping, '049': not_used,
            '050': nBF_random_op, '051': nBF_random_op,
            '052': nBF_random_op, '053': nBF_random_op,
            '054': nBF_random_op, '055': nBF_random_op,
            '056': nBF_random_op, '057': nBF_random_op,
            '058': nBF_random_op, '059': nBF_random_op,
            '060': nBF_random_op, '061': tape_move,
            '062': tape_move, '063': accept_predefined,
            '064': input_IO, '065': mathematics,
            '066': mathematics, '067': mathematics,
            '068': mathematics, '069': mathematics,
            '070': mathematics, '071': mathematics,
            '072': mathematics, '073': mathematics,
            '074': mathematics, '075': mathematics,
            '076': mathematics, '077': mathematics,
            '078': mathematics, '079': mathematics,
            '080': mathematics, '081': tape_manipulate,
            '082': source_move, '083': source_move,
            '084': set_tape_value, '085': set_tape_value,
            '086': set_tape_value, '087': mathematics,
            '088': mathematics, '089': mathematics,
            '090': mathematics, '091': mathematics,
            '092': mathematics, '093': mathematics,
            '094': mathematics, '095': mathematics,
            '096': mathematics, '097': set_tape_value,
            '098': set_tape_value, '099': mathematics,
            '100': mathematics, '101': mathematics,
            '102': mathematics, '103': mathematics,
            '104': mathematics, '105': mathematics,
            '106': mathematics, '107': mathematics,
            '108': mathematics, '109': mathematics,
            '110': mathematics, '111': mathematics,
            '112': mathematics, '113': mathematics,
            '114': mathematics, '115': mathematics,
            '116': mathematics, '117': mathematics,
            '118': not_used, '119': not_used,
            '120': logic, '121': logic,
            '122': logic, '123': logic,
            '124': logic, '125': logic,
            '126': logic, '127': logic,
            '128': logic, '129': logic,
            '130': logic, '131': not_used,
            '132': not_used, '133': tape_manipulate,
            '134': not_used, '135': not_used,
            '136': not_used, '137': not_used,
            '138': not_used, '139': not_used,
            '140': not_used, '141': not_used,
            '142': not_used, '143': not_used,
            '144': not_used, '145': not_used,
            '146': not_used, '147': not_used,
            '148': not_used, '149': not_used,
            '150': not_used, '151': not_used,
            '152': not_used, '153': not_used,
            '154': not_used, '155': not_used,
            '156': not_used, '157': not_used,
            '158': not_used, '159': not_used,
            '160': not_used, '161': not_used,
            '162': not_used, '163': not_used,
            '164': not_used, '165': not_used,
            '166': not_used, '167': not_used,
            '168': not_used, '169': not_used,
            '170': not_used, '171': not_used,
            '172': not_used, '173': not_used,
            '174': not_used, '175': not_used,
            '176': not_used, '177': not_used,
            '178': not_used, '179': not_used,
            '180': not_used, '181': not_used,
            '182': not_used, '183': not_used,
            '184': not_used, '185': not_used,
            '186': not_used, '187': not_used,
            '188': not_used, '189': not_used,
            '190': not_used, '191': not_used,
            '192': not_used, '193': not_used,
            '194': not_used, '195': not_used,
            '196': not_used, '197': not_used,
            '198': not_used, '199': not_used,
            '200': not_used, '201': not_used,
            '202': not_used, '203': not_used,
            '204': not_used, '205': not_used,
            '206': not_used, '207': not_used,
            '208': not_used, '209': not_used,
            '210': not_used, '211': not_used,
            '212': not_used, '213': not_used,
            '214': not_used, '215': not_used,
            '216': not_used, '217': not_used,
            '218': not_used, '219': not_used,
            '220': not_used, '221': not_used,
            '222': not_used, '223': not_used,
            '224': not_used, '225': not_used,
            '226': not_used, '227': not_used,
            '228': not_used, '229': not_used,
            '230': not_used, '231': not_used,
            '232': not_used, '233': not_used,
            '234': not_used, '235': not_used,
            '236': not_used, '237': not_used,
            '238': not_used, '239': not_used,
            '240': not_used, '241': not_used,
            '242': not_used, '243': not_used,
            '244': not_used, '245': not_used,
            '246': not_used, '247': not_used,
            '248': not_used, '249': not_used,
            '250': not_used, '251': not_used,
            '252': not_used, '253': not_used,
            '254': not_used, '255': not_used,
            '256': not_used, '257': not_used,
            '258': not_used, '259': not_used,
            '260': not_used, '261': not_used,
            '262': not_used, '263': not_used,
            '264': not_used, '265': not_used,
            '266': not_used, '267': not_used,
            '268': not_used, '269': not_used,
            '270': not_used, '271': not_used,
            '272': not_used, '273': not_used,
            '274': not_used, '275': not_used,
            '276': not_used, '277': not_used,
            '278': not_used, '279': not_used,
            '280': not_used, '281': not_used,
            '282': not_used, '283': not_used,
            '284': not_used, '285': not_used,
            '286': not_used, '287': not_used,
            '288': not_used, '289': not_used,
            '290': not_used, '291': not_used,
            '292': not_used, '293': not_used,
            '294': not_used, '295': not_used,
            '296': not_used, '297': not_used,
            '298': not_used, '299': not_used,
            '300': not_used, '301': not_used,
            '302': not_used, '303': not_used,
            '304': not_used, '305': not_used,
            '306': not_used, '307': not_used,
            '308': not_used, '309': not_used,
            '310': not_used, '311': not_used,
            '312': not_used, '313': not_used,
            '314': not_used, '315': not_used,
            '316': not_used, '317': not_used,
            '318': not_used, '319': not_used,
            '320': not_used, '321': not_used,
            '322': not_used, '323': not_used,
            '324': not_used, '325': not_used,
            '326': not_used, '327': not_used,
            '328': not_used, '329': not_used,
            '330': not_used, '331': not_used,
            '332': not_used, '333': not_used,
            '334': not_used, '335': not_used,
            '336': not_used, '337': not_used,
            '338': not_used, '339': not_used,
            '340': not_used, '341': not_used,
            '342': not_used, '343': not_used,
            '344': not_used, '345': not_used,
            '346': not_used, '347': not_used,
            '348': not_used, '349': not_used,
            '350': not_used, '351': not_used,
            '352': not_used, '353': not_used,
            '354': not_used, '355': not_used,
            '356': not_used, '357': not_used,
            '358': not_used, '359': not_used,
            '360': not_used, '361': not_used,
            '362': not_used, '363': not_used,
            '364': not_used, '365': not_used,
            '366': not_used, '367': not_used,
            '368': not_used, '369': not_used,
            '370': not_used, '371': not_used,
            '372': not_used, '373': not_used,
            '374': not_used, '375': not_used,
            '376': not_used, '377': not_used,
            '378': not_used, '379': not_used,
            '380': not_used, '381': not_used,
            '382': not_used, '383': not_used,
            '384': not_used, '385': not_used,
            '386': not_used, '387': not_used,
            '388': not_used, '389': not_used,
            '390': not_used, '391': not_used,
            '392': not_used, '393': not_used,
            '394': not_used, '395': not_used,
            '396': not_used, '397': not_used,
            '398': not_used, '399': not_used,
            '400': not_used, '401': not_used,
            '402': not_used, '403': not_used,
            '404': not_used, '405': not_used,
            '406': not_used, '407': not_used,
            '408': not_used, '409': not_used,
            '410': not_used, '411': not_used,
            '412': not_used, '413': not_used,
            '414': not_used, '415': not_used,
            '416': not_used, '417': not_used,
            '418': not_used, '419': not_used,
            '420': not_used, '421': not_used,
            '422': not_used, '423': not_used,
            '424': not_used, '425': not_used,
            '426': not_used, '427': not_used,
            '428': not_used, '429': not_used,
            '430': not_used, '431': not_used,
            '432': not_used, '433': not_used,
            '434': not_used, '435': not_used,
            '436': not_used, '437': not_used,
            '438': not_used, '439': not_used,
            '440': not_used, '441': not_used,
            '442': not_used, '443': not_used,
            '444': not_used, '445': not_used,
            '446': not_used, '447': not_used,
            '448': not_used, '449': not_used,
            '450': not_used, '451': not_used,
            '452': not_used, '453': not_used,
            '454': not_used, '455': not_used,
            '456': not_used, '457': not_used,
            '458': not_used, '459': not_used,
            '460': not_used, '461': not_used,
            '462': not_used, '463': not_used,
            '464': not_used, '465': not_used,
            '466': not_used, '467': not_used,
            '468': not_used, '469': not_used,
            '470': not_used, '471': not_used,
            '472': not_used, '473': not_used,
            '474': not_used, '475': not_used,
            '476': not_used, '477': not_used,
            '478': not_used, '479': not_used,
            '480': not_used, '481': not_used,
            '482': not_used, '483': not_used,
            '484': not_used, '485': not_used,
            '486': not_used, '487': not_used,
            '488': not_used, '489': not_used,
            '490': not_used, '491': not_used,
            '492': not_used, '493': not_used,
            '494': not_used, '495': not_used,
            '496': not_used, '497': not_used,
            '498': not_used, '499': not_used,
            '500': not_used, '501': not_used,
            '502': not_used, '503': not_used,
            '504': not_used, '505': not_used,
            '506': not_used, '507': not_used,
            '508': not_used, '509': not_used,
            '510': not_used, '511': not_used,
            '512': not_used, '513': not_used,
            '514': not_used, '515': not_used,
            '516': not_used, '517': not_used,
            '518': not_used, '519': not_used,
            '520': not_used, '521': not_used,
            '522': not_used, '523': not_used,
            '524': not_used, '525': not_used,
            '526': not_used, '527': not_used,
            '528': not_used, '529': not_used,
            '530': not_used, '531': not_used,
            '532': not_used, '533': not_used,
            '534': not_used, '535': not_used,
            '536': not_used, '537': not_used,
            '538': not_used, '539': not_used,
            '540': not_used, '541': not_used,
            '542': not_used, '543': not_used,
            '544': not_used, '545': not_used,
            '546': not_used, '547': not_used,
            '548': not_used, '549': not_used,
            '550': not_used, '551': not_used,
            '552': not_used, '553': not_used,
            '554': not_used, '555': not_used,
            '556': not_used, '557': not_used,
            '558': not_used, '559': not_used,
            '560': not_used, '561': not_used,
            '562': not_used, '563': not_used,
            '564': not_used, '565': not_used,
            '566': not_used, '567': not_used,
            '568': not_used, '569': not_used,
            '570': not_used, '571': not_used,
            '572': not_used, '573': not_used,
            '574': not_used, '575': not_used,
            '576': not_used, '577': not_used,
            '578': not_used, '579': not_used,
            '580': not_used, '581': not_used,
            '582': not_used, '583': not_used,
            '584': not_used, '585': not_used,
            '586': not_used, '587': not_used,
            '588': not_used, '589': not_used,
            '590': not_used, '591': not_used,
            '592': not_used, '593': not_used,
            '594': not_used, '595': not_used,
            '596': not_used, '597': not_used,
            '598': not_used, '599': not_used,
            '600': not_used, '601': not_used,
            '602': not_used, '603': not_used,
            '604': not_used, '605': not_used,
            '606': not_used, '607': not_used,
            '608': not_used, '609': not_used,
            '610': not_used, '611': not_used,
            '612': not_used, '613': not_used,
            '614': not_used, '615': not_used,
            '616': not_used, '617': not_used,
            '618': not_used, '619': not_used,
            '620': not_used, '621': not_used,
            '622': not_used, '623': not_used,
            '624': not_used, '625': not_used,
            '626': not_used, '627': not_used,
            '628': not_used, '629': not_used,
            '630': not_used, '631': not_used,
            '632': not_used, '633': not_used,
            '634': not_used, '635': not_used,
            '636': not_used, '637': not_used,
            '638': not_used, '639': not_used,
            '640': not_used, '641': not_used,
            '642': not_used, '643': not_used,
            '644': not_used, '645': not_used,
            '646': not_used, '647': not_used,
            '648': not_used, '649': not_used,
            '650': not_used, '651': not_used,
            '652': not_used, '653': not_used,
            '654': not_used, '655': not_used,
            '656': not_used, '657': not_used,
            '658': not_used, '659': not_used,
            '660': not_used, '661': not_used,
            '662': not_used, '663': not_used,
            '664': not_used, '665': not_used,
            '666': not_used, '667': not_used,
            '668': not_used, '669': not_used,
            '670': not_used, '671': not_used,
            '672': not_used, '673': not_used,
            '674': not_used, '675': not_used,
            '676': not_used, '677': not_used,
            '678': not_used, '679': not_used,
            '680': not_used, '681': not_used,
            '682': not_used, '683': not_used,
            '684': not_used, '685': not_used,
            '686': not_used, '687': not_used,
            '688': not_used, '689': not_used,
            '690': not_used, '691': not_used,
            '692': not_used, '693': not_used,
            '694': not_used, '695': not_used,
            '696': not_used, '697': not_used,
            '698': not_used, '699': not_used,
            '700': not_used, '701': not_used,
            '702': not_used, '703': not_used,
            '704': not_used, '705': not_used,
            '706': not_used, '707': not_used,
            '708': not_used, '709': not_used,
            '710': not_used, '711': not_used,
            '712': not_used, '713': not_used,
            '714': not_used, '715': not_used,
            '716': not_used, '717': not_used,
            '718': not_used, '719': not_used,
            '720': not_used, '721': not_used,
            '722': not_used, '723': not_used,
            '724': not_used, '725': not_used,
            '726': not_used, '727': not_used,
            '728': not_used, '729': not_used,
            '730': not_used, '731': not_used,
            '732': not_used, '733': not_used,
            '734': not_used, '735': not_used,
            '736': not_used, '737': not_used,
            '738': not_used, '739': not_used,
            '740': not_used, '741': not_used,
            '742': not_used, '743': not_used,
            '744': not_used, '745': not_used,
            '746': not_used, '747': not_used,
            '748': not_used, '749': not_used,
            '750': not_used, '751': not_used,
            '752': not_used, '753': not_used,
            '754': not_used, '755': not_used,
            '756': not_used, '757': not_used,
            '758': not_used, '759': not_used,
            '760': not_used, '761': not_used,
            '762': not_used, '763': not_used,
            '764': not_used, '765': not_used,
            '766': not_used, '767': not_used,
            '768': not_used, '769': not_used,
            '770': not_used, '771': not_used,
            '772': not_used, '773': not_used,
            '774': not_used, '775': not_used,
            '776': not_used, '777': not_used,
            '778': not_used, '779': not_used,
            '780': not_used, '781': not_used,
            '782': not_used, '783': not_used,
            '784': not_used, '785': not_used,
            '786': not_used, '787': not_used,
            '788': not_used, '789': not_used,
            '790': not_used, '791': not_used,
            '792': not_used, '793': not_used,
            '794': not_used, '795': not_used,
            '796': not_used, '797': not_used,
            '798': not_used, '799': not_used,
            '800': not_used, '801': not_used,
            '802': not_used, '803': not_used,
            '804': not_used, '805': not_used,
            '806': not_used, '807': not_used,
            '808': not_used, '809': not_used,
            '810': not_used, '811': not_used,
            '812': not_used, '813': not_used,
            '814': not_used, '815': not_used,
            '816': not_used, '817': not_used,
            '818': not_used, '819': not_used,
            '820': not_used, '821': not_used,
            '822': not_used, '823': not_used,
            '824': not_used, '825': not_used,
            '826': not_used, '827': not_used,
            '828': not_used, '829': not_used,
            '830': not_used, '831': not_used,
            '832': not_used, '833': not_used,
            '834': not_used, '835': not_used,
            '836': not_used, '837': not_used,
            '838': not_used, '839': not_used,
            '840': not_used, '841': not_used,
            '842': not_used, '843': not_used,
            '844': not_used, '845': not_used,
            '846': not_used, '847': not_used,
            '848': not_used, '849': not_used,
            '850': not_used, '851': not_used,
            '852': not_used, '853': not_used,
            '854': not_used, '855': not_used,
            '856': not_used, '857': not_used,
            '858': not_used, '859': not_used,
            '860': not_used, '861': not_used,
            '862': not_used, '863': not_used,
            '864': not_used, '865': not_used,
            '866': not_used, '867': not_used,
            '868': not_used, '869': not_used,
            '870': not_used, '871': not_used,
            '872': not_used, '873': not_used,
            '874': not_used, '875': not_used,
            '876': not_used, '877': not_used,
            '878': not_used, '879': not_used,
            '880': not_used, '881': not_used,
            '882': not_used, '883': not_used,
            '884': not_used, '885': not_used,
            '886': not_used, '887': not_used,
            '888': not_used, '889': not_used,
            '890': not_used, '891': not_used,
            '892': not_used, '893': not_used,
            '894': not_used, '895': not_used,
            '896': not_used, '897': not_used,
            '898': not_used, '899': not_used,
            '900': not_used, '901': not_used,
            '902': not_used, '903': not_used,
            '904': not_used, '905': not_used,
            '906': not_used, '907': not_used,
            '908': not_used, '909': not_used,
            '910': not_used, '911': not_used,
            '912': not_used, '913': not_used,
            '914': not_used, '915': not_used,
            '916': not_used, '917': not_used,
            '918': not_used, '919': not_used,
            '920': not_used, '921': not_used,
            '922': not_used, '923': not_used,
            '924': not_used, '925': not_used,
            '926': not_used, '927': not_used,
            '928': not_used, '929': not_used,
            '930': not_used, '931': not_used,
            '932': not_used, '933': not_used,
            '934': not_used, '935': not_used,
            '936': not_used, '937': not_used,
            '938': not_used, '939': not_used,
            '940': not_used, '941': not_used,
            '942': not_used, '943': not_used,
            '944': not_used, '945': not_used,
            '946': not_used, '947': not_used,
            '948': not_used, '949': not_used,
            '950': not_used, '951': not_used,
            '952': not_used, '953': not_used,
            '954': not_used, '955': not_used,
            '956': not_used, '957': not_used,
            '958': not_used, '959': not_used,
            '960': not_used, '961': not_used,
            '962': not_used, '963': not_used,
            '964': not_used, '965': not_used,
            '966': not_used, '967': not_used,
            '968': not_used, '969': not_used,
            '970': not_used, '971': not_used,
            '972': not_used, '973': not_used,
            '974': not_used, '975': not_used,
            '976': not_used, '977': not_used,
            '978': not_used, '979': not_used,
            '980': not_used, '981': not_used,
            '982': not_used, '983': not_used,
            '984': not_used, '985': not_used,
            '986': not_used, '987': not_used,
            '988': not_used, '989': not_used,
            '990': not_used, '991': not_used,
            '992': not_used, '993': not_used,
            '994': not_used, '995': not_used,
            '996': not_used, '997': not_used,
            '998': not_used, '999': not_used
           }
			
def LCBF_to_Ragaraja(source):
    '''
    Converts Loose Circular Brainfuck source code to Ragaraja source code
    
    @param source: Loose Circular Brainfuck (LCBF) source code
    @type source: string
    @return: Ragaraja source code string
    '''
    converted = []
    for x in source:
        if x == '>': converted.append('000')
        elif x == '<': converted.append('004')
        elif x == '+': converted.append('008')
        elif x == '-': converted.append('011')
        elif x == '.': converted.append('020')
        elif x == ',': converted.append('063')
        elif x == '[': converted.append('014')
        elif x == ']': converted.append('015')
        else: converted.append('...')
    return converted
	
def nBF_to_Ragaraja(source):
    '''
    Converts NucleotideBF (nBF) source code to Ragaraja source code
    
    @param source: NucleotideBF (nBF) source code
    @type source: string
    @return: Ragaraja source code string
    '''
    converted = []
    for x in source:
        if x == 'G': converted.append('000')
        elif x == 'C': converted.append('004')
        elif x == 'A': converted.append('008')
        elif x == 'T': converted.append('011')
        elif x == '.': converted.append('020')
        elif x == 'R': converted.append('050')
        elif x == 'Y': converted.append('051')
        elif x == 'S': converted.append('052')
        elif x == 'W': converted.append('053')
        elif x == 'K': converted.append('054')
        elif x == 'M': converted.append('055')
        elif x == 'B': converted.append('056')
        elif x == 'D': converted.append('057')
        elif x == 'H': converted.append('058')
        elif x == 'V': converted.append('059')
        elif x == 'N': converted.append('060')
        else: converted.append('...')
    return converted
			
def interpreter(source, inputdata=[], array=None, size=30000):
    (array, apointer, inputdata, output, source, spointer) = \
        r.interpret(source, ragaraja, 3, inputdata, array, size)
    return (array, apointer, inputdata, output, source, spointer)
	
if __name__ == '__main__':
    print interpreter('000008008000000011011011004008', [], None, 30)
    print interpreter('001009002010005012', [], None, 30)
