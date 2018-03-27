from zipcodes import is_valid
from random import randint
from all_lunch_locs import call_lunch_api

default_max = 30
default_range = 20


def random_zip():
    # because what matters is good food, not close food.
    random_zip = 0
    # because strings are required for this module
    while not is_valid(str(random_zip)):
        range_start = 10 ** (4)
        range_end = (10 ** 5) - 1
        random_zip = randint(range_start, range_end)

    return str(random_zip)


def within_lunch_range(input_number):
    return int(input_number) <= default_max


def set_values_with_default(loc=random_zip(), range=default_range):
    return {'location': loc, 'range': range}


def two_params(first_param, second_param):
    if is_valid(first_param) and within_lunch_range(second_param):
        return set_values_with_default(first_param, second_param)
    else:
        return set_values_with_default()


def split_params(param_text):
    if not param_text:  # no params, default random zip code, 20 miles
        return set_values_with_default()

    params = param_text.split()

    if len(params) == 2:  # two values
        return two_params(params[0], params[1])

    if len(params) == 1 and is_valid(params[0]):  # one value
        return set_values_with_default(loc=params[0])

    else:
        return set_values_with_default()


def select_random_location(lunch_response):
    number_locs = len(lunch_response['businesses'])

    selected_loc = randint(0, number_locs - 1)
    return lunch_response['businesses'][selected_loc]


def build_response_text(loc_dict):
    return f'The Wheel of Lunch has selected {loc_dict["name"]} at {" ".join(loc_dict["location"]["display_address"])}'


def create_lunch_event(request):
    param_dict = split_params(request.get('text'))
    response = call_lunch_api(location=param_dict['location'], range=param_dict['range'])
    location = select_random_location(response.json())

    return build_response_text(location)


if __name__ == '__main__':
    # format of the json
    # CombinedMultiDict([ImmutableMultiDict([]), ImmutableMultiDict(
    #     [('token', 'workspace token'), ('team_id', 'team_id'), ('team_domain', 'some_string_name'),
    #      ('channel_id', 'some_channel_id'), ('channel_name', 'some_channel_name'), ('user_id', 'user_id_requested'), ('user_name', 'user_name_requested'),
    #      ('command', '/lunch'), ('text', '80233'), #<---- args
    #      ('response_url', 'response url'),
    #      ('trigger_id', 'slash trigger command')])])

    print(create_lunch_event({'text': '80020 20'}))
    print(create_lunch_event({'text': '20'}))
