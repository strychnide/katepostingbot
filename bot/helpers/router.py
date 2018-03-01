import re


class Router(object):
    def __init__(self):
        self.rules = []

    def route(self, path, methods=["GET"]):
        def wrapper(func):
            rule = {
                'path': re.compile(path),
                'methods': methods,
                'resolver': func
            }
            self.rules.append(rule)

            def wrapped(environ, start_response):
                return func(environ, start_response)
            return wrapped
        return wrapper

    def resolve(self, path, method):
        for rule in self.rules:
            if method in rule['methods']:
                rule_path = rule['path']
                match = rule_path.match(path)

                if match:
                    return rule['resolver']

        raise Exception('Your route is in another castle')

    def __call__(self, path, method, **kwargs):
        return self.resolve(path, method)
