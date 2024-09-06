![Alt](https://repobeats.axiom.co/api/embed/14505d78589231d9a3c51954c6f2991de95ef210.svg "Repobeats analytics image")

# how to activate existing virtual enviroment 
    pipenv shell

# dependencies of system
    python 
    pipenv

# create file  requirements.txt
    pip freeze > requirements.txt

# install dependencies
    pip install -r requirements.txt

#by run tests
    pytest
    pytest -v

#run test of single file
    pytest tests/test_post_degree.py

#run test of single file with mark
      pytest -v -m smoke tests/test_post_degree.py

#run test of a directory
    pytest tests/

# run test coverage
    coverage run -m pytest

# run report test coverage
    coverage report 
    coverage report -m 

# run and generated report test to "html" 
    coverage html

