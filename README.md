## Python FastAPI

Simple my learning documentation

#### **Step 1**: import `FastAPI`

```python
from fastapi import FastAPI
```

`FastAPI` is a Python class that provides all the functionality for your API.

#### **Step 2**: Create a `FastAPI` "instance"

```python
app = FastAPI()
```

- Here the app variable will be an "instance" of the class `FastAPI`
- app varibale will help us to perform routing, controlling everything as like
  the `express`
- This will be the main point of interaction to create all your API.
- And this `app` variable will help me to run our `uvicorn` application

**Summary of `main.py` file**

- Import FastAPI.
- Create an app instance.
- Write a path operation decorator (like `@app.get("/")`).
- Write a path operation function (like def root(): ... above).
- Run the development server (like `uvicorn main:app --reload`).
