import io
from fastavro import schemaless_writer, reader, load_schema
from os import path

basepath = path.dirname(__file__)

filename = '{basepath}/client_events.avsc'.format(basepath=basepath)
schema = load_schema(filename)

class ObjectDetectEventSerializer:

    def __init__(self):
        self.writer = DatumWriter(schema)
        self.reader = DatumReader(schema)

    def schemaless_encode(self, client_event):
        bytes_writer = io.BytesIO()
        schemaless_writer(bytes_writer, schema, client_event)
        return bytes_writer.get_value()