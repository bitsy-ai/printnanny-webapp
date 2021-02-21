# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Telemetry

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Image(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsImage(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Image()
        x.Init(buf, n + offset)
        return x

    # Image
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Image
    def Width(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # Image
    def Height(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # Image
    def Data(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Image
    def DataAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Image
    def DataLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Image
    def DataIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

def ImageStart(builder): builder.StartObject(3)
def ImageAddWidth(builder, width): builder.PrependUint32Slot(0, width, 0)
def ImageAddHeight(builder, height): builder.PrependUint32Slot(1, height, 0)
def ImageAddData(builder, data): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(data), 0)
def ImageStartDataVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def ImageEnd(builder): return builder.EndObject()

try:
    from typing import List
except:
    pass

class ImageT(object):

    # ImageT
    def __init__(self):
        self.width = 0  # type: int
        self.height = 0  # type: int
        self.data = None  # type: List[int]

    @classmethod
    def InitFromBuf(cls, buf, pos):
        image = Image()
        image.Init(buf, pos)
        return cls.InitFromObj(image)

    @classmethod
    def InitFromObj(cls, image):
        x = ImageT()
        x._UnPack(image)
        return x

    # ImageT
    def _UnPack(self, image):
        if image is None:
            return
        self.width = image.Width()
        self.height = image.Height()
        if not image.DataIsNone():
            if np is None:
                self.data = []
                for i in range(image.DataLength()):
                    self.data.append(image.Data(i))
            else:
                self.data = image.DataAsNumpy()

    # ImageT
    def Pack(self, builder):
        if self.data is not None:
            if np is not None and type(self.data) is np.ndarray:
                data = builder.CreateNumpyVector(self.data)
            else:
                ImageStartDataVector(builder, len(self.data))
                for i in reversed(range(len(self.data))):
                    builder.PrependUint8(self.data[i])
                data = builder.EndVector(len(self.data))
        ImageStart(builder)
        ImageAddWidth(builder, self.width)
        ImageAddHeight(builder, self.height)
        if self.data is not None:
            ImageAddData(builder, data)
        image = ImageEnd(builder)
        return image
