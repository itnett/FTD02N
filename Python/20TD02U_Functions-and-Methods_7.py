python
def process_data(data):
    result = []
    for item in data:
        if isinstance(item, dict):
            for key, value in item.items():
                if key == 'target' and isinstance(value, list):
                    result.extend(value)
                elif key == 'target' and isinstance(value, dict):
                    result.append(value)
    return result