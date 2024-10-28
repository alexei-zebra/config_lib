# conflib.py
# config lib v1.0
# Copyright (C) 2022  Alex Zebra


class Config:
    data:dict = {}
    
    cfg_name:str = None
    file_path:str = None
    
    
    def __init__(self, cfg_name:str, file_path:str = None) -> None:
        self.cfg_name = cfg_name
        self.file_path = file_path

        with open(file_path,'r') as file:
            data_:list[str] = [string for string in file.readlines()]
            self.__parse(data_)


    def get_element(self, var_name:str):
        return self.data[var_name]


    def __parse(self, data_:list[str]):
        for string in data_:
            string = string.strip()
            
            if (string == '') or (string[0] == '#'):
                continue
            
            if '#' in string:
                string = string.split('#')[0]
            
            value_name, value = string.split('=', 1)
            value_name = value_name.strip()
            value = value.strip()

            if len(value) == 0:
                self.data[value_name] = None

            elif value in ("true","false"):
                self.data[value_name] = bool(value)

            elif value.isdigit():
                self.data[value_name] = int(value)

            elif value[0] == value[-1] and value[0] in "'\"":
                self.data[value_name] = value[1:-1]

            elif value[-1] == 'f':
                    self.data[value_name] = float(value[:-1])

            else:
                raise ValueError(f"'{value_name}' value<{value}> is not in [bool, int, str, float]") from None



class Configs:
    configs:dict = {}
    
    def __init__(self, cfg_name:str = None, file_path:str = None) -> None:
        if cfg_name:
            self.add_config(cfg_name=cfg_name, file_path=file_path)

    def add_config(self, cfg_name:str, file_path:str = None):
        file_path = f"{file_path}" if file_path != None else f"config/{cfg_name}.cfg"
        config = Config(cfg_name, file_path)
        self.configs[cfg_name] = config

    def get_config(self, name:str):
        return self.configs[name]


if __name__ == "__main__":
    print("\n !!! TEST CONFRLIB !!! ")
    confs = Configs()
    print("\n       TEST CONF       \n")
    confs.add_config("test", "test/testconflib.cfg")
    conf:Config = confs.get_config("test")
    print(conf.data)
    print(' =')
    print({"aboba": 5, "name": "alex","id": 'b2c3d7f=', "fl": 5.8})
    print("\n= = = = = = = =\n")
    print(conf.get_element("name"))
    print(' =')
    print("alex")
    print("\n !!! END TEST CONFLIB !!! \n")