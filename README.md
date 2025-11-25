[![This package is currently under development.](https://img.shields.io/badge/under-development-orange.svg)](https://github.com/sdhutchins/flask-demo)
[![codecov](https://codecov.io/gh/sdhutchins/flask-demo/branch/main/graph/badge.svg)](https://codecov.io/gh/sdhutchins/flask-demo)

# flask-demo

This is a demo Flask website that includes a login page.

In order to log in, the `username` is `admin` and the `password` is `admin`.

## Install & Setup

### Requirements

- Python 3.9 or newer
- pip

### Instructions

1. Clone or download this repository:
   ```bash
   git clone https://github.com/sdhutchins/flask-demo.git
   cd flask-demo
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. (Optional) Create a `.env` file for environment variables:
   ```bash
   FLASK_DEBUG=True
   SECRET_KEY=your-secret-key-here
   ```
   If no `.env` file is present, the app will use default values.

## Usage

### Running the Development Server

Run the application using one of the following methods:

#### Method 1: Using run.py

```bash
python run.py
```

#### Method 2: Using Flask CLI

```bash
flask run
```

The application will be available at `http://localhost:5000/`.

## Tests

Run tests with pytest:

```bash
pytest
```

Run tests with coverage report:

```bash
pytest --cov=app --cov-report=html
```

View the HTML coverage report by opening `htmlcov/index.html` in your browser.

## ToDo

- [ ] Add example for setting up a database.
- [x] Update css to Bootstrap 4.
