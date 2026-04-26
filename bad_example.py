def average_age(records):
    total = 0
    for record in records:
        total += record['age']
    #len(record) zamiast len(records). Przez to dzielisz przez długość ostatniego słownika, a nie listy.
    #return total / len(record)
    return total / len(records)


if __name__ == '__main__':
    sample = [
        {'name': 'Anna', 'age': 21},
        {'name': 'Piotr', 'age': 23},
        {'name': 'Maria', 'age': 25},
    ]
    print(average_age(sample))



"""
Zamiast ręcznej pętli użyto sum() i generatora — kod jest krótszy i bardziej „pythonowy”.
Dodano zabezpieczenie przed pustą listą, żeby uniknąć błędu dzielenia przez zero.
Wprowadzono typowanie, co ułatwia zrozumienie funkcji i jej użycia.
Uproszczono nazewnictwo zmiennej (total_age zamiast total).
"""

from typing import List, Dict, Union

def average_age(records: List[Dict[str, int]]) -> float:
    if not records:
        return 0.0

    total_age = sum(record["age"] for record in records)
    return total_age / len(records)


if __name__ == "__main__":
    sample = [
        {"name": "Anna", "age": 21},
        {"name": "Piotr", "age": 23},
        {"name": "Maria", "age": 25},
    ]

    print(average_age(sample))
