from requests import get


def call_lunch_api(location, range):
    params = (
        ('zip', f'{location}^'),
        ('query', 'lunch^'),
        ('radius', f'{range}'),
    )
    return get('https://wheelof.com/lunch/yelpProxyJSON.php', params=params)
