#!/usr/bin/python3
"""__init__ magic method for models directory"""
from .engine.file_storage import FileStorage

#__all__ = ['base_model']
storage = FileStorage()
storage.reload()
