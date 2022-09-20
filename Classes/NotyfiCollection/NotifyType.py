class NotifyType:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value


class NotifyAdd(NotifyType):
    def __init__(self, value):
        super().__init__(value)


class NotifyDelete(NotifyType):
    def __init__(self, value):
        super().__init__(value)


class NotifyUpdate(NotifyType):
    def __init__(self, value):
        super().__init__(value)