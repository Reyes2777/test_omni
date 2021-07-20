import datetime
import decimal


class ToDict:
    def to_dict(self):
        data = {}
        for attribute, value in self.__dict__.items():
            if (not attribute.startswith('__') and not attribute.endswith('__')) and not attribute.startswith('_'):
                if type(value) == decimal.Decimal:
                    data[attribute] = str(value)
                elif isinstance(value, (datetime.datetime, datetime.date)):
                    data[attribute] = value.isoformat()
                elif value is None:
                    data[attribute] = ''
                else:
                    data[attribute] = value
        return data