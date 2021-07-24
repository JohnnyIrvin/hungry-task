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
import click
from viking.domain.seedwork import AbstractRepository
from viking.domain.task import Task
from viking.infrastructure.repository_factory import RepositoryFactory

repository: AbstractRepository = None

@click.group()
@click.argument('repo', required=True)
def cli(repo: str):
   """
   This is the main entry point for the hungry task CLI.

   Args:
       repo (str): The name of the repository to use.
   """
   global repository
   repository = RepositoryFactory(Task).create(repo)

@click.argument('name')
@cli.command()
def add(name: str):
   """
   Add a new task.

   Args:
       name (str): The name of the task to add.
   """
   click.echo(f"Task added '{name}'")
   repository.add(Task(name))

@click.argument('name')
@cli.command()
def get(name: str):
   """
   Get a task by name.

   Args:
       name (str): The name of the task to get.
   """   
   for task in repository.list():
      if task.name == name:
         completed: str = 'x' if str(task.completed) == str(True) else ' '
         click.echo(f"[{completed}] - {task.name}")
         return
   click.echo(f"Task '{name}' not found")

@click.argument('name')
@cli.command()
def remove(name: str):
   """
   Remove a task by name.

   Args:
       name (str): The name of the task to remove.
   """   
   click.echo(f"Task removed '{name}'")
   for task in repository.list():
      if task.name == name:
         repository.remove(task)
         return
   click.echo(f"Task '{name}' not found")

@cli.command()
def list():
   """
   List all tasks.
   """
   for task in repository.list():
      completed: str = 'x' if str(task.completed) == str(True) else ' '
      click.echo(f"[{completed}] - {task.name}")

@click.argument('name')
@cli.command()
def complete(name: str):
   """
   Mark a task as complete.

   Args:
      name (str): The name of the task to mark as complete.
   """   
   for task in repository.list():
      if task.name == name:
         try:
            task = task.complete()
         except Task.AlreadyCompletedError:
            click.echo(f"Task '{name}' already completed")
            return
         repository.add(task)
         click.echo(f"Task '{name}' completed")
         return
   click.echo(f"Task '{name}' not found")
