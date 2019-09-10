class CustomDict(dict):
    """
    A dictionary that keeps its keys in the order in which they're inserted.
    """
    def __new__(cls, *args, **kwargs):
        instance = super(CustomDict, cls).__new__(cls, *args, **kwargs)
        instance.keyOrder = []
        return instance

    def __init__(self, data=None):
        if data is None or isinstance(data, dict):
            data = data or []
            super(CustomDict, self).__init__(data)
            self.keyOrder = list(data) if data else []
        else:
            super(CustomDict, self).__init__()
            super_set = super(CustomDict, self).__setitem__
            for key, value in data:
                # Take the ordering from first key
                if key not in self:
                    self.keyOrder.append(key)
                # But override with last value in data (dict() does this)
                super_set(key, value)

    def __setitem__(self, key, value):
        if key not in self:
            self.keyOrder.append(key)
        super(CustomDict, self).__setitem__(key, value)



d = CustomDict({'c':1, 'b':2, 'a':3})
print(d.get('c'))
d['d']=4
print(d)



    

    