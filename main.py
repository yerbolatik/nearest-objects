import json
from typing import List, Tuple
from haversine import haversine, Unit


def load_data_from_json(file_path: str) -> List[Tuple[str, float, float]]:
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return [(obj[0], obj[1], obj[2]) for obj in data]


def find_nearest_objects(point: Tuple[float, float], top: int, data: List[Tuple[str, float, float]]) -> List[List[str]]:
    distances = [(obj[0], obj[1], obj[2], haversine(
        point, (obj[1], obj[2]), unit=Unit.KILOMETERS)) for obj in data]
    distances.sort(key=lambda x: x[3])

    top_objects = [[obj[0], str(obj[1]), str(obj[2]), str(obj[3])]
                   for obj in distances[:top]]
    return top_objects


if __name__ == "__main__":
    point = (43.256274, 76.789275)
    top = 10
    data_file = "data.json"

    data = load_data_from_json(data_file)

    result = find_nearest_objects(point, top, data)

    for obj in result:
        print(obj)
