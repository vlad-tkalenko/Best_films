FILE = "data.txt"

def load(filename: str) -> str:
    """Return list of dictionaries from text file. Skip broken rows"""
    records = []
    try:
        f = open(filename, "r", encoding="utf-8")
    except FileNotFoundError:
        return records              # No file found: return empty records

    with f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            parts = line.split(";")
            try:
                record = {
                    "name": parts[0],
                    "year": parts[1],
                    "category": parts[2],
                    "duration": parts[3],
                    "rating": parts[4],
                    "actors": parts[5]
                }
            except (IndexError, ValueError):
                print("Skip broken line:", line)
                continue
            records.append(record)
    return records

def save(filename: str, records: list[dict]) -> None:
    """Write records into a file"""
    with open(filename, "w", encoding="utf-8") as f:
        for r in records:
            f.write(f"{r["name"]};{r["year"]};{r["category"]};{r["duration"]};{r["rating"]};{r["actors"]}\n")