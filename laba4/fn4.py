import json

def convert_dict_to_json(data: dict) -> str:
    return json.dumps(data, indent=2, ensure_ascii=False)