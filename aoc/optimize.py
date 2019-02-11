#
# Module contains ptimization routines.
#

import copy

def minimize_variable(func, obj, variable, debug=False):
    """
    Performs a binary search to find the minimum value of variable that
    returns anything other than None when calling func with obj.  Object 
    obj is deepcopied before each execution of func.  When minimum value
    is found, a tuple is returned that contains the value of the variable
    and the return of func at that variable.
    """

    min_state = None
    hi = None
    lo = None

    test_value = int(variable)
    done = False
    iters = 0
    while not done:
       
        if debug:
            print 'Testing value:', test_value
            
        # run the test
        test_obj = copy.deepcopy(obj)
        result = func(test_obj, test_value)
        
        # set the watermark
        if result:
            if debug:
                print 'PASS', result
            hi = test_value
            min_state = result
        else:
            if debug:
                print 'FAIL'
            lo = test_value

        # determine next test value
        if hi == None:
            test_value *= 2
        elif lo == None:
            test_value /= 2
        else:
            test_value = (hi + lo) / 2

        # bounds check to make we don't rerun a test
        if test_value == lo:
            test_value += 1
        if test_value == hi:
            test_value -= 1

        # check for completion
        if hi and lo and lo + 1 == hi:
            done = True

    return min_state




