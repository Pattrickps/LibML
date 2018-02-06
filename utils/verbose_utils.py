def describe_class(class_obj):
    print ( "The class {0} contains the following methods: ".format(class_obj))
    function_list = dir(class_obj)
    for fn in function_list:
        if fn[:1] != "_":
            print("Method name: " + fn),
            print("  Method arguments: " + str(getattr(class_obj, fn).func_code.co_varnames))
    print(" ")


def describe_function(class_obj, param, variable_list):
    for variable in variable_list:
        if param == None:
            print("Value of {0} : {1}".format(variable, getattr(class_obj, variable)))
        else:
            print(" {0} of {1} : {2} ".format(param, variable, getattr(getattr(class_obj, variable), param)))
