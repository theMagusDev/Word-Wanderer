import json

def get_user_data():
    with open('data/data.json', 'rt') as data_file:
        data = json.load(data_file)

    return data



def set_user_data(data, pretty=False):
    if pretty:
        with open('data/data.json', 'wt') as data_file:
            json.dump(data, data_file, allow_nan=True, indent=4)
    else:
        with open('data/data.json', 'wt') as data_file:
            json.dump(data, data_file, allow_nan=True, separators=(',', ':'))



def get_settings():
    with open('data/settings.json', 'rt') as data_file:
        data = json.load(data_file)

    return data



def save_settings(data, pretty=True):
    if pretty:
        with open('data/settings.json', 'wt') as data_file:
            json.dump(data, data_file, allow_nan=True, indent=4)
    else:
        with open('data/settings.json', 'wt') as data_file:
            json.dump(data, data_file, allow_nan=True, separators=(',', ':'))
