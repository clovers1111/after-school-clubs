from datetime import datetime, date
from uuid import UUID

from sqlalchemy.inspection import inspect
from sqlalchemy.orm import DeclarativeBase

class BaseEntity(DeclarativeBase):
    pass

    __abstract__ = True

    def to_dict(self):
        result = {}
        # Iterate through columns in response
        for column in inspect(self).mapper.column_attrs:
            value = getattr(self, column.key)
            # Convert non-JSON-native types
            if isinstance(value, (datetime, date)):
                value = value.isoformat()
            elif isinstance(value, UUID):
                value = str(value)
            result[column.key] = value
        return result