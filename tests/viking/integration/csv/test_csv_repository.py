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
from viking.domain.task import Task
from viking.infrastructure.csv_repository import CsvRepository


def test_csv_repository_save(task: Task, repo: CsvRepository):
    repo.add(task)
    assert repo.get(task.id).name == task.name

def test_csv_repository_save_multiple(task: Task, repo: CsvRepository):
    repo.add(task)
    repo.add(task)
    assert repo.get(task.id).name == task.name

def test_csv_get_all(repo: CsvRepository):
    repo.add(Task('Task One'))
    repo.add(Task('Task Two'))
    assert len(repo.list()) == 2

def test_remove(task: Task, repo: CsvRepository):
    repo.add(task)
    repo.remove(task)
    assert len(repo.list()) == 0

def test_remove_multiple(task: Task, repo: CsvRepository):
    repo.add(task)
    repo.add(task)
    repo.remove(task)
    assert len(repo.list()) == 0

def test_remove_nonexistent(task: Task, repo: CsvRepository):
    repo.remove(task)
    assert len(repo.list()) == 0

def test_remove_multiple_nonexistent(task: Task, repo: CsvRepository):
    repo.remove(task)
    repo.remove(task)
    assert len(repo.list()) == 0

def test_remove_all(repo: CsvRepository):
    tasks = [Task('Task One'), Task('Task Two')]
    for task in tasks:
        repo.add(task)
        repo.remove(task)
    assert len(repo.list()) == 0

def test_list_empty(repo: CsvRepository):
    assert len(repo.list()) == 0

def test_list_multiple(repo: CsvRepository):
    tasks = [Task('Task One'), Task('Task Two')]
    for task in tasks:
        repo.add(task)
    assert len(repo.list()) == 2

def test_list_all(repo: CsvRepository):
    tasks = [Task('Task One'), Task('Task Two')]
    for task in tasks:
        repo.add(task)
        
    assert [str(task.id) for task in repo.list()] == [str(task.id) for task in tasks]

    for task in tasks:
        repo.remove(task)

def test_list_all_nonexistent(repo: CsvRepository):
    assert repo.list() == []
