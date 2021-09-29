# If you want to Contribute With de TODO-List API Project follow these steps:

We use [Poetry](https://python-poetry.org) to manage our virtualenv and dependencies. If you don't use the poetry don't forget to install the dev dependencies. You can know what are the dev dependencies into pyproject.toml file. This is self-explanatory. 

### There are some steps to take for contributing to the project

1. Clone the repository
2. Access the directory of your local repository
3. Install the project dependencies with Poetry
4. Create a file .secrets.toml in the `configs/` directory 
5. Put the variable `JWT_SCRET` in .secrets.toml file and set its value.

#### These steps in code:

```bash
git clone git@github.com:Riverfount/todo-api.git
cd todo-api
poetry install
cd configs/ 
touch .secrets.toml
```

### To run all tests

```bash
poety run pytest
```
