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
from typing import List, Tuple

import pytest
from cli import cli

task_names: List[str] = ['Read a book', 'Eat Popcorn', 'Go to sleep']
repo_names: List[str] = ['csv']
repo_tasks_tuples: List[Tuple[str, str]] = [(repo, name) for repo in repo_names for name in task_names]


def test_invoke_cli(runner):
    result = runner.invoke(cli)

    assert result.exit_code == 0
    assert 'Usage' in result.output

@pytest.mark.parametrize(('repo', 'name'), repo_tasks_tuples)
def test_add_task_with_name(repo: str, name: str, runner):
    result = runner.invoke(cli, [repo, 'add', name])

    assert 'Task added' in result.output
    assert name in result.output

@pytest.mark.parametrize(('repo', 'name'), repo_tasks_tuples)
def test_remove_task_with_name(repo: str, name: str, runner):
    runner.invoke(cli, [repo, 'add', name])
    
    result = runner.invoke(cli, [repo, 'remove', name])

    assert 'Task removed' in result.output
    assert name in result.output

@pytest.mark.parametrize(('repo', 'name'), repo_tasks_tuples)
def test_list_added_tasks(repo: str, name: str, runner):
    runner.invoke(cli, [repo, 'add', name])

    result = runner.invoke(cli, [repo, 'list'])

    assert name in result.output
    runner.invoke(cli, [repo, 'remove', name])

@pytest.mark.parametrize(('repo', 'name'), repo_tasks_tuples)
def test_list_added_tasks(repo: str, name: str, runner):
    runner.invoke(cli, [repo, 'add', name])

    result = runner.invoke(cli, [repo, 'list'])

    assert name in result.output
    runner.invoke(cli, [repo, 'remove', name])

@pytest.mark.parametrize(('repo', 'name'), repo_tasks_tuples)
def test_get_task_with_name(repo: str, name: str, runner):
    runner.invoke(cli, [repo, 'add', name])

    result = runner.invoke(cli, [repo, 'get', name])

    assert f'[ ] - {name}' in result.output
    runner.invoke(cli, [repo, 'remove', name])

@pytest.mark.parametrize(('repo', 'name'), repo_tasks_tuples)
def test_task_not_found(repo: str, name: str, runner):
    result = runner.invoke(cli, [repo, 'get', name])

    assert f"Task '{name}' not found" in result.output

@pytest.mark.parametrize(('repo', 'name'), repo_tasks_tuples)
def test_complete_task(repo: str, name: str, runner):
    runner.invoke(cli, [repo, 'add', name])

    result = runner.invoke(cli, [repo, 'complete', name])

    assert f"Task '{name}' completed" in result.output
    assert name in result.output
    runner.invoke(cli, [repo, 'remove', name])
