import types


# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        self.items = items
        if 'ignore_case' in kwargs:
            self.flag = kwargs['ignore_case']
        else:
            self.flag = False
        self.i = 0
        self.items_set = set()

    def __next__(self):
        if not isinstance(self.items, types.GeneratorType):
            if self.i < len(self.items):
                if self.flag and isinstance(self.items[self.i], str):
                    if not (self.items[self.i].lower() in self.items_set):
                        self.items_set.add(self.items[self.i].lower())
                        self.i += 1
                        return self.items[self.i - 1]
                    else:
                        self. i += 1
                        return self.__next__()
                elif not (self.items[self.i] in self.items_set):
                    self.items_set.add(self.items[self.i])
                    self.i += 1
                    return self.items[self.i - 1]
                else:
                    self.i += 1
                    return self.__next__()
            else:
                raise StopIteration
        else:
            try:
                item = next(self.items)
                if self.flag and (isinstance(item, str)):
                    if not (item.lower() in self.items_set):
                        self.items_set.add(item.lower())
                        return item
                    else:
                        return self.__next__()
                elif not (item in self.items_set):
                    self.items_set.add(item)
                    return item
                else:
                    return self.__next__()
            except StopIteration:
                raise StopIteration

    def __iter__(self):
        return self
