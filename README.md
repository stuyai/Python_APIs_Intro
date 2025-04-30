# Python_APIs_Intro

*Notes for Lesson on 4/30*

A simple FastAPI project demonstrating basic API endpoints for reading, iterating, and managing names and numbers.  

## Table of Contents

- [Overview](#overview)  
- [Prerequisites](#prerequisites)  
- [Installation](#installation)  
- [Usage](#usage)  
  - [Running the API](#running-the-api)  
  - [Available Endpoints](#available-endpoints)  
  - [Example Requests](#example-requests)  
- [Files in This Project](#files-in-this-project)  
- [Contributing](#contributing)  
- [License](#license)  

## Overview

This project uses [FastAPI](https://fastapi.tiangolo.com/) to expose a few simple REST endpoints:
- Read a greeting message  
- Read and increment a counter stored in `number.txt`  
- Manage an in‑memory list of names  
- Set and get a separate numeric value  

## Prerequisites

- Python 3.10+  
- pip  

## Installation

1. Clone the repo or download the files.  
2. (Optional) Create a virtual environment:  
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```  
3. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  

## Usage

### Running the API

Start the server with Uvicorn:

```bash
uvicorn main:app --reload
```

By default, it listens on `http://127.0.0.1:8000`.

### Available Endpoints

| Method | Path                          | Description                                 |
| ------ | ----------------------------- | ------------------------------------------- |
| GET    | `/`                           | Returns a greeting JSON                    |
| GET    | `/iterate`                    | Reads, returns, then increments `number.txt` |
| GET    | `/names`                      | Returns JSON list of added names           |
| POST   | `/addname/{name}`             | Appends `name` to list, returns `name`      |
| PUT    | `/set_right_num/{s_num}`      | Sets internal `right_num`, returns it       |
| GET    | `/right_num`                  | Returns the current `right_num`             |

All endpoints are defined in [`main.py`](main.py).  

### Example Requests

You can test endpoints via `curl`, Python `requests`, or the included Jupyter notebook.

#### Using `curl`

```bash
# Greeting
curl http://127.0.0.1:8000/

# Iterate number
curl http://127.0.0.1:8000/iterate

# Add a name
curl -X POST http://127.0.0.1:8000/addname/elias

# Set right_num
curl -X PUT http://127.0.0.1:8000/set_right_num/6

# Get right_num
curl http://127.0.0.1:8000/right_num
```

#### Using Python `requests`

```python
import requests

# Add a name
resp = requests.post("http://127.0.0.1:8000/addname/alice")
print(resp.json())

# Get names
resp = requests.get("http://127.0.0.1:8000/names")
print(resp.json())
```

#### Jupyter Notebook

Open and run [`request.ipynb`](request.ipynb) for live examples.

## Files in This Project

- [`main.py`](main.py) – FastAPI application  
- [`requirements.txt`](requirements.txt) – Python dependencies  
- [`number.txt`](number.txt) – Counter storage  
- [`request.ipynb`](request.ipynb) – Example usage notebook  
- [.gitignore](.gitignore) – Ignored files list  
- [APIs in Python.pdf](APIs%20in%20Python.pdf) – Lesson material PDF  
- [`LICENSE`](LICENSE) – MIT License  
- [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) – Contributor Covenant  

## Contributing

Please open issues or pull requests via GitHub. Use the templates in `.github/ISSUE_TEMPLATE/`.

## License

This project is licensed under the MIT License. See [`LICENSE`](LICENSE) for details.