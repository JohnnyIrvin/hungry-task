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
from typing import Dict, List
from uuid import UUID

from viking.domain.seedwork.abstract_repository import AbstractRepository
from viking.domain.seedwork.entity import Entity


class FakeRepository(AbstractRepository):
    """
    Fake repository for testing purposes.
    """
    _entities: Dict[UUID, Entity]
    
    def __init__(self, entities: Dict[UUID, Entity] = None):
        """
        Constructor.

        Args:
            entities (Dict[UUID, Entity]): The entities to add to the repository.
        """
        if entities is None:
            entities = dict()
        self._entities = entities

    def add(self, entity: Entity):
        """
        Add an entity to the repository.

        Args:
            entity (Entity): The entity to add.
        """
        self._entities[entity.id] = entity

    def get(self, reference: UUID) -> Entity:
        """
        Get an entity from the repository.

        Args:
            reference (UUID): The reference of the entity to get.

        Returns:
            Entity: The entity.
        """        
        return self._entities.get(reference)

    def remove(self, entity: Entity) -> Entity:
        """
        Remove an entity from the repository.

        Args:
            entity (Entity): The entity to remove.

        Returns:
            Entity: The entity.
        """
        return self._entities.pop(entity.id)

    def list(self) -> List[Entity]:
        """
        List all entities in the repository.

        Returns:
            list: The list of entities.
        """
        return self._entities.values()

    @property
    def count(self) -> int:
        """
        Get the number of entities in the repository.

        Returns:
            int: The number of entities.
        """
        return len(self._entities)
