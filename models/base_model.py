#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
from models import storage

datetime_format = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.now()
        if kwargs:
            for k,v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    v = datetime.strptime(v, datetime_format)
                if k != "__class__":
                    setattr(self, k, v)
        else:
            storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)


    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        d = self.__dict__.copy()
        d["__class__"] = self.__class__.__name__
        d["created_at"] = self.created_at.isoformat()
        d["updated_at"] = self.updated_at.isoformat()
        return d
