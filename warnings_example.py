import warnings


def deprecated_function():
    warnings.warn("This function is deprecated", DeprecationWarning)
    return 'x'


def some_function():
    # with warnings.catch_warnings():
    #     warnings.simplefilter("ignore")
    print(deprecated_function())


some_function()
        