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
from abc import ABC, abstractmethod
from typing import List

from viking.domain.seedwork.entity import Entity


class AbstractRepository(ABC):
    @abstractmethod
    def add(self, entity: Entity):
        """
        Add an entity to the repository.

        Args:
            entity (Entity): The entity to add.
        """

    @abstractmethod
    def get(self, reference) -> Entity:
        """
        Get an entity from the repository.

        Args:
            reference: The reference of the entity to get.

        Returns:
            Entity: The entity.
        """       

    @abstractmethod
    def remove(self, entity: Entity) -> Entity:
        """
        Remove an entity from the repository.

        Args:
            entity (Entity): The entity to remove.

        Returns:
            Entity: The entity.
        """

    @abstractmethod
    def list(self) -> List[Entity]:
        """
        List all entities in the repository.

        Returns:
            list: The list of entities.
        """
