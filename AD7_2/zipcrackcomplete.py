import zipfile
import threading
import optparse


def extractFile(zfile, password):
    try:
        with zipfile.ZipFile(zfile) as zip_file:
            zip_file.extractall(path="D:\\", pwd=password.encode())
            print(f"Successfully extracted {zfile} with password {password}")
    except:
        pass


def read_passwords_from_file(password_file_path):
    with open(password_file_path, 'r') as file:
        passwords = file.read().splitlines()
    return passwords


def main():
    parser = optparse.OptionParser("usage%prog "+\
                                   "-f <zipfile> -d <dictionary>")
    parser.add_option('-f', dest='zname', type='string',\
                      help='specify zip file')
    parser.add_option('-d', dest='dname', type='string',\
                      help='specify dictionary file')
    (options, args) = parser.parse_args()
    if (options.zname == None) | (options.dname == None):
        print(parser.usage)
        exit(0)
    else:
        zname = options.zname
        dname = options.dname
    passwords = read_passwords_from_file(dname)
    for password in passwords:
        t = threading.Thread(target=extractFile, args=(zname, password))
        t.start()


# Call the main function to crack the zip file
if __name__ == '__main__':
    main()
