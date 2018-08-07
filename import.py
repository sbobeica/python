To 'import' a module:
    import importlib
    import sys
    sys.path

In sys.path should be included the path to the module/library
To include a new path to the sys.path, to do next:
    sys.path.append('D:\python')
then importe the implicit module/library:
    import name_of_Module

    dir() - diplays the names in the main name space (__name__)
    dir(module/library) - will display the name into that module/library

    importlib.reload(module_To_Reload) - to reload a module/library if it was updated