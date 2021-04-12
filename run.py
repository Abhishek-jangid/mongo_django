import argparse
import os
import sys


def execfile(filepath, globals=None, locals=None):
    if globals is None:
        globals = {}
    globals.update({
        "__file__": filepath,
        "__name__": "__main__",
    })
    with open(filepath, 'rb') as file:
        exec(compile(file.read(), filepath, 'exec'), globals, locals)


def isArgPresent(name, args):
    temp = vars(args)
    if temp[name]:
        return True
    else:
        return False


parser = argparse.ArgumentParser()
requiredNamed = parser.add_argument_group('required named arguments')
parser.add_argument('-v', help='Path to virtualenv bin activate.py')
requiredNamed.add_argument('-p', help='<APPNAME>.<file.py>')
requiredNamed.add_argument('-f', help='Function name in argument specified by -p')
parser.add_argument('-a', help='Arguments separated by comma(,) for function specified by -f')

args = parser.parse_args()

required = ['p', 'f']
if (not all(isArgPresent(d, args) for d in required)):
    print('required named arguments: ', required)
else:
    os.environ['DJANGO_SETTINGS_MODULE'] = 'mongo_django.settings'

    originalWorkingDir = os.getcwd()

    runContainingDir = os.path.abspath(os.path.dirname(__file__))
    sys.path.append(runContainingDir)
    # Changing directory to run.py containing directory
    os.chdir(runContainingDir)

    if args.v:
        execfile(os.getcwd() + '/' + args.v)

    moduleName = args.p

    if args.a:
        funcArgs = args.a.split(',')
        functionName = ' ' + args.f + '('
        for funcArg in funcArgs:
            functionName = functionName + '"' + funcArg + '",'
        if functionName:
            functionName = functionName[:-1] + ')'
    else:
        functionName = ' ' + args.f + '()'
    print('Executing: import django;django.setup()')
    exec('import django;django.setup()')
    print('Executing: import %s' % moduleName)
    exec('import %s' % moduleName)
    print('Executing: %s.%s' % (moduleName, functionName))
    exec('%s.%s' % (moduleName, functionName))

    # Changing directory to orignial caller directory
    os.chdir(originalWorkingDir)

# USAGE:
# python3 run.py -h

# Keep this file in your code repository root
# Command to run in cron or on console
# Can be run from anywhere and -v can take relative or absolute path both
# python3 run.py -p <appname>.<filename> -f <functionName> -a 123,123 -v finZenv/bin/activate_this.py
