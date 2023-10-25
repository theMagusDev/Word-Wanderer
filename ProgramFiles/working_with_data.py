import json

def get_user_data():
    try:
        with open('data/data.json', 'rt') as data_file:
            data = json.load(data_file)
    except json.decoder.JSONDecodeError:
        with open('defaults/data.json', 'rt') as data_file:
            data = json.load(data_file)
        with open('data/data.json', 'wt') as data_file:
            json.dump(data, data_file, allow_nan=True, indent=4)

    return data



def set_user_data(data, pretty=False):
    with open('data/data.json', 'wt') as data_file:
        if pretty:
            json.dump(data, data_file, allow_nan=True, indent=4)
        else:
            json.dump(data, data_file, allow_nan=True, separators=(',', ':'))



def get_settings():
    try:
        with open('data/settings.json', 'rt') as data_file:
            data = json.load(data_file)
    except json.decoder.JSONDecodeError:
        with open('defaults/settings.json', 'rt') as data_file:
            data = json.load(data_file)
        with open('data/settings.json', 'wt') as data_file:
            json.dump(data, data_file, allow_nan=True, indent=4)

    return data



def save_settings(data, pretty=True):
    with open('data/settings.json', 'wt') as data_file:
        if pretty:
            json.dump(data, data_file, allow_nan=True, indent=4)
        else:
            json.dump(data, data_file, allow_nan=True, separators=(',', ':'))
