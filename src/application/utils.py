from sqlalchemy.inspection import inspect


def convert_entity_to_model(ObjectEntity, ObjectModel, data):
    attributes = {c.key: getattr(data, c.key) for c in inspect(ObjectEntity).mapper.column_attrs}
    return ObjectModel(**attributes)
