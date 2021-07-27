# Hungry Task

Hungry Task is a set of tools based around "Tasks".

Task are a unique identifier, a name, and a status of completed or not.

## Installation

```bash
python3 -m virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

For Tests
```bash
./run_tests.py
```

For CLI where group is command group, and command is group.
```bash
./cli.py <repo> <group> <command>
```
```bash
./cli.py csv add Take out the garbage.
```

For API
```bash
uvicorn api:api
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)