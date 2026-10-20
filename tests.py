import logic
from datetime import timedelta

test_values = {
    'name': 'Test name 2',
    'year': 2065,
    'category': 'scifi',
    'duration': timedelta(hours=1, minutes=43, seconds=12),
    'rating': 4,
    'actors': 'Stephen Hawking,Ann Rotwein'
}
test_values_bad = {
    'name': 'Test name',
    'year': 1900,
    'category': 'horror',
    'duration': timedelta(hours=1, minutes=43, seconds=12),
    'rating': 5,
    'actors': 'Stephen Hawking,Ann Rotwein'
}
# logic.add(test_values)

#print(logic.list_records())
# print(logic.find_by_category("scifi"))
# print(logic.films_by_category())
print(logic.remove_record(1))