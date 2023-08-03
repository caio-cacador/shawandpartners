# Test for Shaw and Partners

## This API is available on render.com
https://caio-cacador-001.onrender.com/docs

## Instructions for running the application

#### Genereting your GitHub API token
To learn how to do this go to the link below:

https://docs.github.com/en/enterprise-server@3.6/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens

### Running the application
  
1. First, set the environment variable

Linux/Mac:
```sh
export GITHUB_AUTH_TOKEN=your_token_here
```

Windows:
```sh
set GITHUB_AUTH_TOKEN=your_token_here
```

2. Second, make sure you are at the root of the project.

3. Then, install the requirements:
```sh
pip install -r requirements.txt
```

4. Then, run the the application:

Example using uvicorn:

```sh
uvicorn main:app
```

Example using python:
```sh
python main.py
```

5. Access the application through the link http://localhost:8000/

## Instructions for accessing the documentation

1. First, make sure you have run the application
2. Then, go to the link:

http://localhost:8000/docs

or

http://localhost:8000/redoc/
