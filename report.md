# Search Tool for Research Papers using Gemini API Documentation

## Table of Contents
1. [Getting Started](#getting-started)
2. [Project Structure](#project-structure)
3. [API Documentation](#api-documentation)
4. [Dependencies](#dependencies)

---

## Getting Started

To get started with the Search Tool for Research Papers that utilizes the Gemini API, follow the steps below:

### Prerequisites
- Python 3.6 or higher
- An active Gemini API key
- Required libraries (listed in dependencies section)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/research-paper-search.git
   ```
2. Navigate into the project directory:
   ```bash
   cd research-paper-search
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Configuration
Setup your environment variables to secure sensitive information like your API key. Create a `.env` file and add your keys:
```
GEMINI_API_KEY=your_api_key_here
```

## Project Structure

```plaintext
research-paper-search/
│
├── src/
│   ├── __init__.py               
│   ├── api.py                     # Gemini API interaction layer
│   ├── search.py                  # Search functionalities
│   ├── utils.py                   # Utility functions
│   └── main.py                    # Entry point of the application
│
├── tests/
│   ├── __init__.py               
│   ├── test_search.py             # Unit tests for search functionalities
│   └── test_api.py                # Unit tests for API interactions
│
├── requirements.txt                # Project dependencies
└── README.md                       # Project overview and documentation
```

### File Descriptions
- `api.py`: This file contains the `GeminiAPI` class encapsulating methods to interact with the Gemini API.
- `search.py`: Contains methods for searching papers, filtering, and sorting results.
- `utils.py`: Provides utility functions used across the project.
- `main.py`: The main entry point for running the application.

## API Documentation

### GeminiAPI class
This class handles all interactions with the Gemini API.
- **Methods**:
  - `search_papers(query: str, filters: dict = None, page: int = 1) -> list`: Searches for papers based on the query and provided filters, with pagination support.
  - `filter_by_year(results: list, years: list) -> list`: Filters results based on a list of years.
  - `sort_by(results: list, key: str = 'relevance_score', reverse: bool = True) -> list`: Sorts results based on specified criteria.

**Example Usage**:
```python
from src.api import GeminiAPI

api = GeminiAPI()
papers = api.search_papers("quantum computing", page=1)
```

### Error Handling
The API interactions should raise exceptions in case of errors as follows:
```python
if response.status_code != 200:
    raise Exception(f"Error: {response.status_code} - {response.text}")
```

### Logging
Utilize the logging module for error reporting:
```python
import logging
logging.basicConfig(level=logging.INFO)
logging.error("Error fetching data from the API")
```

## Dependencies
- **requests**: For handling HTTP requests.
- **python-dotenv**: For loading environment variables from a `.env` file.
- **pytest**: For writing and running unit tests.

Use the following command to install the dependencies:
```bash
pip install -r requirements.txt
```

---

### Conclusion
By following this documentation, you should be able to set up the Search Tool for Research Papers using the Gemini API efficiently. Ensure to incorporate proper error handling, logging practices, and well-structured code for maintainability and scalability. Feel free to explore the test directory to validate the functionalities as you modify and enhance the project. 

By maintaining accurate, up-to-date documentation like this, the team can work more collaboratively and effectively, ensuring the project's success.