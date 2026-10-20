from pydantic import BaseModel, Field
from datetime import timedelta
from enum import StrEnum
from collections import defaultdict
import storage

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

def return_string_for_print(records: list[dict]) -> str:
    """Create string from records for printing"""
    final_string = 'Id     Title                Year Category   Duration  Rating Authors\n'
    final_string += '-----------------------------------------------------------------------------------------------\n'
    for record in records:
        final_string += f"{record['id']:<6} {record['name']:<20} {record['year']} {record['category']:<10} {record['duration']:<9} {record['rating']:<6} {record['actors']}\n"
    return final_string.strip()

def add(args: dict) -> int:
    """
    Add record about film.
    Args should contain next fields:
    name, year, category, duration, rating, actors
    Return an id of new record
    """
    film_record = FilmRecord(**args)
    film_record_dict = film_record.model_dump()
    new_id = storage.add(film_record_dict)
    return new_id

def list_records() -> str:
    """
    Return all records for output
    """
    film_records = storage.load()
    return return_string_for_print(film_records)


def find_by_category(category: str) -> list[dict]:
    """Return records of selected category. Return empty list if category doesn't exist"""
    if category not in FilmCategories:
        return []
    film_records = storage.load(category)
    return return_string_for_print(film_records)

def films_by_category() -> dict[str: int]:
    """return dictionary, where keys are categories and values are number of films for each category"""
    films_by_category = defaultdict(int)
    records = storage.load()
    for record in records:
        films_by_category[record['category']] += 1
    return films_by_category

def remove_record(id: int) -> bool:
    """Remove record with specific id"""
    return storage.delete(id)