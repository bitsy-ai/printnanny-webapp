# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Telemetry

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Box(object):
    __slots__ = ['_tab']

    # Box
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Box
    def Ymin(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(0))
    # Box
    def Ymax(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(4))
    # Box
    def Xmin(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(8))
    # Box
    def Xmax(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(12))
    # Box
    def Score(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(16))
    # Box
    def ClassIndex(self): return self._tab.Get(flatbuffers.number_types.Int8Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(20))

def CreateBox(builder, ymin, ymax, xmin, xmax, score, classIndex):
    builder.Prep(4, 24)
    builder.Pad(3)
    builder.PrependInt8(classIndex)
    builder.PrependFloat32(score)
    builder.PrependFloat32(xmax)
    builder.PrependFloat32(xmin)
    builder.PrependFloat32(ymax)
    builder.PrependFloat32(ymin)
    return builder.Offset()


class BoxT(object):

    # BoxT
    def __init__(self):
        self.ymin = 0.0  # type: float
        self.ymax = 0.0  # type: float
        self.xmin = 0.0  # type: float
        self.xmax = 0.0  # type: float
        self.score = 0.0  # type: float
        self.classIndex = 0  # type: int

    @classmethod
    def InitFromBuf(cls, buf, pos):
        box = Box()
        box.Init(buf, pos)
        return cls.InitFromObj(box)

    @classmethod
    def InitFromObj(cls, box):
        x = BoxT()
        x._UnPack(box)
        return x

    # BoxT
    def _UnPack(self, box):
        if box is None:
            return
        self.ymin = box.Ymin()
        self.ymax = box.Ymax()
        self.xmin = box.Xmin()
        self.xmax = box.Xmax()
        self.score = box.Score()
        self.classIndex = box.ClassIndex()

    # BoxT
    def Pack(self, builder):
        return CreateBox(builder, self.ymin, self.ymax, self.xmin, self.xmax, self.score, self.classIndex)
