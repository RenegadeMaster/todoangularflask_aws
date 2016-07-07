from datetime import datetime

from pynamodb.indexes import GlobalSecondaryIndex, AllProjection
from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute, NumberAttribute, UnicodeSetAttribute, UTCDateTimeAttribute,
    BooleanAttribute)


class ListIndex(GlobalSecondaryIndex):
    """
    This class represents a global secondary index
    """
    class Meta:
        # index_name is optional, but can be provided to override the default name
        index_name = 'list-index'
        read_capacity_units = 1
        write_capacity_units = 1
        # All attributes are projected
        projection = AllProjection()

    # This attribute is the hash key for the index
    # Note that this attribute must also exist
    # in the model
    list = UnicodeAttribute(hash_key=True)

class Todo(Model):
    class Meta:
        table_name = 'todosrich'
        region = 'us-east-1'
    uuid = UnicodeAttribute(hash_key=True)
    task = UnicodeAttribute()
    done = BooleanAttribute()
    date = UTCDateTimeAttribute()
    owner = UnicodeAttribute()
    list_index = ListIndex()
    list = UnicodeAttribute()
