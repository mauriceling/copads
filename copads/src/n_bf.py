import random
import register_machine as r
from lc_bf import increment, decrement, forward, backward, call_out

def random_op(array, apointer, inputdata, output, source, spointer):
    r = random.random()
    if source[spointer] == 'R' and r < 0.5:
        return increment(array, apointer, inputdata, output, source, spointer)
    elif source[spointer] == 'R' and r >= 0.5:
        if apointer == len(array): apointer = 0
        return forward(array, apointer, inputdata, output, source, spointer)
    elif source[spointer] == 'Y' and r < 0.5:
        return decrement(array, apointer, inputdata, output, source, spointer)
    elif source[spointer] == 'Y' and r >= 0.5:
        if apointer == 0: apointer = len(array) 
        return backward(array, apointer, inputdata, output, source, spointer)
    elif source[spointer] == 'S' and r < 0.5:
        if apointer == len(array): apointer = 0
        return forward(array, apointer, inputdata, output, source, spointer)
    elif source[spointer] == 'S' and r >= 0.5:
        if apointer == 0: apointer = len(array) 
        return backward(array, apointer, inputdata, output, source, spointer)
    elif source[spointer] == 'W' and r < 0.5:
        return increment(array, apointer, inputdata, output, source, spointer)
    elif source[spointer] == 'W' and r >= 0.5:
        return decrement(array, apointer, inputdata, output, source, spointer)
    elif source[spointer] == 'K' and r < 0.5:
        return decrement(array, apointer, inputdata, output, source, spointer)
    elif source[spointer] == 'K' and r >= 0.5:
        if apointer == len(array): apointer = 0
        return forward(array, apointer, inputdata, output, source, spointer)
    elif source[spointer] == 'M' and r < 0.5:
        return increment(array, apointer, inputdata, output, source, spointer)
    elif source[spointer] == 'M' and r >= 0.5:
        if apointer == 0: apointer = len(array) 
        return backward(array, apointer, inputdata, output, source, spointer)
    elif source[spointer] == 'B' and r < 0.33:
        if apointer == len(array): apointer = 0
        return forward(array, apointer, inputdata, output, source, spointer)
    elif source[spointer] == 'B' and r >= 0.33 and r < 0.67:
        return decrement(array, apointer, inputdata, output, source, spointer)
    elif source[spointer] == 'B' and r >= 0.67:
        if apointer == 0: apointer = len(array) 
        return backward(array, apointer, inputdata, output, source, spointer)
    elif source[spointer] == 'D' and r < 0.33:
        return increment(array, apointer, inputdata, output, source, spointer)
    elif source[spointer] == 'D' and r >= 0.33 and r < 0.67:
        return decrement(array, apointer, inputdata, output, source, spointer)
    elif source[spointer] == 'D' and r >= 0.67:
        if apointer == len(array): apointer = 0
        return forward(array, apointer, inputdata, output, source, spointer)
    elif source[spointer] == 'H' and r < 0.33:
        return increment(array, apointer, inputdata, output, source, spointer)
    elif source[spointer] == 'H' and r >= 0.33 and r < 0.67:
        return decrement(array, apointer, inputdata, output, source, spointer)
    elif source[spointer] == 'H' and r >= 0.67:
        if apointer == 0: apointer = len(array) 
        return backward(array, apointer, inputdata, output, source, spointer)
    elif source[spointer] == 'V' and r < 0.33:
        return increment(array, apointer, inputdata, output, source, spointer)
    elif source[spointer] == 'V' and r >= 0.33 and r < 0.67:
        if apointer == len(array): apointer = 0
        return forward(array, apointer, inputdata, output, source, spointer)
    elif source[spointer] == 'V' and r >= 0.67:
        if apointer == 0: apointer = len(array) 
        return backward(array, apointer, inputdata, output, source, spointer)
    elif source[spointer] == 'N' and r < 0.25:
        return increment(array, apointer, inputdata, output, source, spointer)
    elif source[spointer] == 'N' and r >= 0.25 and r < 0.5:
        return decrement(array, apointer, inputdata, output, source, spointer)
    elif source[spointer] == 'N' and r >= 0.5 and r < 0.75:
        if apointer == len(array): apointer = 0
        return forward(array, apointer, inputdata, output, source, spointer)
    elif source[spointer] == 'N' and r >= 0.75:
        if apointer == 0: apointer = len(array) 
        return backward(array, apointer, inputdata, output, source, spointer)

nBF = {'A': increment,
       'T': decrement,
       'G': forward,
       'C': backward,
       'R': random_op,
       'Y': random_op,
       'S': random_op,
       'W': random_op,
       'K': random_op,
       'M': random_op,     
       'B': random_op,
       'D': random_op,
       'H': random_op,
       'V': random_op,
       'N': random_op,
       '.': call_out
       }

if __name__ == '__main__':
    print r.interpret('AAAAGGTTTCAAA', nBF)
    print r.interpret('AAAAGGTTTCAAARRYYSKVDVDBBHVNVH', nBF)
