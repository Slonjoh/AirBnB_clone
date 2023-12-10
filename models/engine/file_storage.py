#!/usr/bin/python3
"""
FileStorage module.
"""

import json
from datetime import datetime
import os


class FileStorage:
    """
    FileStorage class.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        serialized_objects = {}
        for key, value in FileStorage.__objects.items():
            serialized_objects[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """
        Deserializes the JSON file to __object.
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.user import User
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.amenity import Amenity
        from models.review import Review
        dict_class = {"Amenity": Amenity, "BaseModel": BaseModel,
                      "City": City, "Place": Place, "Review": Review,
                      "State": State, "User": User}

        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                for key, value in json.load(f).items():
                    self.new(dict_class[value['__class__']](**value))
