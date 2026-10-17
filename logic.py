from pydantic import BaseModel, Field
from datetime import timedelta
from enum import StrEnum
import storage
from collections import defaultdict

class FilmCategories(StrEnum):
    ANIMATED = "animated"
    FANTASY = "fantasy"
    GANGSTER = "gangster"
    SCIFI = "scifi"
    WESTERN = "western"
    SPORTS = "sports"
    MYSTERY = "mystery"
    ROMANTIC = "romantic"
    DRAMA = "drama"
    EPIC = "epic"
    HORROR = "horror"

class FilmRecord(BaseModel):
    name: str
    year: int = Field(ge=1900)
    category: FilmCategories
    duration: timedelta
    rating: int = Field(ge=1, le=5)
    actors: str

def add(args: dict):
    """
    Add record about film.
    Args should contain next fields:
    name, year, category, duration, rating, actors
    """
    film_record = FilmRecord(**args)
    film_record_dict = film_record.model_dump()
    all_records = storage.load(storage.FILE)
    all_records.append(film_record_dict)
    storage.save(storage.FILE, all_records)

def list_records() -> str:
    """
    Return all records for output
    """
    film_records = storage.load(storage.FILE)
    final_string = 'Title                Year Category   Duration  Rating Authors\n'
    final_string += '-----------------------------------------------------------------------------------------------\n'
    for record in film_records:
        final_string += f"{record['name']:<20} {record['year']} {record['category']:<10} {record['duration']:<9} {record['rating']:<6} {record['actors']}\n"
    return final_string.strip()

def find_by_category(category: str) -> list[dict]:
    """Return records of selected category. Return empty list if category doesn't exist"""
    if category not in FilmCategories:
        return []
    film_records = storage.load(storage.FILE)
    filtered_records = []
    for record in film_records:
        if record['category'] == category:
            filtered_records.append(record) 
    return filtered_records

def films_by_category() -> dict[str: int]:
    """return dictionary, where keys are categories and values are number of films for each category"""
    films_by_category = defaultdict(int)
    records = storage.load(storage.FILE)
    for record in records:
        films_by_category[record['category']] += 1
    return films_by_category