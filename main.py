import requests
from flask import Flask, render_template, request
from bs4 import BeautifulSoup

app = Flask(__name__)

# Replace with your Google Books API key
API_KEY = "AIzaSyBJbqV0W0awFfA8zjApXM0bJjbM2Yl6I9g"

# Base URL for Google Books API search
BASE_URL = "https://www.googleapis.com/books/v1/volumes"

def search_books(query, page=1):
    params = {
        "q": query,
        "key": API_KEY,
        "maxResults": 10,  # Limit to 10 results per page
        "startIndex": (page - 1) * 10,  # Adjust for pagination
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()

        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def process_results(data):
    if not data:
        return None

    total_results = data.get("totalItems", 0)
    items = data.get("items", [])

    author_counts = {}
    for item in items:
        authors = item.get("volumeInfo", {}).get("authors", [])
        for author in authors:
            author_counts[author] = author_counts.get(author, 0) + 1
    most_frequent_author = max(author_counts, key=author_counts.get, default=None)

    publication_dates = []
    for item in items:
        pub_date = item.get("volumeInfo", {}).get("publishedDate")
        if pub_date:
            publication_dates.append(pub_date)
    earliest_date = min(publication_dates) if publication_dates else None
    latest_date = max(publication_dates) if publication_dates else None

    books = []
    for item in items:
        volume_info = item.get("volumeInfo", {})
        description_html = volume_info.get("description", "")
        soup = BeautifulSoup(description_html, 'html.parser')
        description = soup.get_text(strip=True)

        # Fetch the cover photo URL
        image_links = volume_info.get("imageLinks", {})
        thumbnail = image_links.get("thumbnail", "")

        book_data = {
            "title": volume_info.get("title", ""),
            "authors": ", ".join(volume_info.get("authors", [])),
            "description": description if description else "No description available",
            "thumbnail": thumbnail,
            # ... Add more book data as needed
        }
        books.append(book_data)

    results = {
        "total_results": total_results,
        "most_frequent_author": most_frequent_author,
        "publication_dates": (earliest_date, latest_date),
        "books": books,
    }
    return results

@app.route('/')
def index():
    search_query = request.args.get('query', 'artificial intelligence')
    page_number = int(request.args.get('page', 1))

    data = search_books(search_query, page_number)

    if data:
        results = process_results(data)
        return render_template('index.html', results=results, page=page_number)

    return render_template('index.html', results=None)

if __name__ == "__main__":
    app.run(debug=True)
