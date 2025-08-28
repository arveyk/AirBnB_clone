#!/usr/bin/python3
import datetime


class NewClass():
    def __init__(self, name):
        print(name)
    def to_dict(self):
        inst_dict = self.__dict__
        inst_dict['__class__'] = self.__class__.__name__
        created_at = datetime.datetime.now().isoformat()
        updated_at = datetime.datetime.now().isoformat()
        inst_dict['__class2__'] = NewClass.__name__
        inst_dict['created_at'] = created_at
        inst_dict['updated_at'] = updated_at

        return inst_dict

nc = NewClass('Henry')
print(nc.to_dict())
