#!usr/bin/env python
import sys
import hashlib


def chngPass():
    # Changes the password
    print 'in chngPass'
    passwd = raw_input('\nPlease enter your Password: ')
    if auth(passwd):
        print 'you are now going to change your password'
        passwd1 = raw_input('\nPlease enter your new password: ')
        passwd2 = raw_input('\nPlease conform your password: ')
        if passwd1 == passwd2:
            m = hashlib.sha1(passwd1)
            print m.hexdigest()
            hashfile = open('hashfile', 'w+')
            hashfile.write(m.hexdigest())
            hashfile.close()
    else:
        print 'ERROR You entered the wrong password!!!'
        sys.exit(0)


def auth(passwd):
    # a foolish little authentication method
    print 'in auth'
    try:
        hashfile = open('hashfile', 'r')

    except IOError:
        # If the hashfile is not there then the user
        # is logging in for the first time so this generates the hashfile
        print 'this is just the prototype so be concecious about the security'
        print 'will now generate the pass..........'
        passwd1 = raw_input('\nPlease enter your new password: ')
        passwd2 = raw_input('Please confirm your password: ')
        if passwd1 == passwd2:
            hashfile = open('hashfile', 'w')
            m = hashlib.sha1(passwd1)  # hashes the password
            hashfile.write(m.hexdigest())
            print 'Creating hashfile.........'
            hashfile.close()
            auth(passwd)
        print "\n\t\tpasswords don'nt match!!!!\n"
        auth(passwd)

    hashpass = hashfile.read()
    m = hashlib.sha1(passwd)
    hashfile.close()
    if hashpass == m.hexdigest():
        return True
    return False


def main():
    # print sys.argv
    args = sys.argv[1:]
    # This is a custom parser since this program only takes 3 arguments
    for arg in args:
        if arg == '-s' or arg == '-h' or arg == '-c':

            if arg == '-s':
                try:
                    auth(args[1])
                except IndexError:
                    print 'please enter the password!'
                sys.exit(0)

            elif arg == '-h':
                print 'will display help'

            elif arg == '-c':
                chngPass()
        else:
            print 'Please enter a valid argument or "jpass -h" for help'
    # If no arguments are provided then the program guesses that you want to
    # autherise with the password
    print '\n\t\tWelcome to JPASS\n\n\n'
    print '(if you are logging for the first time just press enter)\n'
    passwd = raw_input('Enter Password: ')
    auth(passwd)

if __name__ == '__main__':
    main()
