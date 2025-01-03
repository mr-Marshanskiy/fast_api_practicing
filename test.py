if __name__ == "__main__":
    import requests
    print(requests.get(
        'http://127.0.0.1:8000/hi/',
    ).json())

    # print(requests.get(
    #     'http://127.0.0.1:8000/header/test/1234',
    # ).headers)

    # requests.post(
    #     'http://127.0.0.1:8000/tags/',
    #     json={'tag': 'new_tag'}
    # )
    # print(requests.get(
    #     'http://127.0.0.1:8000/tags/new_tag'
    # ).json())