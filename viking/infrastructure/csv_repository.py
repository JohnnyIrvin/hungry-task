# Copyright (c) 2021 Johnathan P. Irvin
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
from csv import DictReader, DictWriter
from dataclasses import asdict
from distutils.util import strtobool
from os import remove, stat
from os.path import exists as file_exists
from typing import List, cast

from viking.domain.seedwork.abstract_repository import AbstractRepository
from viking.domain.seedwork.entity import Entity


class CsvRepository(AbstractRepository):
    def __init__(self, filename: str, entity_type: type):
        """
        Initialize the CSV repository

        Args:
            filename (str): The filename to use for the CSV repository
            entity_type (type): The type of entity to use for the CSV repository
        """
        self.filename = filename
        self.type = entity_type

    def _file_empty(self) -> bool:
        """
        Check if the file is empty

        Returns:
            bool: True if the file is empty, False otherwise
        """
        if not file_exists(self.filename):
            return True
        return stat(self.filename).st_size == 0

    def add(self, entity: Entity) -> None:
        with open(self.filename, 'a+', encoding='UTF8', newline='') as f:
            fields = list(asdict(entity).keys())
            writer = DictWriter(f, fieldnames=fields)
            if self._file_empty():
                writer.writeheader()
            writer.writerow(asdict(entity))

    def remove(self, entity: Entity) -> Entity:
        stored = self.list()
        if file_exists(self.filename):
            remove(self.filename)
        
        for s in stored:
            if str(entity.id) != str(s.id):
                self.add(s)

    def get(self, reference) -> Entity:
        stored = self.list()

        for s in stored:
            if str(s.id) == str(reference):
                return s

    def _cast_field_to_type(self, entity: object, field: str, value: str) -> object:
        """
        Cast the field to the correct type

        Args:
            entity (object): The entity to cast the field to
            field (str): The field to cast
            value (str): The value to cast

        Returns:
            object: The casted value
        """
        target_type = type(getattr(entity, field))
        if target_type == bool:
            casted = strtobool(value)
        elif target_type == callable:
            casted = target_type(value)
        else:
            casted = cast(target_type, value)

        return casted

    def list(self) -> List[Entity]:
        return_list = []
        try:
            with open(self.filename, encoding='UTF8', newline='') as f:
                for row in DictReader(f):
                    entity = self.__new__(self.type)
                    for field in row:
                        setattr(entity, field, self._cast_field_to_type(entity, field, row[field]))
                    return_list.append(entity)
        except FileNotFoundError:
            pass
        return return_list
