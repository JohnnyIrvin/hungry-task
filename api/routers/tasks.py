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
from dataclasses import asdict
from typing import List

from api.dependencies import repository
from api.models import task
from fastapi import APIRouter, Depends
from viking.domain.seedwork.abstract_repository import AbstractRepository
from viking.domain.task import Task

router = APIRouter(
    prefix="/tasks",
    responses={404: {"description": "Task not found"}},
)

@router.get('', response_model=List[task.Model])
async def get_all_tasks(repository: AbstractRepository = Depends(repository)):
    """
    Get all tasks.

    Args:
        repository (AbstractRepository): The repository to use.

    Returns:
        List[Task]: A list of all tasks.
    """
    return [asdict(task) for task in repository.list()]

@router.post('', response_model=task.Model, status_code=201)
async def create_task(name: str, repository: AbstractRepository = Depends(repository)):
    """
    Create a task.

    Args:
        task (Task): The task to create.
        repository (AbstractRepository): The repository to use.

    Returns:
        Task: The created task
    """
    new_task = Task(name=name)
    repository.add(new_task)
    return asdict(new_task)

@router.delete('', status_code=204)
async def delete_task(name: str, repository: AbstractRepository = Depends(repository)):
    """
    Delete a task.

    Args:
        name (str): The name of the task to delete.
        repository (AbstractRepository): The repository to use.
    """    
    for task in repository.list():
        if task.name == name:
            repository.remove(task)

@router.get('/{item_id}', response_model=task.Model)
async def get_task(item_id: str, repository: AbstractRepository = Depends(repository)):
    """
    Get a task.

    Args:
        item_id (int): The id of the task to get.
        repository (AbstractRepository): The repository to use.

    Returns:
        Task: The task.
    """
    return asdict(repository.get(item_id))

@router.put('/{item_id}', response_model=task.Model)
async def update_task(item_id: str, name: str, repository: AbstractRepository = Depends(repository)):
    """
    Update a task.

    Args:
        item_id (int): The id of the task to update.
        task (Task): The task to update.
        repository (AbstractRepository): The repository to use.

    Returns:
        Task: The updated task.
    """
    item = repository.get(item_id)
    repository.remove(item)
    item.name = name
    repository.add(item)
    return asdict(item)

@router.post('/{item_id}/complete', response_model=task.Model)
async def complete_task(item_id: str, repository: AbstractRepository = Depends(repository)):
    """
    Complete a task.

    Args:
        item_id (int): The id of the task to complete.
        repository (AbstractRepository): The repository to use.

    Returns:
        Task: The completed task.
    """
    item = repository.get(item_id)
    repository.remove(item)
    item.complete()
    repository.add(item)
    return asdict(item)