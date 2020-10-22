def singleton(cls):
    # Этот код не мой, реализация синглтона из интернета
    class_instances = {}

    def get_instance(*args, **kwargs):
        """ creating or just return the one and only class instance.
            The singleton depends on the parameters used in __init__ """
        key = (cls, args, str(kwargs))
        if key not in class_instances:
            class_instances[key] = cls(*args, **kwargs)
        return class_instances[key]

    return get_instance
