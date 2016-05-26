'''
Jigsaw Encryption System
Date created: 25th May 2016
Licence: Python Software Foundation License version 2
'''

import os
import random
import hashlib

class JigsawCore(object):

    hash = hashlib.sha256
    
    def __init__(self):
        pass
    
    def evenSlicer(self, filename, block_size=4096):
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
        f = open(filename, 'rb')
        block = True
        while block:
            block_size = int(max_block_size) - int(min_block_size)
            block_size = int(random.random() * block_size)
            block_size = int(min_block_size) + block_size
            block = f.read(block_size)
            yield block
        f.close()
        
    def generateHash(self, filename):
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
    def __init__(self):
        self.version = 'JigsawFileONE'
        self.decryptkey = []
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

    def setting(self, key, value):
        key = str(key).lower()
        if key == 'slicer':
            if str(value).lower() == 'uneven':
                self.slicer = 'uneven'
            else:
                self.slicer = 'even'
        elif key == 'blocksize':
            self.block_size = int(value)
        elif key == 'filenamelength':
            self.filename_length = int(value)
        elif key == 'version':
            if key == 1:
                self.version == 'JigsawFileONE'
        elif key == 'hashlength':
            self.hashlength = int(value)

    def _generateFilename(self):
        mapping = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A',
                   'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                   'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                   'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'd', 'e', 'g',
                   'h', 'q', 'r', 't']
        while True:
            randomName = [random.choice(mapping) 
                          for i in range(self.filename_length)]
            randomName = ''.join(randomName) + '.jig'
            if randomName not in self.fileList:
                self.fileList.append(randomName)
                return randomName

    def _setEncryptDir(self, outputdir=''):
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

    def _writeJigsawFile(self, count, block):
        ofileName = self._generateFilename()
        ofile = open(self.outputdir + os.sep + ofileName, 'wb')
        hash = str(self.hash(block).hexdigest()[:self.hashlength])
        ofile.write(block)
        data = '>>'.join([str(count), str(len(block)), 
                          self.outputdir, ofileName, hash])
        self.decryptkey.append(data)
        print('Code: %s' % data)
        ofile.close()

    def _writeKeyFile(self):
        if len(self.filename.split(os.sep)) == 1:
            filename = self.filename
        else:
            filename = self.filename.split(os.sep)[-1]
        kfileName = os.sep.join([self.outputdir, filename + '.jgk'])
        print('Writing key file: %s' % kfileName)
        ofile = open(kfileName, 'w')
        header = ['>>'.join(['#version', self.version]),
                  '>>'.join(['#inputdir', self.inputdir]),
                  '>>'.join(['#infile', filename]),
                  '>>'.join(['#hashlength', str(self.hashlength)]),
                  '>>'.join(['#md5', self.checksums[0]]),
                  '>>'.join(['#sha1', self.checksums[1]]),
                  '>>'.join(['#sha224', self.checksums[2]]),
                  '>>'.join(['#sha256', self.checksums[3]]),
                  '>>'.join(['#sha384', self.checksums[4]]),
                  '>>'.join(['#sha512', self.checksums[5]])]
        for line in header:
            ofile.write(line + '\n')
        for line in self.decryptkey:
            ofile.write(line + '\n')
        ofile.close()
        return kfileName

    def _encrypt1(self, filename):
        count = 0
        if self.slicer == 'even':
            print('Processing using even slicer')
            for block in self.evenSlicer(self.filename, 
                                         self.block_size):
                self._writeJigsawFile(count, block)
                count = count + 1
        if self.slicer == 'uneven':
            print('Processing using uneven slicer')
            for block in self.unevenSlicer(self.filename, 
                                           self.block_size, 
                                           self.block_size*2):
                self._writeJigsawFile(count, block)
                count = count + 1

    def encrypt(self, filename, outputdir=''):
        print('Encrypting file: %s' % filename)
        self.filename = filename
        self._setEncryptDir(outputdir)
        print('... in input directory: %s' % self.inputdir)
        print('... onto output directory: %s' % self.outputdir)
        print('... using Jigsaw version: %s' % self.version)
        print('... using slicer: %s' % self.slicer)
        print('... using block size: %s' % str(self.block_size))
        self.decryptkey = []
        self.checksums = self.generateHash(filename)
        if self.version == 'JigsawFileONE': 
            self._encrypt1(self.filename)
        keyFileName = self._writeKeyFile()
        print('')
        return keyFileName
    
    def _readKeyFile(self):
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
        for x in code:
            blockcount = int(x[0])
            self.keycode[blockcount] = x[1:]
            
    def _setDecryptDir(self, decryptfilename='', encryptdir=''):
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
    
    def _decrypt1(self):
        print('Decrypting file ......')
        ofile = open(self.decryptfilename, 'wb')
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
            self.decryptkey.append(data)
            expected = expected + int(blocksize)
            actual = actual + len(block)
            print('Code: %s' % data)
        print('%s encrypted files processed' % str(len(block_sequence)))
        print('Expected number of bytes: %s' % str(expected))
        print('Actual number of bytes  : %s' % str(actual))
        ofile.close()
        
    def _compareHash(self):
        self.checksums = self.generateHash(self.decryptfilename)
        print('File Hashs (Decrypted File vs Original Unencrypted File)')
        print('md5: %s' % self.checksums[0])
        print('  vs %s' % self.keyhead['md5'])
        print('sha1: %s' % self.checksums[1]) 
        print('  vs  %s' % self.keyhead['sha1'])
        print('sha224: %s' % self.checksums[2]) 
        print('  vs    %s' % self.keyhead['sha224'])
        print('sha256: %s' % self.checksums[3]) 
        print('  vs    %s' % self.keyhead['sha256'])
        print('sha384: %s' % self.checksums[4]) 
        print('  vs    %s' % self.keyhead['sha384'])
        print('sha512: %s' % self.checksums[5]) 
        print('  vs    %s' % self.keyhead['sha512'])
        
    def decrypt(self, keyfilename, decryptfilename='', encryptdir=''):
        print('Decrypting file using keyfile: %s' % keyfilename)
        self.keyfilename = keyfilename
        self._readKeyFile()
        self._setDecryptDir(decryptfilename, encryptdir)
        print('... Directory of encrypted files (input): %s' % 
            self.inputdir)
        print('... Uncrypted file name (output): %s' % 
            self.decryptfilename)
        self.decryptkey = []
        if self.keyhead['version'] == 'JigsawFileONE': 
            self._decrypt1()
        self._compareHash()
