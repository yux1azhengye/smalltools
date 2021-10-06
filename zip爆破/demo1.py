import zipfile
import argparse
import os
from os.path import *

def tryZipPwd(zipFile, password, savePath):
    try:
        print(password.encode('utf-8'),type(password.encode('utf-8')))
        zipFile.extractall(path=savePath, pwd=password.encode('utf-8'))
        print('[+] Zip File decompression success,password: %s' % (password))
        return True
    except:
        print('[-] Zip File decompression failed,password: %s' % (password))
        return False


def main():

    parser = argparse.ArgumentParser(description='Brute Crack Zip')

    parser.add_argument('-f', dest='zFile', type=str, help='The zip file path.')
    parser.add_argument('-w', dest='pwdFile', type =str, help='Password dictionary file.')
    zFilePath = None
    pwdFilePath = None
    try:
        options = parser.parse_args()
        zFilePath = options.zFile
        pwdFilePath = options.pwdFile
    except:
        print(parser.parse_args(['-h']))
        exit(0)

    if zFilePath == None or pwdFilePath == None:
        print(parser.parse_args(['-h']))
        exit(0)

    with zipfile.ZipFile(zFilePath) as zFile:
        with open(pwdFilePath) as f:
            for pwd in f.readlines():
                p,f = split(zFilePath)
                dirName = f.split('.')[0]
                dirPath = join(p, dirName)
                try:
                    os.mkdir(dirPath)
                except:
                    pass
                ok = tryZipPwd(zFile, pwd.strip('\n'), dirPath)#这里的strip很重要,不要漏
                if ok:
                    break
if __name__ == '__main__':
    main()