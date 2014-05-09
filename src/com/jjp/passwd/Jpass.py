#!usr/bin/env python
import sys


def chngPass():
    # Changes the password
    print 'in chngPass'
    sys.exit(0)


def auth(passwd):
    # a foolish little authentication method
    print 'in auth'
    try:
        hashfile = open('hashfile', 'rU')
    except IOError:
        # If the hashfile is not thier then the user
        # is logging in for the first time so this generates the hashfile
        print 'will now generate the pass..........'
        print '\n\t\tWelcome to JPASS\n\n'
        print 'this is just the prototype so be concecious about the security'
        print '\nPlease enter your new password:'
        print 'Please confirm your password:'
        hashfile = open('hashfile', 'w')
        print 'Creating hashfile.........'
        auth(passwd)

    for hashpass in hashfile:
        if hashpass == passwd:
            print 'true'
    sys.exit(0)


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

            elif arg == '-h':
                print 'will display help'

            elif arg == '-c':
                print 'will change passwd'
        else:
            print 'Please enter a valid argument or "jpass -h" for help'
# If no arguments are provided then the program guesses that you want to
# autherise with the password
    print '\n\t\tWelcome to JPASS\n\n\n'
    print '(if you are logging for the first time just press enter)\n'
    print 'Enter Password:',

if __name__ == '__main__':
    main()
