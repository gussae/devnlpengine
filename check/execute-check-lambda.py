from importlib import import_module
from os.path import abspath
import sys
def executeCheck(functionResourceName, event, context) :
    srcPath = abspath("../amplify/backend/function/" + functionResourceName + "/src")
    sys.path.append(srcPath)
    index = import_module('index')
    return index.handler(event, context)



#! use function resource name : the folder containing your lambda
#comment out unused functions
functionResourceName = "nlpengineTest"

#execute check your lambda with proper input
event = {'a': 1}

# context in execute-check has no meaning 
context = {}

print(executeCheck(functionResourceName, event, context))