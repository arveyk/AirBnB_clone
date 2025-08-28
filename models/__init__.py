#!/usr/bin/python3
"""__init__ magic method for models directory"""
<<<<<<< HEAD
#from models.engine.file_storage import FileStorage
from .engine.file_storage import FileStorage
=======
from .models.engine.file_storage import FileStorage

>>>>>>> 7663981 (Resolve rebase)

__all__ = ['base_model']
storage = FileStorage()
storage.reload()
