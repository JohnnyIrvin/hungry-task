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

from viking.domain.seedwork.entity import Entity


def test_entity_has_id(entity: Entity):
    assert entity.id != None

def test_entity_id_is_uuid(entity: Entity):
    assert type(entity.id) == UUID

def test_entity_is_equivalent_based_on_id(uuid: UUID):
    first, second = Entity(), Entity()

    first.uuid = uuid
    second.uuid = uuid

    assert first == second

def test_non_entity_is_not_equal(entity: Entity):
    assert entity != 5

def test_entity_is_hashable(entity: Entity):
    assert hash(entity) != None

def test_entity_hash_is_based_on_id(uuid: UUID):
    first, second = Entity(), Entity()

    first.uuid = uuid
    second.uuid = uuid

    assert hash(first) == hash(second)
