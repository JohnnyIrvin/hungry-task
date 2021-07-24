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
from uuid import UUID

from viking.domain.seedwork import AbstractRepository, Entity


def test_repository_add_entity(repo: AbstractRepository, entity: Entity):
    repo.add(entity)

    assert repo.get(entity.id) == entity

def test_repository_add_entity_with_duplicate_id(repo: AbstractRepository, entity: Entity):
    repo.add(entity)
    repo.add(entity)

    assert repo.get(entity.id) == entity

def test_repository_duplicate_entity_count_increases_by_one(repo: AbstractRepository, entity: Entity):
    for _ in range(3, 5):
        repo.add(entity)

    assert repo.count == 1

def test_add_entities_with_different_ids(uuid: UUID, repo: AbstractRepository, entity: Entity):
    second_entity: Entity = Entity()
    second_entity.id = uuid
    
    repo.add(entity)
    repo.add(second_entity)

    assert repo.get(entity.id) == entity
    assert repo.get(uuid) == second_entity

def test_remove_entity(repo: AbstractRepository, entity: Entity):
    repo.add(entity)
    repo.remove(entity)

    assert repo.get(entity.id) is None

def test_add_three_different_entities_list_three_entities(repo: AbstractRepository):
    expected = [Entity(), Entity(), Entity()]

    for e in expected:
        repo.add(e)
        assert e in repo.list()
