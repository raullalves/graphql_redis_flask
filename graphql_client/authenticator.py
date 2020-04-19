import functools


def authenticate(f):
    @functools.wraps(f)
    def authenticator(*args, **kwargs):
        headers = args[1].context.headers.get_dict('Authorization', None)
        if headers is None:
            raise Exception('Missing user authorization')

        return f(*args, **kwargs)

    return authenticator
