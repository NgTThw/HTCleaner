import os
import pickle
import module #pip install module-thw


class Config:
    def __init__(self, name) -> None:
        self._path = module.Path(__file__).app.join(name+".config")
        self._data = {}

    def setup(self, *args) -> ConfigGroup:
        """
        Format: tuple(name, getter, setter, default)
        """
        keys = []
        for d in args:
            default = d[3] if len(d) >= 4 else None
            self._data[d[0]] = {
                "value": default,
                "getter": d[1],
                "setter": d[2],
            }
            keys.append(d[0])
        return ConfigGroup(self, keys)

    def load(self, keys: list|tuple = None) -> dict:
        data = self.read_source()
        array_key = data.keys() if not keys else keys
        for k in array_key:
            if k in self._data and k in data:
                self._data[k]["value"] = data[k]
        for k in self._data.keys():
            if not keys or k in keys:
                if self._data[k]["setter"] is not None:
                    self._data[k]["setter"](self._data[k]["value"])
        return data

    def upgrade(self, keys: list|tuple = None) -> None:
        data = self.read_source()
        for k in self._data.keys():
            if not keys or k in keys:
                if self._data[k]["getter"] is not None:
                    self._data[k]["value"] = self._data[k]["getter"]()
            data[k] = self._data[k]["value"]
        self.save(data)
    
    def read_source(self) -> dict:
        if not os.path.isfile(self._path):
            self.save({})
            return {}
        with open(self._path, "rb") as f:
            data = pickle.load(f)
        return data
    
    def save(self, data) -> None:
        with open(self._path, "wb") as f:
            pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
    
    def is_value_changed(self) -> bool:
        for k in self._data.keys():
            if self._data[k]["getter"] is not None:
                if self._data[k]["value"] != self._data[k]["getter"]():
                    return True
        return False


class ConfigGroup:
    def __init__(self, parent: Config, keys: list):
        self.parent = parent
        self.keys = keys
    
    def add(self, key: str):
        self.keys.append(key)
    
    def remove(self, key: str):
        self.keys.remove(key)
    
    def load(self):
        return self.parent.load(self.keys)
    
    def upgrade(self):
        return self.parent.upgrade(self.keys)
