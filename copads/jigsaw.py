'''
Jigsaw Encryption System

Date created: 25th May 2016

Licence: Python Software Foundation License version 2

Jigsaw Encryption System (JES) takes its inspiration from jigsaw puzzles. 
Most cryptography methods is a 1-to-1 file method - during encryption, a 
single unencrypted file (commonly known as plain text) is encrypted into 
one encrypted file (commonly known as cipher text) using a key. 
Decryption does the reverse. Mathematically,

M{encrypt(plaintext, key) --> ciphertext}

M{decrypt(ciphertext, key) --> plaintext}

If encryption and decryption are seen as transformation and de-
transformation functions, respectively, between plain text and cipher 
text; the weakest link is in the 1-to-1 file mapping. Brute force attack 
is possible because all the plain text information exist in the cipher 
text, though transformed.

JES addresses the 1-to-1 file weakness by using 1-to-N file mapping. This 
is likened to taking a picture and make a jigsaw puzzle out of it. The 
complexity of brute force attack increases exponentially with the number 
of jigsaw pieces. By producing many files, it also makes it possible to 
transport the encrypted file safely via multiple routes, and this prevents 
reduces the chances of man-in-the-middle attack. This is like making a 
1000-piece jigsaw puzzle, shuffle the pieces, load the pieces into 5 
containers and the assembly instruction in the 6th container. If one 
container is hijacked, all the information is not compromised. 

Given that the key size of AES-256 is 32 characters long (32 characters 
of 8 bytes each = 256 bytes) and given that there are 94 characters in 
the set of mixed alphanumeric with symbols (that is, abcdefghijklmnopqr
stuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_+=~`[]{}|\:;"'
<>,.?/), the total number of keys is 1.38 x 10**63 (94**32).

How does this number of permutations compare with Jigsaw Encryption?

Assuming that Jigsaw Encryption is used to encrypt a 1 MB (1048576 bytes) 
file and split into 16 64-KB Jigsaw files, there are 2 x 10**13 
permutations to assemble 16 64-KB files into the original 1 MB file using 
Jigsaw version 1. 

Jigsaw version 2 provides 63 variations for each Jigsaw file. Hence, the 
full permutations possible for 16 64-KB files is (2 x 10**13)**63 or 9 x 
10**837, and that is just for a 1 MB file split into 16 64-KB.
Jigsaw files.

Jigsaw version 3 takes the Jigsaw file provided by Jigsaw version 2 and 
apply one of the 1350 transpositions. Hence, the full permutations 
possible for 16 64-KB files is (9 x 10**837)**1350 or 1 x 10**1131238.
'''

import os
import random
import hashlib

class JigsawCore(object):
    '''
    Class to hold the core functions that are common for Jigsaw 
    implementations.
    '''
    
    hash = hashlib.sha256
    rfloat = random.random
    rchoice = random.choice
    
    def __init__(self):
        '''Constructor method'''
        pass
    
    def evenSlicer(self, filename, block_size=4096):
        '''
        Generator function to slice a file into blocks of even sizes 
        (except the last block).
        
        @param filename: name (absolute path or relative path) of file to 
        be sliced.
        @type filename: string
        @param block_size: size of each block. Default = 4096 bytes.
        @type block_size: integer
        @return: Blocks of file (generator function).
        '''
        f = open(filename, 'rb')
        block_size = int(block_size)
        block = True
        while block:
            block = f.read(block_size)
            yield block
        f.close()

    def unevenSlicer(self, filename, 
                     min_block_size=4096, 
                     max_block_size=16384):
        '''
        Generator function to slice a file into blocks of uneven sizes.
        
        @param filename: name (absolute path or relative path) of file to 
        be sliced.
        @type filename: string
        @param min_block_size: minimum size of each block. Default = 4096 
        bytes.
        @type min_block_size: integer
        @param max_block_size: maximum size of each block. Default = 16384 
        bytes.
        @type max_block_size: integer
        @return: Blocks of file (generator function).
        '''
        f = open(filename, 'rb')
        block = True
        while block:
            block_size = int(max_block_size) - int(min_block_size)
            block_size = int(self.rfloat() * block_size)
            block_size = int(min_block_size) + block_size
            block = f.read(block_size)
            yield block
        f.close()
        
    def swapBlock(self, block, subBlockALocation, subBlockBLocation):
        '''
        Function to swap 2 sub-blocks within a block. For example, if the 
        block consist of [1, 'A', 2, 'B', 3]; swapping 'A' and 'B' will 
        result in [1, 'B', 2, 'A', 3].
        
        >>> import jigsaw
        >>> c = jigsaw.JigsawCore()
        >>> block = 'ABCDEFGHIJKLM'
        >>> swapped = c.swapBlock(block, (3, 4), (10, 11))
        >>> swapped
        'ABCKEFGHIJDLM'
        >>> reverse_swapped = c.swapBlock(swapped, (3, 4), (10, 11))
        >>> reverse_swapped
        'ABCDEFGHIJKLM'
        >>> 
        
        @param block: block to be processed.
        @type block: string
        @param subBlockALocation: coordinate of first sub-block.
        @type subBlockALocation: tuple
        @param subBlockBLocation: coordinate of second sub-block.
        @type:subBlockBLocation: tuple
        '''
        block = [item for item in block]
        if type(subBlockALocation) == type([]) and \
            len(subBlockALocation) == 1:
            subBlockALocation = [0, int(subBlockALocation[0])]
        elif type(subBlockALocation) == type('str'):
            subBlockALocation = [0, int(subBlockALocation[0])]
        if type(subBlockBLocation) == type([]) and \
            len(subBlockBLocation) == 1:
            subBlockBLocation = [int(subBlockBLocation[0]), len(block)]
        elif type(subBlockBLocation) == type('str'):
            subBlockBLocation = [int(subBlockBLocation[0]), len(block)]
        preBlockA = block[0:subBlockALocation[0]]
        BlockA = block[subBlockALocation[0]:subBlockALocation[1]]
        BlockABlockB = block[subBlockALocation[1]:subBlockBLocation[0]]
        BlockB = block[subBlockBLocation[0]:subBlockBLocation[1]]
        postBlockB = block[subBlockBLocation[1]:]
        swapped = preBlockA + BlockB + BlockABlockB + BlockA + postBlockB
        return ''.join(swapped)
        
    def reverseBlock(self, block):
        '''
        Function to reverse a string.

        >>> import jigsaw
        >>> c = jigsaw.JigsawCore()
        >>> c.reverseBlock('1234567890')
        '0987654321'
        >>>

        @param block: data to be reversed.
        @type block: string
        @return: reversed block
        '''
        block = [item for item in block]
        block.reverse()
        return ''.join(block)

    def subBlock(self, block, length):
        '''
        Generator function to divide a block into smaller blocks 
        (also known as sub-blocks).

        >>> c = jigsaw.JigsawCore()
        >>> text = 'MyNameIsMauriceLing,AndIInventedJigsawEncryption'
        >>> for s in c.subBlock(text, 10):
        ...     print s
        ... 
        MyNameIsMa
        uriceLing,
        AndIInvent
        edJigsawEn
        cryption
        >>> 

        @param block: data block to be divided into sub-blocks.
        @type block: string
        @param length: length of sub-block.
        @type length: integer
        @return: sub-block
        '''
        length = int(length)
        block = [item for item in block]
        sblock = []
        while len(block) > length - 1:
            if len(block) > length:
                sblock = block[:length]
                block = block[length:]
            else:
                sblock = block
            yield ''.join(sblock)
        yield ''.join(block)

    def shuffleBlock(self, block, length):
        '''
        Function to take a block, divide the block into smaller 
        sub-blocks, and shuffle the order of the sub-blocks.

        >>> import jigsaw
        >>> c = jigsaw.JigsawCore()
        >>> text = 'MyNameIsMauriceLing,AndIInventedJigsawEncryption'
        >>> (shuffled_blocks, block_order) = c.shuffleBlock(text, 10)
        >>> print shuffled_blocks
        'edJigsawEnuriceLing,AndIInventMyNameIsMacryption'
        >>> print block_order
        [3, 1, 2, 0, 4]
        >>>

        @param block: data block to be shuffled.
        @type block: string
        @param length: length of sub-block.
        @type length: integer
        @return: (shuffled block, order of sub-blocks)
        '''
        sblocks = [sb for sb in self.subBlock(block, length)]
        shuffled_blocks = range(len(sblocks))
        block_order = range(len(sblocks)-1)
        random.shuffle(block_order)
        block_order.append(len(sblocks)-1)
        shuffled_blocks = [sblocks[order] for order in block_order]
        shuffled_blocks = ''.join(shuffled_blocks)
        return (shuffled_blocks, block_order)

    def deshuffleBlock(self, block, length, block_order):
        '''
        
        >>> import jigsaw
        >>> c = jigsaw.JigsawCore()
        >>> text = 'MyNameIsMauriceLing,AndIInventedJigsawEncryption'
        >>> (shuffled_blocks, block_order) = c.shuffleBlock(text, 10)
        >>> print shuffled_blocks
        uriceLing,MyNameIsMaAndIInventedJigsawEncryption
        >>> print block_order
        [1, 0, 2, 3, 4]
        >>> deshuffled_blocks = c.deshuffleBlock(shuffled_blocks, 10, block_order)
        >>> print deshuffled_blocks
        MyNameIsMauriceLing,AndIInventedJigsawEncryption
        >>> 
        '''
        sblocks = [sb for sb in self.subBlock(block, length)]
        deshuffled_blocks = range(len(sblocks))
        index = 0
        for order in block_order:
            deshuffled_blocks[index] = sblocks[order]
            index = index + 1
        return ''.join(deshuffled_blocks)
    
    def reversePartBlock(self, block, length):
        '''
        Function to reverse the first N-th length of a string or 
        a list. If N is equal or more than the length of the 
        block, the entire block will be reversed

        @param block: data to be reversed.
        @type block: string
        @param length: number of N-th items (from the front) to be 
        reversed.
        @type length: integer
        @return: reversed block
        '''
        length = abs(int(length))
        if length > len(block) - 1:
            return self.reverseBlock(block)
        block = [item for item in block]
        rblock = block[:length]
        rblock.reverse()
        block = rblock + block[length:]
        return ''.join(block)
                
    def reversePartBlock2(self, block, slength, elength):
        '''
        Function to reverse from M-th to N-th length of a string or 
        a list where M < N. If M is zero or less than zero, reversal will 
        start from the first element. If N is equal or more than the length 
        of the block, the entire block from M will be reversed. 

        @param block: data to be reversed.
        @type block: string
        @param slength: number of M-th items (from the front) to start 
        reversing.
        @type slength: integer
        @param elength: number of N-th items (from the front) to start 
        reversing.
        @type elength: integer
        @return: reversed block
        '''
        slength = abs(int(slength))
        elength = abs(int(elength))
        if slength < 0:
            slength = 0
        if elength > len(block) - 1:
            elength = len(block) - 1
        if elength < slength:
            elength = slength
        block = [item for item in block]
        rblock = block[slength:elength]
        rblock.reverse()
        block = block[:slength] + rblock + block[elength:]
        return ''.join(block)

    def generateHash(self, filename):
        '''
        Function to generate a set of hashes for a single file. The hashes 
        which will be generated are:
            - md5
            - sha1
            - sha224
            - sha256
            - sha384
            - sha512
        
        @param filename: name (absolute path or relative path) of file to 
        be hashed.
        @type filename: string
        @return: a list of hashes - [md5, sha1, sha224, sha256, sha384, 
        sha512].
        '''
        md5 = hashlib.md5()
        sha1 = hashlib.sha1()
        sha224 = hashlib.sha224()
        sha256 = hashlib.sha256()
        sha384 = hashlib.sha384()
        sha512 = hashlib.sha512()
        f = open(filename, 'rb')
        block = True
        while block:
            block = f.read(4096)
            md5.update(block)
            sha1.update(block)
            sha224.update(block)
            sha256.update(block)
            sha384.update(block)
            sha512.update(block)
        return [str(md5.hexdigest()),
                str(sha1.hexdigest()),
                str(sha224.hexdigest()),
                str(sha256.hexdigest()),
                str(sha384.hexdigest()),
                str(sha512.hexdigest())]

class JigsawFile(JigsawCore):
    '''
    Implementation of Jigsaw System for files, to be used on individual 
    file; where a file will be split into multiple smaller files of either 
    equal or unequal file sizes known as Jigsaw files. A keyfile will be 
    generated (the file name is <original filename with extension>.jgk), 
    which is required for assembly of the various sub-files (file extension 
    is '.jig' into the original file.
    
    >>> from jigsaw import JigsawFile
    >>> jsys = JigsawFile()
    >>> jsys.setting('version', 1)          # Jigsaw version 1
    >>> jsys.setting('slicer', 'uneven')    # generates uneven sized files
    >>> jsys.setting('blocksize', 65535)    # 64kb < file size < 128kb
    >>> jsys.setting('filenamelength', 30)  # 30 character sub-file names
    >>> jsys.setting('hashlength', 16)      # 16 character sub-file hash
    >>> # encrypt /home/mling/GA.zip and place sub-files and keyfile into 
    >>> # /home/jigsaw
    >>> jsys.encrypt('/home/mling/GA.zip', /home/jigsaw)
    >>> # decrypt the previously encrypted file
    >>> # keyfile = /home/jigsaw/GA.zip.jgk
    >>> # all the encrypted sub-files are found in /home/jigsaw
    >>> # assembled/decrypted file = /home/jigsaw/GA_decrypt.zip
    >>> jsys.decrypt('/home/jigsaw/GA.zip.jgk', 
    ...              '/home/jigsaw/GA_decrypt.zip', 
    ...              '/home/jigsaw')
    >>>
    
    The following Jigsaw versions are implemented:
        - version 1: The original file is sliced and saved as a series of 
        smaller files.
        - version 2: The original file is sliced into blocks. Each block is 
        separated into 2 sub-blocks where the first sub-block is reversed 
        and merged before saved as a file.
        - version 2: The original file is sliced into blocks. Each block is 
        separated into 2 sub-blocks where the first sub-block is reversed. 
        This is following double transposition of the same number of bytes 
        in the block before saved as a file.
    '''
    def __init__(self):
        '''Constructor method.'''
        self.version = 'JigsawFileONE'
        self.reverseOptions = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
                               'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
                               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
                               'Y', 'Z', '1', '2', '3', '4', '5', '6', 
                               '7', '8', '9', '1a',
                               '1b', '1c', '1e', '1f',
                               '1g', '1h', '2a', '2b', '2c', 
                               '2e', '2f', '2g', '3a', '3b', 
                               '3c', '3d', '3e', '3f', '4a', 
                               '4b', '4c', '4d', '4e','5a', 
                               '5b', '5c', '5d']
        # 1350 swap sizes
        self.swapSize = [str(x) for x in range(0, 4050, 3)]
        self.decryptkey = None
        self.fileList = []
        self.checksums = []
        self.slicer = 'even'
        self.block_size = 4096
        self.filename_length = 30
        self.hashlength = 16
        self.inputdir = ''
        self.filename = ''
        self.outputdir = ''
        self.keyfilename = ''
        self.decryptfilename = ''
        self.verbose = 1
        self.header = {}

    def setting(self, key, value):
        '''
        Function to set various options to the system.
        
        Available options to set are:
            - blocksize: Set the size of a Jigsaw file. Allowable values 
            are any positive integer. In the case of uneven slicer, size 
            of Jisgaw files will be between 1 to 2  block sizes.
            - filenamelength: Set the length of file name of a Jigsaw file. 
            Longer file name determines the number of allowable Jigsaw 
            files in a directory, up to file system limits. Allowable 
            values are any positive integer.
            - hashlength: Set the file has length of each Jigsaw file. 
            This is used to check for fidelity of the files. Allowable 
            values are any positive integer.
            - slicer: Set the file slicing method. Allowable values are 
            'even' (even Jigsaw file size) or 'uneven' (uneven Jigsaw file 
            size).
            - verbose: Set the verbosity from 1 (most information) onwards.
            - version: Set the Jigsaw version. Allowable values are 1 
            (version 1).
        
        @param key: name of option to set.
        @type key: string
        @param value: value to set the option.
        '''
        key = str(key).lower()
        if key == 'slicer':
            if str(value).lower() == 'uneven':
                self.slicer = 'uneven'
            else:
                self.slicer = 'even'
        elif key == 'blocksize':
            self.block_size = abs(int(value))
        elif key == 'filenamelength':
            self.filename_length = abs(int(value))
        elif key == 'version':
            if value == 1:
                self.version = 'JigsawFileONE'
            elif value == 2:
                self.version = 'JigsawFileTWO'
            elif value == 3:
                self.version = 'JigsawFileTHREE'
        elif key == 'hashlength':
            self.hashlength = abs(int(value))
        elif key == 'verbose':
            self.verbose = abs(int(value))

    def _generateFilename(self):
        '''
        Private method to generate non-duplicating name for sub-files.
        '''
        mapping = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A',
                   'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                   'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                   'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'd', 'e', 'g',
                   'h', 'q', 'r', 't']
        while True:
            randomName = [self.rchoice(mapping) 
                          for i in range(self.filename_length)]
            randomName = ''.join(randomName) + '.jig'
            if randomName not in self.fileList:
                self.fileList.append(randomName)
                return randomName

    def _setEncryptDir(self, outputdir=''):
        '''
        Private function to set the input and output directories prior to 
        encryption.
        
        Input directory (directory of file to encrypt): It will first 
        attempt to get input directory from input file name if the input 
        file name is an absolute path. Otherwise, if the input file name 
        is a relative path, the current working directory will be used.
        
        Output directory (directory to write out Jigsaw files and keyfile): 
        If given, it will be used. If not given, it will use the input 
        directory (depending on whether the input file name is absolute or 
        relative file name).
        
        @param outputdir: absolute path of directory (without trailing 
        slash) to write the Jigsaw files (encrypted/sub-files) into. This 
        parameter is optional. If not given, the Jigsaw files will be in 
        the same directory as the input file or int he current working 
        directory.
        @type outputdir: string
        '''
        # Input directory
        print('... Sorting out input (source file) directory')
        print('...... Attempt to get input directory from input file path')
        if len(self.filename.split(os.sep)) > 1:
            self.inputdir = self.filename.split(os.sep)[:-1]
            self.inputdir = os.sep.join(self.inputdir)
        elif len(self.filename.split(os.sep)) == 1:
            print('...... Failed: Input file is relative file name')
            print('...... Set input directory to currect working directory')
            self.inputdir = os.getcwd()
        # Output directory
        print('... Sorting out output (encrypted files output) directory')
        if outputdir != '':
            print('...... Output directory given as %s' % outputdir)
            print('...... Set output directory to %s' % outputdir)
            self.outputdir = outputdir
        else:
            print('...... Output directory not given')
            print('...... Attempt to find output directory from input file')
            if len(self.filename.split(os.sep)) > 1:
                print('...... Input file name is absolute path: %s' % 
                    self.filename)
                self.outputdir = self.filename.split(os.sep)[:-1]
                self.outputdir = os.sep.join(self.outputdir)
                print('...... Set output directory to: %s' % self.outdir)
            else:
                print('...... Failed: Input file is relative file name')
                print('...... Set output directory to currect working directory')
                self.outputdir = os.getcwd()

    def _writeKeyHeader(self):
        '''
        Private method to write out keyfile (.jgk) header. The header 
        contains information and metadata related to the encryption, which 
        may be used during decryption process. To separate from header 
        from the encryption coding, header lines starts with '#'.
        
        @return: name of keyfile.
        '''
        if len(self.filename.split(os.sep)) == 1:
            filename = self.filename
        else:
            filename = self.filename.split(os.sep)[-1]
        kfileName = os.sep.join([self.outputdir, filename + '.jgk'])
        print('Writing key file: %s' % kfileName)
        self.decryptkey = open(kfileName, 'w')
        header = ['>>'.join([k, self.header[k]]) 
                  for k in self.header.keys()]
        for line in header:
            self.decryptkey.write(line + '\n')
        return kfileName

    def _addHeader(self, key, value):
        '''
        Private method to add items to be written into keyfile.
        
        @param key: name of option to set.
        @type key: string
        @param value: value to set the option.
        '''
        key = str(key)
        value = str(value)
        if not key.startswith('#'):
            key = '#' + key
        self.header[key] = value
            
    def _encryptVerbosity(self, count, data):
        '''
        Private method to generate process information based in level of 
        verbosity (1 = most information; highest verbosity) during 
        encryption.

        @param count: block sequence
        @type count: integer
        @param data: process information
        @type data: string
        '''
        if self.verbose == 1:
            print('Code: %s' % data)
        if self.verbose > 1 and (count % 1000 == 0):
            print('%s blocks processed' % str(count))
        
    def _writeJigsawFile(self, block):
        '''
        Private method to write a block into a Jigsaw file. A 
        truncated SHA1 hash of the block/Jigsaw file will be 
        generated for checking against corruption during file 
        storage and transportation.

        @param block: data to be written into a Jigsaw file.
        @type block: byte
        @return: (hash, relative path of Jigsaw file)
        '''
        ofileName = self._generateFilename()
        ofile = open(self.outputdir + os.sep + ofileName, 'wb')
        hash = str(self.hash(block).hexdigest()[:self.hashlength])
        ofile.write(block)
        ofile.close()
        return (hash, ofileName)

    def _encrypt1(self, filename):
        '''
        Private method to run the operations for Jigsaw version 1 
        encryption.
        
        The encryption coding write out into keyfile consist of the 
        following (in the order, delimited by '>>'):
            - 'AA'
            - block sequence (incremental integer from 0)
            - size of block (in bytes)
            - directory to write out Jigsaw file
            - name of Jigsaw file
            - truncated sha256 hash of block
        
        @param filename: name (absolute path or relative path) of file to 
        be encrypted.
        @type filename: string
        @return: number of blocks processed
        '''
        count = 0
        if self.slicer == 'even':
            print('Processing using even slicer')
            for block in self.evenSlicer(self.filename, 
                                         self.block_size):
                (hash, ofileName) = self._writeJigsawFile(block)
                data = '>>'.join(['AA', str(count), str(len(block)), 
                                  self.outputdir, ofileName, hash])
                self.decryptkey.write(data + '\n')
                self._encryptVerbosity(count, data)
                count = count + 1
        if self.slicer == 'uneven':
            print('Processing using uneven slicer')
            for block in self.unevenSlicer(self.filename, 
                                           self.block_size, 
                                           self.block_size*2):
                (hash, ofileName) = self._writeJigsawFile(block)
                data = '>>'.join(['AA', str(count), str(len(block)), 
                                  self.outputdir, ofileName, hash])
                self.decryptkey.write(data + '\n')
                self._encryptVerbosity(count, data)
                count = count + 1
        return count

    def _blockReverse(self, block, reverse_flag):
        '''
        Private method for block reversal based on fixed reversal scheme.

        @param block: data to be reversed.
        @type block: string
        @param reverse_flag: type of reversal. Allowable values are: 
            - 'A' (no reversal)
            - 'B' (full reversal)
            - 'C' (reverse first 200 bytes)
            - 'D' (reverse first 400 bytes)
            - 'E' (reverse first 600 bytes)
            - 'F' (reverse first 800 bytes)
            - 'G' (reverse first 1000 bytes)
            - 'H' (reverse first 1200 bytes)
            - 'I' (reverse first 1400 bytes)
            - 'J' (reverse first 1600 bytes)
            - 'K' (reverse first 1800 bytes)
            - 'L' (reverse first 2000 bytes)
            - 'M' (reverse first 2200 bytes)
            - 'N' (reverse first 2400 bytes)
            - 'O' (reverse first 2600 bytes)
            - 'P' (reverse first 2800 bytes)
            - 'Q' (reverse first 3000 bytes)
            - 'R' (reverse first 3200 bytes)
            - 'S' (reverse first 3400 bytes)
            - 'T' (reverse first 3600 bytes)
            - 'U' (reverse first 3800 bytes)
            - 'V' (reverse first 4000 bytes)
            - 'W' (reversing the last 10% of the bytes)
            - 'X' (reversing the last 20% of the bytes)
            - 'Y' (reversing the last 30% of the bytes)
            - 'Z' (reversing the last 40% of the bytes)
            - '1' (reverse first 10% of the bytes)
            - '2' (reverse first 20% of the bytes)
            - '3' (reverse first 30% of the bytes)
            - '4' (reverse first 40% of the bytes)
            - '5' (reverse first 50% of the bytes)
            - '6' (reverse first 60% of the bytes)
            - '7' (reverse first 70% of the bytes)
            - '8' (reverse first 80% of the bytes)
            - '9' (reverse first 90% of the bytes)
            - '1a' (reverse first 10% to 20% of the bytes)
            - '1b' (reverse first 20% to 30% of the bytes)
            - '1c' (reverse first 30% to 40% of the bytes)
            - '1d' (reverse first 40% to 50% of the bytes)
            - '1e' (reverse first 50% to 60% of the bytes)
            - '1f' (reverse first 60% to 70% of the bytes)
            - '1g' (reverse first 70% to 80% of the bytes)
            - '1h' (reverse first 80% to 90% of the bytes)
            - '2a' (reverse first 10% to 30% of the bytes)
            - '2b' (reverse first 20% to 40% of the bytes)
            - '2c' (reverse first 30% to 50% of the bytes)
            - '2d' (reverse first 40% to 60% of the bytes)
            - '2e' (reverse first 50% to 70% of the bytes)
            - '2f' (reverse first 60% to 80% of the bytes)
            - '2g' (reverse first 70% to 90% of the bytes)
            - '3a' (reverse first 10% to 40% of the bytes)
            - '3b' (reverse first 20% to 50% of the bytes)
            - '3c' (reverse first 30% to 60% of the bytes)
            - '3d' (reverse first 40% to 70% of the bytes)
            - '3e' (reverse first 50% to 80% of the bytes)
            - '3f' (reverse first 60% to 90% of the bytes)
            - '4a' (reverse first 10% to 50% of the bytes)
            - '4b' (reverse first 20% to 60% of the bytes)
            - '4c' (reverse first 30% to 70% of the bytes)
            - '4d' (reverse first 40% to 80% of the bytes)
            - '4e' (reverse first 50% to 90% of the bytes)
            - '5a' (reverse first 10% to 60% of the bytes)
            - '5b' (reverse first 20% to 70% of the bytes)
            - '5c' (reverse first 30% to 80% of the bytes)
            - '5d' (reverse first 40% to 90% of the bytes)
        @type reverse_flag: string
        @return: reversed block
        '''
        if reverse_flag.startswith('RR'):
            pass
        elif reverse_flag == 'A':
            block = block
        elif reverse_flag == 'B':
            block = self.reverseBlock(block)
        elif reverse_flag == 'C':
            block = self.reversePartBlock(block, 200)
        elif reverse_flag == 'D':
            block = self.reversePartBlock(block, 400)
        elif reverse_flag == 'E':
            block = self.reversePartBlock(block, 600)
        elif reverse_flag == 'F':
            block = self.reversePartBlock(block, 800)
        elif reverse_flag == 'G':
            block = self.reversePartBlock(block, 1000)
        elif reverse_flag == 'H':
            block = self.reversePartBlock(block, 1200)
        elif reverse_flag == 'I':
            block = self.reversePartBlock(block, 1400)
        elif reverse_flag == 'J':
            block = self.reversePartBlock(block, 1600)
        elif reverse_flag == 'K':
            block = self.reversePartBlock(block, 1800)
        elif reverse_flag == 'L':
            block = self.reversePartBlock(block, 2000)
        elif reverse_flag == 'M':
            block = self.reversePartBlock(block, 2200)
        elif reverse_flag == 'N':
            block = self.reversePartBlock(block, 2400)
        elif reverse_flag == 'O':
            block = self.reversePartBlock(block, 2600)
        elif reverse_flag == 'P':
            block = self.reversePartBlock(block, 2800)
        elif reverse_flag == 'Q':
            block = self.reversePartBlock(block, 3000)
        elif reverse_flag == 'R':
            block = self.reversePartBlock(block, 3200)
        elif reverse_flag == 'S':
            block = self.reversePartBlock(block, 3400)
        elif reverse_flag == 'T':
            block = self.reversePartBlock(block, 3600)
        elif reverse_flag == 'U':
            block = self.reversePartBlock(block, 3800)
        elif reverse_flag == 'V':
            block = self.reversePartBlock(block, 4000) 
        elif reverse_flag == 'W':
            length = int(len(block) / 10)
            block = self.reversePartBlock2(block, 9*length, 10*length)
        elif reverse_flag == 'X':
            length = int(len(block) / 10)
            block = self.reversePartBlock2(block, 8*length, 10*length)
        elif reverse_flag == 'Y':
            length = int(len(block) / 10)
            block = self.reversePartBlock2(block, 7*length, 10*length)
        elif reverse_flag == 'Z':
            length = int(len(block) / 10)
            block = self.reversePartBlock2(block, 6*length, 10*length)
        elif reverse_flag == '1':
            length = int(len(block) / 10)
            length = 1 * length
            block = self.reversePartBlock(block, length)
        elif reverse_flag == '2':
            length = int(len(block) / 10)
            length = 2 * length
            block = self.reversePartBlock(block, length)
        elif reverse_flag == '3':
            length = int(len(block) / 10)
            length = 3 * length
            block = self.reversePartBlock(block, length)
        elif reverse_flag == '4':
            length = int(len(block) / 10)
            length = 4 * length
            block = self.reversePartBlock(block, length)
        elif reverse_flag == '5':
            length = int(len(block) / 10)
            length = 5 * length
            block = self.reversePartBlock(block, length)
        elif reverse_flag == '6':
            length = int(len(block) / 10)
            length = 6 * length
            block = self.reversePartBlock(block, length)
        elif reverse_flag == '7':
            length = int(len(block) / 10)
            length = 7 * length
            block = self.reversePartBlock(block, length)
        elif reverse_flag == '8':
            length = int(len(block) / 10)
            length = 8 * length
            block = self.reversePartBlock(block, length)
        elif reverse_flag == '9':
            length = int(len(block) / 10)
            length = 9 * length
            block = self.reversePartBlock(block, length)
        elif reverse_flag == '1a':
            length = int(len(block) / 10)
            block = self.reversePartBlock2(block, 1*length, 2*length)
        elif reverse_flag == '1b':
            length = int(len(block) / 10)
            block = self.reversePartBlock2(block, 2*length, 3*length)
        elif reverse_flag == '1c':
            length = int(len(block) / 10)
            block = self.reversePartBlock2(block, 3*length, 4*length)
        elif reverse_flag == '1d':
            length = int(len(block) / 10)
            block = self.reversePartBlock2(block, 4*length, 5*length)
        elif reverse_flag == '1e':
            length = int(len(block) / 10)
            block = self.reversePartBlock2(block, 5*length, 6*length)
        elif reverse_flag == '1f':
            length = int(len(block) / 10)
            block = self.reversePartBlock2(block, 6*length, 7*length)
        elif reverse_flag == '1g':
            length = int(len(block) / 10)
            block = self.reversePartBlock2(block, 7*length, 8*length)
        elif reverse_flag == '1h':
            length = int(len(block) / 10)
            block = self.reversePartBlock2(block, 8*length, 9*length)
        elif reverse_flag == '2a':
            length = int(len(block) / 10)
            block = self.reversePartBlock2(block, 1*length, 3*length)
        elif reverse_flag == '2b':
            length = int(len(block) / 10)
            block = self.reversePartBlock2(block, 2*length, 4*length)
        elif reverse_flag == '2c':
            length = int(len(block) / 10)
            block = self.reversePartBlock2(block, 3*length, 5*length)
        elif reverse_flag == '2d':
            length = int(len(block) / 10)
            block = self.reversePartBlock2(block, 4*length, 6*length)
        elif reverse_flag == '2e':
            length = int(len(block) / 10)
            block = self.reversePartBlock2(block, 5*length, 7*length)
        elif reverse_flag == '2f':
            length = int(len(block) / 10)
            block = self.reversePartBlock2(block, 6*length, 8*length)
        elif reverse_flag == '2g':
            length = int(len(block) / 10)
            block = self.reversePartBlock2(block, 7*length, 9*length)
        elif reverse_flag == '3a':
            length = int(len(block) / 10)
            block = self.reversePartBlock2(block, 1*length, 4*length)
        elif reverse_flag == '3b':
            length = int(len(block) / 10)
            block = self.reversePartBlock2(block, 2*length, 5*length)
        elif reverse_flag == '3c':
            length = int(len(block) / 10)
            block = self.reversePartBlock2(block, 3*length, 6*length)
        elif reverse_flag == '3d':
            length = int(len(block) / 10)
            block = self.reversePartBlock2(block, 4*length, 7*length)
        elif reverse_flag == '3e':
            length = int(len(block) / 10)
            block = self.reversePartBlock2(block, 5*length, 8*length)
        elif reverse_flag == '3f':
            length = int(len(block) / 10)
            block = self.reversePartBlock2(block, 6*length, 9*length)
        elif reverse_flag == '4a':
            length = int(len(block) / 10)
            block = self.reversePartBlock2(block, 1*length, 5*length)
        elif reverse_flag == '4b':
            length = int(len(block) / 10)
            block = self.reversePartBlock2(block, 2*length, 6*length)
        elif reverse_flag == '4c':
            length = int(len(block) / 10)
            block = self.reversePartBlock2(block, 3*length, 7*length)
        elif reverse_flag == '4d':
            length = int(len(block) / 10)
            block = self.reversePartBlock2(block, 4*length, 8*length)
        elif reverse_flag == '4e':
            length = int(len(block) / 10)
            block = self.reversePartBlock2(block, 5*length, 9*length)
        elif reverse_flag == '5a':
            length = int(len(block) / 10)
            block = self.reversePartBlock2(block, 1*length, 6*length)
        elif reverse_flag == '5b':
            length = int(len(block) / 10)
            block = self.reversePartBlock2(block, 2*length, 7*length)
        elif reverse_flag == '5c':
            length = int(len(block) / 10)
            block = self.reversePartBlock2(block, 3*length, 8*length)
        elif reverse_flag == '5d':
            length = int(len(block) / 10)
            block = self.reversePartBlock2(block, 4*length, 9*length)
        else:
            block = block
        return block

    def _encrypt2(self, filename):
        '''
        Private method to run the operations for Jigsaw version 2 
        encryption. Jigsaw version 2 encryption requires block size 
        to be at least 4096 bytes and will set any smaller block 
        size to 4096 bytes.
        
        The encryption coding write out into keyfile consist of the 
        following (in the order, delimited by '>>'):
            - 'AA'
            - block sequence (incremental integer from 0)
            - reverse flag
            - size of block (in bytes)
            - directory to write out Jigsaw file
            - name of Jigsaw file
            - truncated sha256 hash of block
        
        @param filename: name (absolute path or relative path) of file to 
        be encrypted.
        @type filename: string
        @return: number of blocks processed
        '''
        if self.block_size < 4096:
            self.block_size = 4096
        count = 0
        if self.slicer == 'even':
            print('Processing using even slicer')
            for block in self.evenSlicer(self.filename, 
                                         self.block_size):
                reverse_flag = self.rchoice(self.reverseOptions)
                block = self._blockReverse(block, reverse_flag)
                (hash, ofileName) = self._writeJigsawFile(block)
                data = '>>'.join(['AA', str(count), reverse_flag,
                                  str(len(block)), 
                                  self.outputdir, ofileName, hash])
                self.decryptkey.write(data + '\n')
                self._encryptVerbosity(count, data)
                count = count + 1
        if self.slicer == 'uneven':
            print('Processing using uneven slicer')
            for block in self.unevenSlicer(self.filename, 
                                           self.block_size, 
                                           self.block_size*2):
                reverse_flag = self.rchoice(self.reverseOptions)
                block = self._blockReverse(block, reverse_flag)
                (hash, ofileName) = self._writeJigsawFile(block)
                data = '>>'.join(['AA', str(count), reverse_flag,
                                  str(len(block)), 
                                  self.outputdir, ofileName, hash])
                self.decryptkey.write(data + '\n')
                self._encryptVerbosity(count, data)
                count = count + 1
        return count

    def _blockSwap(self, block, swap_flag):
        '''
        Private method for block swap based on fixed swapping 
        scheme.

        @param block: data to be swapped.
        @type block: string
        @param swap_flag: type of swapping. All swap flags starts 
        with 'S', followed by the number of bytes to be swapped. 
        For example, 'S300' in a block of 1000 bytes will result 
        in swapping first 300 bytes of the block with 500th to 
        799th byte.
        @type swap_flag: string
        '''
        midpoint = int(len(block) / 2)
        swap_size = int(swap_flag[1:])
        if swap_flag.startswith('S'):
            block = self.swapBlock(block, (0, swap_size), 
                (midpoint, midpoint+swap_size))
        else:
            block = block
        return block

    def _encrypt3(self, filename):
        '''
        Private method to run the operations for Jigsaw version 3 
        encryption. Jigsaw version 3 encryption requires block size 
        to be at least 16384 bytes and must be divisible by 2. Any 
        block size smaller than 16384 bytes will be set to 16384 
        bytes.
        
        The encryption coding write out into keyfile consist of the 
        following (in the order, delimited by '>>'):
            - 'AA'
            - block sequence (incremental integer from 0)
            - swap flag (all swap flags starts with 'S')
            - reverse flag 
            - size of block (in bytes)
            - directory to write out Jigsaw file
            - name of Jigsaw file
            - truncated sha256 hash of block
        
        @param filename: name (absolute path or relative path) of file to 
        be encrypted.
        @type filename: string
        @return: number of blocks processed
        '''
        if self.block_size < 16384:
            self.block_size = 16384
        count = 0
        if self.slicer == 'even':
            print('Processing using even slicer')
            for block in self.evenSlicer(self.filename, 
                                         self.block_size):
                reverse_flag = self.rchoice(self.reverseOptions)
                block = self._blockReverse(block, reverse_flag)
                swap_flag = 'S' + self.rchoice(self.swapSize)
                block = self._blockSwap(block, swap_flag)
                (hash, ofileName) = self._writeJigsawFile(block)
                data = '>>'.join(['AA', str(count), swap_flag, 
                                  reverse_flag, str(len(block)), 
                                  self.outputdir, ofileName, hash])
                self.decryptkey.write(data + '\n')
                self._encryptVerbosity(count, data)
                count = count + 1
        if self.slicer == 'uneven':
            print('Processing using uneven slicer')
            for block in self.unevenSlicer(self.filename, 
                                           self.block_size, 
                                           self.block_size*2):
                reverse_flag = self.rchoice(self.reverseOptions)
                block = self._blockReverse(block, reverse_flag)
                swap_flag = 'S' + self.rchoice(self.swapSize)
                block = self._blockSwap(block, swap_flag)
                (hash, ofileName) = self._writeJigsawFile(block)
                data = '>>'.join(['AA', str(count), swap_flag, 
                                  reverse_flag, str(len(block)), 
                                  self.outputdir, ofileName, hash])
                self.decryptkey.write(data + '\n')
                self._encryptVerbosity(count, data)
                count = count + 1
        return count

    def encrypt(self, filename, outputdir=''):
        '''
        Function to run encryption.
        
        @param filename: name (absolute path or relative path) of file to 
        be hashed.
        @type filename: string
        @param outputdir: absolute path of directory (without trailing 
        slash) to write the Jigsaw files (encrypted/sub-files) into. This 
        parameter is optional. If not given, the Jigsaw files will be in 
        the same directory as the input file or in the current working 
        directory.
        @type outputdir: string
        @return: name of keyfile.
        '''
        print('Encrypting file: %s' % filename)
        self.filename = filename
        self._setEncryptDir(outputdir)
        self.fileList = [x.split('.')[0] 
                         for x in os.listdir(self.outputdir)
                             if x.endswith('.jig')]
        print('... in input directory: %s' % self.inputdir)
        print('... onto output directory: %s' % self.outputdir)
        print('... using Jigsaw version: %s' % self.version)
        print('... using slicer: %s' % self.slicer)
        print('... using block size: %s' % str(self.block_size))
        self.checksums = self.generateHash(filename)
        self._addHeader('version', self.version)
        self._addHeader('inputdir', self.inputdir)
        self._addHeader('infile', filename)
        self._addHeader('hashlength', str(self.hashlength))
        self._addHeader('md5', self.checksums[0])
        self._addHeader('sha1', self.checksums[1])
        self._addHeader('sha224', self.checksums[2])
        self._addHeader('sha256', self.checksums[3])
        self._addHeader('sha384', self.checksums[4])
        self._addHeader('sha512', self.checksums[5])
        keyFileName = self._writeKeyHeader()
        if self.version == 'JigsawFileONE': 
            num_blocks = self._encrypt1(self.filename)
        if self.version == 'JigsawFileTWO': 
            num_blocks = self._encrypt2(self.filename)
        if self.version == 'JigsawFileTHREE': 
            num_blocks = self._encrypt3(self.filename)
        self.decryptkey.close()
        print('%s blocks processed' % str(num_blocks))
        print('Encrypting file, %s, completed' % filename)
        print('')
        return keyFileName
    
    def _readKeyFile(self):
        '''
        Private method to read and process a keyfile (.jgk) for decryption 
        and assembly.
        '''
        print('... Processing key file')
        keydata = open(self.keyfilename, 'r').readlines()
        keydata = [x[:-1].strip() for x in keydata]
        keydata = [x for x in keydata if x != '']
        self.keyhead = {}
        header = [x for x in keydata if x.startswith('#')]
        header = [x[1:].split('>>') for x in header]
        for item in header:
            self.keyhead[str(item[0]).strip()] = str(item[1]).strip()
        self.hashlength = int(self.keyhead['hashlength'])
        self.keycode = {}
        code = [x for x in keydata if not x.startswith('#')]
        code = [[str(item).strip() for item in line.split('>>')] 
                for line in code]
        codeset = list(set([x[0] for x in code]))
        '''
        Note to myself: The first 2 elements in the encryption code will 
        not be in the value of self.keycode. For example, for Jigsaw 
        version 1, the encryption code is 
        ['AA', 
         <block sequence>,
         <size of block (in bytes)>,
         <directory to write out Jigsaw file>,
         <name of Jigsaw file>
         <truncated sha256 hash of block>]

        self.keycode['AA'][<block sequence>] = \
            [<size of block (in bytes)>,
             <directory to write out Jigsaw file>,
             <name of Jigsaw file>
             <truncated sha256 hash of block>]
        '''
        for section in codeset:
            self.keycode[section] = {}
            for x in code:
                blockcount = int(x[1])
                self.keycode[section][blockcount] = x[2:]
            
    def _setDecryptDir(self, decryptfilename='', encryptdir=''):
        '''
        Private function to set the input directory and output file name 
        prior to decryption and assembly.
        
        Input directory (location of Jigsaw files): If given, it will be 
        used. If not given, it will try the following in sequence. Firstly, 
        it will attempt to set to the directory of the keyfile if name of 
        keyfile is absolute path. Secondly, it will attempt to set to the 
        directory of the decrypted file if the name is an absolute path. 
        If both attempt fails, it will set to the current working directory.
        
        Output file name (name of decrypted file): If given, it will be 
        used. Otherwise, it will use the original file name from encryption 
        as the output file name and write into the input (Jigsaw files) 
        directory.
        
        @param decryptfilename: absolute or relative file name for the 
        decrypted file.
        @type decryptfilename: string
        @param encryptdir: absolute path of directory (without trailing 
        slash) where the required Jigsaw files (encrypted/sub-files) are 
        located.
        @type encryptdir: string
        '''
        # Input directory
        print('... Sorting out input (encrypted files) directory')
        if encryptdir == '':
            print('...... Input directory is not given')
            print('...... Attempt to get input directory from keyfile name')
            if len(self.keyfilename.split(os.sep)) > 1:
                print('...... Keyfile name is absolute path: %s' % 
                    self.keyfilename)
                encryptdir = self.keyfilename.split(os.sep)[:-1]
                encryptdir = os.sep.join(encryptdir)
                print('...... Set input directory to directory of keyfile')
            elif len(decryptfilename.split(os.sep)) > 1:
                print('...... Failed: Keyfile name is relative path')
                print('...... Set input directory to output directory')
                print('       from absolute path to write unencrypted file')
                encryptdir = decryptfilename.split(os.sep)[:-1]
                encryptdir = os.sep.join(encryptdir)
                print('...... Set input directory to %s' % encryptdir)
            else:
                print('...... Failed: Output file name is relative path')
                print('...... Set input directory to currect working directory')
                encryptdir = os.getcwd()
            self.inputdir = encryptdir
        else:
            print('...... Input directory given as %s' % encryptdir)
            print('...... Set input directory to %s' % encryptdir)
            self.inputdir = encryptdir
        # Output file
        print('... Sorting out output file (unencrypted file) name')
        if decryptfilename == '':
            print('...... Output file name not given')
            print('...... Use original input source file name (unencrypted') 
            print('       file in keyfile as output file name')
            decryptfilename = self.keyhead['infile']
            print('...... Set folder to write output file as input directory')
            self.outputdir = self.inputdir
            self.decryptfilename = os.sep.join([self.outputdir, 
                                                decryptfilename])
        else:
            if len(decryptfilename.split(os.sep)) == 1:
                print('...... Given output file name is relative path: %s' % 
                    decryptfilename)
                print('...... Attempt to generate absolute output file path')
                print('...... Set folder to write output file as input directory')
                self.outputdir = self.inputdir
                self.decryptfilename = os.sep.join([self.outputdir, 
                                                    decryptfilename])
            else:
                self.decryptfilename = decryptfilename
    
    def _decryptVerbosity(self, count, data):
        '''
        Private method to generate process information based in level of 
        verbosity (1 = most information; highest verbosity) during 
        decryption.

        @param count: block sequence
        @type count: integer
        @param data: process information
        @type data: string
        '''
        if self.verbose == 1:
            self.decryptkey.write(data + '\n')
            print('Code: %s' % data)
        elif self.verbose == 2:
            self.decryptkey.write(data + '\n')
        if self.verbose > 1 and (count % 1000 == 0):
            print('%s blocks processed' % str(count))

    def _decryptSummary(self, num_blocks, expected, actual):
        '''
        Private method to display summary of decryption.

        @param num_blocks: number of Jigsaw files processed.
        @type num_blocks: integer
        @param expected: expected number of bytes to be processed.
        @type expected: integer
        @param actual: actual number of bytes processed.
        @type actual: integer
        '''
        print('%s Jigsaw files processed' % str(num_blocks))
        print('Expected number of bytes: %s' % str(expected))
        print('Actual number of bytes  : %s' % str(actual))
        self.decryptkey.write('%s Jigsaw files processed \n' % 
            str(num_blocks))
        self.decryptkey.write('Expected number of bytes: %s \n' % 
            str(expected))
        self.decryptkey.write('Actual number of bytes  : %s \n' % 
            str(actual))

    def _decrypt1(self):
        '''
        Private method to run the operations for Jigsaw version 1 
        decryption.
        '''
        print('Decrypting file ......')
        ofile = open(self.decryptfilename, 'wb')
        self.keycode = self.keycode['AA']       # for Jigsaw version 1 
        block_sequence = self.keycode.keys()
        block_sequence.sort()
        actual = 0
        expected = 0
        for b in block_sequence:
            filename = self.keycode[b][2]
            filename = os.sep.join([self.inputdir, filename])
            blocksize = self.keycode[b][0]
            block = open(filename, 'rb').read()
            hash = str(self.hash(block).hexdigest()[:self.hashlength])
            ofile.write(block)
            data = '>>'.join([str(b), filename, 
                              str(blocksize), str(len(block)),
                              self.keycode[b][3], hash])
            expected = expected + int(blocksize)
            actual = actual + len(block)
            self._decryptVerbosity(b, data)
        self._decryptSummary(len(block_sequence), expected, actual)
        ofile.close()
        
    def _decrypt2(self):
        '''
        Private method to run the operations for Jigsaw version 2 
        decryption.
        '''
        print('Decrypting file ......')
        ofile = open(self.decryptfilename, 'wb')
        self.keycode = self.keycode['AA']       # for Jigsaw version 1 
        block_sequence = self.keycode.keys()
        block_sequence.sort()
        actual = 0
        expected = 0
        for b in block_sequence:
            filename = self.keycode[b][3]
            filename = os.sep.join([self.inputdir, filename])
            blocksize = self.keycode[b][1]
            block = open(filename, 'rb').read()
            hash = str(self.hash(block).hexdigest()[:self.hashlength])
            block = self._blockReverse(block, self.keycode[b][0])
            ofile.write(block)
            data = '>>'.join([str(b), self.keycode[b][0], filename, 
                              str(blocksize), str(len(block)),
                              self.keycode[b][4], hash])
            expected = expected + int(blocksize)
            actual = actual + len(block)
            self._decryptVerbosity(b, data)
        self._decryptSummary(len(block_sequence), expected, actual)
        ofile.close()

    def _decrypt3(self):
        '''
        Private method to run the operations for Jigsaw version 3 
        decryption.
        '''
        print('Decrypting file ......')
        ofile = open(self.decryptfilename, 'wb')
        self.keycode = self.keycode['AA']       # for Jigsaw version 1 
        block_sequence = self.keycode.keys()
        block_sequence.sort()
        actual = 0
        expected = 0
        for b in block_sequence:
            filename = self.keycode[b][4]
            filename = os.sep.join([self.inputdir, filename])
            blocksize = self.keycode[b][2]
            block = open(filename, 'rb').read()
            hash = str(self.hash(block).hexdigest()[:self.hashlength])
            block = self._blockSwap(block, self.keycode[b][0])
            block = self._blockReverse(block, self.keycode[b][1])
            ofile.write(block)
            data = '>>'.join([str(b), self.keycode[b][0], 
                              self.keycode[b][1], filename, 
                              str(blocksize), str(len(block)),
                              self.keycode[b][5], hash])
            expected = expected + int(blocksize)
            actual = actual + len(block)
            self._decryptVerbosity(b, data)
        self._decryptSummary(len(block_sequence), expected, actual)
        ofile.close()

    def _compareHash(self):
        '''
        Private method to print out a series of file hashes from the 
        expected decrypted file and the actual decrypted file.
        '''
        self.checksums = self.generateHash(self.decryptfilename)
        print('File Hashs (Decrypted File vs Original Unencrypted File)')
        self.decryptkey.write('File Hashs (Decrypted File vs Original Unencrypted File) \n')
        print('md5: %s' % self.checksums[0])
        print('  vs %s' % self.keyhead['md5'])
        self.decryptkey.write('md5: %s \n' % self.checksums[0])
        self.decryptkey.write('  vs %s \n' % self.keyhead['md5'])
        print('sha1: %s' % self.checksums[1]) 
        print('  vs  %s' % self.keyhead['sha1'])
        self.decryptkey.write('sha1: %s \n' % self.checksums[1]) 
        self.decryptkey.write('  vs  %s \n' % self.keyhead['sha1'])
        print('sha224: %s' % self.checksums[2]) 
        print('  vs    %s' % self.keyhead['sha224'])
        self.decryptkey.write('sha224: %s \n' % self.checksums[2]) 
        self.decryptkey.write('  vs    %s \n' % self.keyhead['sha224'])
        print('sha256: %s' % self.checksums[3]) 
        print('  vs    %s' % self.keyhead['sha256'])
        self.decryptkey.write('sha256: %s \n' % self.checksums[3]) 
        self.decryptkey.write('  vs    %s \n' % self.keyhead['sha256'])
        print('sha384: %s' % self.checksums[4]) 
        print('  vs    %s' % self.keyhead['sha384'])
        self.decryptkey.write('sha384: %s \n' % self.checksums[4]) 
        self.decryptkey.write('  vs    %s \n' % self.keyhead['sha384'])
        print('sha512: %s' % self.checksums[5]) 
        print('  vs    %s' % self.keyhead['sha512'])
        self.decryptkey.write('sha512: %s \n' % self.checksums[5]) 
        self.decryptkey.write('  vs    %s \n' % self.keyhead['sha512'])
        
    def decrypt(self, keyfilename, decryptfilename='', encryptdir=''):
        '''
        Function to run decryption. The decryption information will be 
        stored in a file - <decryptfilename>.jkd

        @param keyfilename: absolute path to the keyfile (.jgk) required 
        for decryption.
        @type keyfilename: string
        @param decryptfilename: absolute or relative file name for the 
        decrypted file. This parameter is optional. If not given, the 
        decrypted file will be in the same directory as the keyfile or in 
        the current working directory.
        @type decryptfilename: string
        @param encryptdir: absolute path of directory (without trailing 
        slash) where the required Jigsaw files (encrypted/sub-files) are 
        located. This parameter is optional. If not given, it will be set 
        to the same directory as the keyfile or in the current working directory.
        @type encryptdir: string
        '''
        print('Decrypting file using keyfile: %s' % keyfilename)
        self.keyfilename = keyfilename
        self._readKeyFile()
        self._setDecryptDir(decryptfilename, encryptdir)
        print('... Directory of encrypted files (input): %s' % 
            self.inputdir)
        print('... Uncrypted file name (output): %s' % 
            self.decryptfilename)
        self.decryptkey = open(self.decryptfilename + '.jkd', 'w')
        if self.keyhead['version'] == 'JigsawFileONE': 
            self._decrypt1()
        if self.keyhead['version'] == 'JigsawFileTWO': 
            self._decrypt2()
        if self.keyhead['version'] == 'JigsawFileTHREE': 
            self._decrypt3()
        self._compareHash()
        print('Decryption completed')
        print('')
        self.decryptkey.close()
