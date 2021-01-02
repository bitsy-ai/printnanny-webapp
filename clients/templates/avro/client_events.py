import avro.schema
import io
from avro.io import DatumReader, DatumWriter, BinaryEncoder
from os import path

basepath = path.dirname(__file__)

filename = '{basepath}/client_events.avsc'.format(basepath=basepath)
schema = avro.schema.parse(open(filename, "rb").read())

class ObjectDetectEventSerializer:

    def __init__(self):
        self.writer = DatumWriter(schema)
        self.reader = DatumReader(schema)

    
    def encode_bytes(self, client_events=[]):
        bytes_writer = io.BytesIO()
        encoder = BinaryEncoder(bytes_writer)
        for client_event in client_events:
            self.writer.write(client_event, encoder)
        return bytes_writer.get_value()

    def encode_bytes_io(self, client_events=[]):
        bytes_writer = io.BytesIO()
        encoder = BinaryEncoder(bytes_writer)
        for client_event in client_events:
            self.writer.write(client_event, encoder)
        return bytes_writer
    
    def decode_bytes(self, raw_bytes):
        bytes_reader = io.BytesIO(raw_bytes)
        decoder = BinaryDecoder(bytes_reader)
        client_events = []
        while bytes_reader.tell() < len(raw_bytes):
            client_events.append(self.reader.read(decoder))
        
        if len(client_events) == 1:
            return client_events[0]
        else:
            return client_events
