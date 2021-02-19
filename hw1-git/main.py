from urllib.parse import urlparse


def parse(query: str) -> dict:
    """
    Converts url to a field-value dict
    """
    # select only the query string
    query = urlparse(query).query
    # if the string ends with an & or ? - remove it
    query = query[:-1] if (query.endswith('&') or query.endswith('?')) else query
    # if the str > 0, return a non-empty dictionary
    return {e[0]: e[1] for e in [e.split("=", 1) for e in query.split("&")]} if len(query) > 0 else {}


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}


def parse_cookie(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
