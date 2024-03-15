def get_root_directory():
    import os
    currentDirectory = os.path.dirname(__file__)
    rootDirectory = os.path.abspath(os.path.join(currentDirectory, os.pardir))
    return rootDirectory
