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

import pytest

from viking.domain.seedwork.entity import Entity
from viking.domain.task import Task


def test_task_has_name(task):
    assert task.name == "Task Name"

def test_task_without_name_throws_type_error():
    with pytest.raises(TypeError):
        Task()

def test_task_not_completed(task):
    assert not task.completed

def test_task_completed(task):
    task.complete()

    assert task.completed

def test_task_completed_set_throws_error(task):
    with pytest.raises(AttributeError):
        task.completed = True

def test_task_complete_returns_task(task):
    returned = task.complete()

    assert type(returned) == Task

def test_task_completed_twice_throws_already_completed(task):
    with pytest.raises(Task.AlreadyCompletedError):
        task.complete().complete()

def test_completed_task_is_same_task(task):
    completed = task.complete()

    assert completed == task

def test_completed_task_has_same_name(task):
    completed = task.complete()

    assert completed.name == task.name

def test_task_has_id(task):
    assert task.id != None

def test_task_id_is_uuid(task):
    assert type(task.id) == UUID

def test_task_is_entity(task):
    assert issubclass(type(task), Entity)

