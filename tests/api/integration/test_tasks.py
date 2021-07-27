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
from typing import List

from fastapi.testclient import TestClient


def test_get_tasks(client: TestClient):
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json() == []

def test_get_added_task(client: TestClient):
    response = client.post("/tasks", params={"name": "test"})
    assert response.status_code == 201
    
    response = client.get("/tasks")
    assert response.status_code == 200
    assert "test" in response.content.decode("utf-8")

    client.delete("/", params={"name": "test"})

def test_delete_added_task(client: TestClient):
    response = client.post("/tasks", params={"name": "test"})
    assert response.status_code == 201

    response = client.delete("/tasks", params={"name": "test"})
    assert response.status_code == 204

    response = client.get("/tasks")
    assert response.status_code == 200
    assert "test" not in response.content.decode("utf-8")

def test_get_specific_task(client: TestClient):
    response = client.post("/tasks", params={"name": "test"})
    assert response.status_code == 201
    id = response.json()["id"]

    response = client.get(f"/tasks/{id}")
    assert response.status_code == 200
    assert response.json()["name"] == "test"

    client.delete("/", params={"name": "test"})

def test_update_specific_task(client: TestClient):
    response = client.post("/tasks", params={"name": "test"})
    assert response.status_code == 201
    print(response.json()['id'])
    id = str(response.json()["id"])

    response = client.put(f"/tasks/{id}", params={"name": "updated"})
    assert response.status_code == 200
    assert response.json()["name"] == "updated"

    client.delete("/tasks", params={"name": "updated"})

def test_complete_task(client: TestClient):
    response = client.post("/tasks", params={"name": "test"})
    assert response.status_code == 201
    id = response.json()["id"]

    response = client.post(f"/tasks/{id}/complete")
    assert response.status_code == 200
    assert response.json()["completed"] == True

    client.delete("/tasks", params={"name": "test"})