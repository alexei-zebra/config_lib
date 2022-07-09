# config lib v1.0  by zebra
class Config:
    def __init__(self) -> None:
        self._configs = {}
    def new_config(self, name :str, path = None):
        path = path if path else f"config/{name}.cfg"
        with open(path,'r') as file:
            config = {}
            for string in file.readlines():
                string = string.strip()
                if string[0] == '#':
                    continue
                value_name, value = string.split('=')
                config[value_name.strip()] = value.strip()
        self._configs[name] = config
    def get_config(self, name = None):
        return self._configs[name] if name else self._configs