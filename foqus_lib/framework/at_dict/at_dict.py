
class AtDict(dict):
    def __getattr__(self, name):
            return self[name]

    def __setattr__(self, name, value):
        if name in self.keys():
            self[name] = value
        else:
             super(AtDict, self).__setattr__(name, value)

class OrderedAtDict(AtDict):
    def __init__(self, *args, **kwargs):
        self._ordered_keys = []
        super(AtDict, self).__init__(self, *args, **kwargs)

    def __setitem__(self, name, value):
        if name not in self._ordered_keys:
            self._ordered_keys.append(name)
        super(AtDict, self).__setitem__(name, value)

    def __delitem__(self, name):
        if name not in self._ordered_keys:
            return
        self._ordered_keys.remove(name)
        super(AtDict, self).__delitem__(name)

    def __iter__(self):
        for k in self._ordered_keys:
            yield k

    def iteritems(self):
        for k in self:
            yield (k, self[k])

    def ordered_keys(self):
        return self._ordered_keys
