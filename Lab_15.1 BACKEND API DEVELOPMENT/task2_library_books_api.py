"""Library Book Management RESTful API with partial PATCH updates."""
from typing import Optional
from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient
from pydantic import BaseModel

app = FastAPI(title="Library Book Management API")
books_db: dict[int, dict] = {}


class BookCreate(BaseModel):
    title: str
    author: str
    available: bool = True


class BookPatch(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    available: Optional[bool] = None


@app.get("/books")
def get_all_books():
    """Retrieve all books in the library."""
    return {"books": list(books_db.values())}


@app.post("/books", status_code=201)
def add_book(book_id: int, book: BookCreate):
    """Add a new book record."""
    if book_id in books_db:
        raise HTTPException(status_code=400, detail="Book ID already exists")
    books_db[book_id] = {"id": book_id, **book.dict()}
    return books_db[book_id]


@app.get("/books/{book_id}")
def get_book(book_id: int):
    """Fetch details of a single book by ID."""
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")
    return books_db[book_id]


@app.patch("/books/{book_id}")
def patch_book(book_id: int, updates: BookPatch):
    """Partially update book fields such as availability."""
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")
    patch_data = updates.dict(exclude_unset=True)
    if not patch_data:
        raise HTTPException(status_code=400, detail="No fields provided for update")
    books_db[book_id].update(patch_data)
    return books_db[book_id]


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    """Remove a book from the library."""
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"deleted": books_db.pop(book_id)}


if __name__ == "__main__":
    client = TestClient(app)
    r1 = client.post("/books?book_id=1", json={"title": "Clean Code", "author": "R. Martin"})
    assert r1.status_code == 201 and r1.json()["available"] is True
    r2 = client.patch("/books/1", json={"available": False})
    assert r2.status_code == 200 and r2.json()["available"] is False
    r3 = client.get("/books/999")
    assert r3.status_code == 404
    r4 = client.delete("/books/1")
    assert r4.status_code == 200
    print("POST /books ->", r1.json())
    print("PATCH /books/1 ->", r2.json())
    print("GET /books/999 (error handling) ->", r3.status_code, r3.json())
    print("DELETE /books/1 ->", r4.json())
    print("All 4 assert test cases PASSED.")
