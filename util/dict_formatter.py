
from typing import Any, Dict, List


def form_dict_to_request(
        dictionary: Dict[str, List[Dict[str, Any]]]) -> Dict[str, Any]:
    """
    Функция принимает словарь с параметрами для запроса.
    Возвращает подготовленный для запроса словарь.
    """
    new_dict = {}
    for key in dictionary.keys():
        if len(dictionary[key]) > 0:
            
            if isinstance(dictionary[key][0][key], str):
                if dictionary[key][0][key].isdigit():
                    new_dict[key] = int(dictionary[key][0][key])
                else:
                    new_dict[key] = dictionary[key][0][key]

            new_dict[key] = dictionary[key][0][key]

    if new_dict.get('media_type'):
        new_dict['media_type'] = ','.join(new_dict['media_type'])
            
    return new_dict
