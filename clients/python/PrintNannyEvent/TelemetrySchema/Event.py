# automatically generated by the FlatBuffers compiler, do not modify

# namespace: TelemetrySchema

class Event(object):
    NONE = 0
    MonitoringFrame = 1


def EventCreator(unionType, table):
    from flatbuffers.table import Table
    if not isinstance(table, Table):
        return None
    if unionType == Event().MonitoringFrame:
        import PrintNannyEvent.TelemetrySchema.MonitoringFrame
        return PrintNannyEvent.TelemetrySchema.MonitoringFrame.MonitoringFrameT.InitFromBuf(table.Bytes, table.Pos)
    return None
