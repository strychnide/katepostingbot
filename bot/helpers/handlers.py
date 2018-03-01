def add_handler(dispatcher, handler):
    def wrapper(func):
        dispatcher.add_handler(handler(func))

        def wrapped(bot, update):
            return func(bot, update)
        return wrapped
    return wrapper
