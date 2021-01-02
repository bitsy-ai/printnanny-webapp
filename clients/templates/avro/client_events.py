import io
from fastavro import writer, reader, schemaless_writer
from fastavro.schema import load_schema
from os import path

basepath = path.dirname(__file__)

filename = '{basepath}/ObjectDetectEvent.avsc'.format(basepath=basepath)
schema = load_schema(filename)

class ObjectDetectEventSerializer:

    def schemaless_encode(self, client_event):
        bytes_writer = io.BytesIO()
        schemaless_writer(bytes_writer, schema, client_event)
        return bytes_writer.get_value()
    
    def encode(self, client_event):
        fo = BytesIO()
        writer(fo, schema, client_event)
        return fo.get_value()
    
    def decode(self, raw_bytes):
        fo = BytesIO()
        writer(fo, schema, raw_bytes)
        fo.seek(0)
        return record for record in reader(fo)    
