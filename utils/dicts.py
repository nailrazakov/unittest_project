def get_val(collection: dict, key, default='git'):
    """
    Функция возвращает значение из словаря по переданному ключу, если ключ существует.
    В ином случае возвращается значение default
    """
    if key in collection.keys():
        return collection.get(key)
    else:
        return default
