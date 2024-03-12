# Google Books Search App

## Introduction
This is Challenge #1 for the Deque Systems Senior Solutions Engineer interview process.
It is a simple web application that allows users to search the Google Books API and view the results. The application includes pagination, displays detailed information about each book, and provides summary statistics about the search results.

## Features
- **Pagination:** Results are displayed in sets of 10, and you can navigate through pages.
- **Detailed Book Information:** Clicking on a book shows its details, including authors, title, and description.
- **Summary Statistics:** The search results include total results, the most frequent author, and the publication date range.
- **Responsive Design:** The UI is designed to work on various screen sizes.

## Requirements
Make sure you have the following installed:
- Python (version 3.6 or higher)
- pip (Python package installer)

## Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/google-books-search-app.git
    cd google-books-search-app
    ```

2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    - On Unix or MacOS:
        ```bash
        source venv/bin/activate
        ```

4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Run the application:
    ```bash
    python main.py
    ```

2. Open your web browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

3. Use the search form to enter your query and explore the results.

## Folder Structure
- **templates:** Contains HTML templates for the application.
- **static:** Holds static files, such as stylesheets.
