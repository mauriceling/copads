'''
Circular file hash
Date created: 16th April 2013
Licence: Python Software Foundation License version 2
'''

import hashlib as h

def forward_hash(f, fsize, start, blocksize, algorithm):
    hash_result = ''
    count = 0
    while start < fsize:
        f.seek(start)
        data = str(f.read(blocksize))
        if algorithm == 'md5':
            hash_result = h.md5(data + str(hash_result)).hexdigest()
        if algorithm == 'sha1':
            hash_result = h.sha1(data + str(hash_result)).hexdigest()
        if algorithm == 'sha244':
            hash_result = h.sha244(data + str(hash_result)).hexdigest()
        if algorithm == 'sha256':
            hash_result = h.sha256(data + str(hash_result)).hexdigest()
        if algorithm == 'sha384':
            hash_result = h.sha384(data + str(hash_result)).hexdigest()
        if algorithm == 'sha512':
            hash_result = h.sha244(data + str(hash_result)).hexdigest()
        start = start + blocksize
        count = count + 1
##        print start, hash_result
    print 'forward hash:', start, count
    return hash_result
    
def backward_hash(f, end, blocksize, algorithm):
    hash_result = ''
    current = 0
    count = 0
    while current < end:
        f.seek(current)
        data = str(f.read(blocksize))
        if algorithm == 'md5':
            hash_result = h.md5(data + str(hash_result)).hexdigest()
        if algorithm == 'sha1':
            hash_result = h.sha1(data + str(hash_result)).hexdigest()
        if algorithm == 'sha244':
            hash_result = h.sha244(data + str(hash_result)).hexdigest()
        if algorithm == 'sha256':
            hash_result = h.sha256(data + str(hash_result)).hexdigest()
        if algorithm == 'sha384':
            hash_result = h.sha384(data + str(hash_result)).hexdigest()
        if algorithm == 'sha512':
            hash_result = h.sha244(data + str(hash_result)).hexdigest()
        current = current + blocksize
        count = count + 1
##        print end, hash_result
    print 'backward hash:', end, count
    return hash_result
    
def cfh(filename,
        blocksize=1024,
        startpoints=10,
        algorithm='md5'):
    f = open(filename, 'rb')
    f.seek(-1, 2)
    fsize = f.tell()
    file_block_size = int(fsize/int(startpoints))
    startpoints = [x*file_block_size
                   for x in range(int(startpoints))]
    fhash = [forward_hash(f, fsize, start, blocksize, algorithm)
             for start in startpoints]
    bhash = [backward_hash(f, startpoints[-1], blocksize, algorithm)]
    bhash = bhash + [backward_hash(f, start, blocksize, algorithm)
                     for start in startpoints[1:]]
    return ''.join(fhash + bhash)
