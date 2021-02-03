import importlib.util

def import_module(module_name, file_path):
    spec_module = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec_module)
    spec_module.loader.exec_module(module)

    return module
