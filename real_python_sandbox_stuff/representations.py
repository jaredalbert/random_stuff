# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 19:44:32 2022

@author: Windows10
"""

class AsDictionaryMixin:
    def to_dict(self):
        return {
           prop: self._represent(value)
           for prop, value in self.__dict__.items()
           if not self._is_internal(prop)
           }
    def _represent(self, value):
        if isinstance(value, object):
            if hasattr(value, 'to_dict'):
                return value.to_dict()
            else:
                return str(value)
        else:
            return value
    def _is_internal(self,prop):
        return prop.startswith('_')