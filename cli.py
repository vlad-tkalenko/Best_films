import sys
import logic
from datetime import timedelta

def main():
    if len(sys.argv) < 2:
        print("використання: python cli.py add|list|find|report|remove ...")
        return
    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) != 8:
            print("використання: python cli.py add НАЗВА_ФІЛЬМУ ДАТА КАТЕГОРІЯ ТРИВАЛІСТЬ(Годин,Хвилин,Секунд) РЕЙТИНГ АКТОРИ_ЧЕРЕЗ_КОМУ")
            return
        name, year, category, duration, rating, actors = sys.argv[2], int(sys.argv[3]), sys.argv[4], sys.argv[5], int(sys.argv[6]), sys.argv[7]
        try:
            hours, minutes, seconds = duration.split(',')
            duration = timedelta(hours=int(hours), minutes=int(minutes), seconds=int(seconds))
        except (IndexError, ValueError) as e:
            print("duration повинен мати вигляд ГОДИНИ,ХВИЛИНИ,СЕКУНДИ")
        logic.add({
            "name": name,
            "year": year,
            "category": category,
            "duration": duration,
            "rating": rating,
            "actors": actors})
        

    elif command == "list":
        print(logic.list_records())

    elif command == "find":
        if len(sys.argv) < 3:
            print("використання: python cli.py find category")
            return
        category = sys.argv[2]
        filtered_categories = logic.find_by_category(category)
        print(filtered_categories)

    elif command == "report":
        print(logic.films_by_category())
    elif command == "remove":
        if len(sys.argv) < 3:
            print("використання: python cli.py remove record_id")
            return
        record_id = sys.argv[2]
        is_removed = logic.remove_record(record_id)
        if is_removed:
            print("Запис був видалений")
        else:
            print("Запису з таким id не було в таблиці")
    else:
        print("невідома команда:", command)

if __name__ == "__main__":
    main()