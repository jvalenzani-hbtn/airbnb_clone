#!/usr/bin/python3
import json

class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__,obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes to file"""
        json_objs = {}
        try:
            # cannot directly dump because datetime is not serializable
            for k in FileStorage.__objects:
                json_objs[k] = FileStorage.__objects[k].to_dict()
            with open(FileStorage.__file_path, "w+") as f:
                json.dump(json_objs, f)
        except TypeError as e:
            print("[ERROR]: ", e)

    def reload(self):
        """De-serializes to __objects"""
        try:
            with open(FileStorage.__file_path) as f:
                json_objs = json.load(f)
            for v in json_objs.values():
                from models.base_model import BaseModel
                self.new(eval(v["__class__"])(**v))
        except IOError:
            pass