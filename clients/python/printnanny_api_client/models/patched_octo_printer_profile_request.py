import json
from typing import TYPE_CHECKING, Any, Dict, List, Tuple, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patched_octo_printer_profile_request_volume_custom_box import (
        PatchedOctoPrinterProfileRequestVolumeCustomBox,
    )


T = TypeVar("T", bound="PatchedOctoPrinterProfileRequest")


@attr.s(auto_attribs=True)
class PatchedOctoPrinterProfileRequest:
    """
    Attributes:
        axes_e_inverted (Union[Unset, None, bool]):
        axes_e_speed (Union[Unset, None, int]):
        axes_x_speed (Union[Unset, None, int]):
        axes_x_inverted (Union[Unset, None, bool]):
        axes_y_inverted (Union[Unset, None, bool]):
        axes_y_speed (Union[Unset, None, int]):
        axes_z_inverted (Union[Unset, None, bool]):
        axes_z_speed (Union[Unset, None, int]):
        extruder_count (Union[Unset, None, int]):
        extruder_nozzle_diameter (Union[Unset, None, float]):
        extruder_shared_nozzle (Union[Unset, None, bool]):
        heated_bed (Union[Unset, None, bool]):
        heated_chamber (Union[Unset, None, bool]):
        model (Union[Unset, None, str]):
        name (Union[Unset, str]):
        octoprint_key (Union[Unset, str]):
        volume_custom_box (Union[Unset, PatchedOctoPrinterProfileRequestVolumeCustomBox]):
        volume_depth (Union[Unset, None, float]):
        volume_formfactor (Union[Unset, None, str]):
        volume_height (Union[Unset, None, float]):
        volume_origin (Union[Unset, None, str]):
        volume_width (Union[Unset, None, float]):
    """

    axes_e_inverted: Union[Unset, None, bool] = UNSET
    axes_e_speed: Union[Unset, None, int] = UNSET
    axes_x_speed: Union[Unset, None, int] = UNSET
    axes_x_inverted: Union[Unset, None, bool] = UNSET
    axes_y_inverted: Union[Unset, None, bool] = UNSET
    axes_y_speed: Union[Unset, None, int] = UNSET
    axes_z_inverted: Union[Unset, None, bool] = UNSET
    axes_z_speed: Union[Unset, None, int] = UNSET
    extruder_count: Union[Unset, None, int] = UNSET
    extruder_nozzle_diameter: Union[Unset, None, float] = UNSET
    extruder_shared_nozzle: Union[Unset, None, bool] = UNSET
    heated_bed: Union[Unset, None, bool] = UNSET
    heated_chamber: Union[Unset, None, bool] = UNSET
    model: Union[Unset, None, str] = UNSET
    name: Union[Unset, str] = UNSET
    octoprint_key: Union[Unset, str] = UNSET
    volume_custom_box: Union[Unset, "PatchedOctoPrinterProfileRequestVolumeCustomBox"] = UNSET
    volume_depth: Union[Unset, None, float] = UNSET
    volume_formfactor: Union[Unset, None, str] = UNSET
    volume_height: Union[Unset, None, float] = UNSET
    volume_origin: Union[Unset, None, str] = UNSET
    volume_width: Union[Unset, None, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        axes_e_inverted = self.axes_e_inverted
        axes_e_speed = self.axes_e_speed
        axes_x_speed = self.axes_x_speed
        axes_x_inverted = self.axes_x_inverted
        axes_y_inverted = self.axes_y_inverted
        axes_y_speed = self.axes_y_speed
        axes_z_inverted = self.axes_z_inverted
        axes_z_speed = self.axes_z_speed
        extruder_count = self.extruder_count
        extruder_nozzle_diameter = self.extruder_nozzle_diameter
        extruder_shared_nozzle = self.extruder_shared_nozzle
        heated_bed = self.heated_bed
        heated_chamber = self.heated_chamber
        model = self.model
        name = self.name
        octoprint_key = self.octoprint_key
        volume_custom_box: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.volume_custom_box, Unset):
            volume_custom_box = self.volume_custom_box.to_dict()

        volume_depth = self.volume_depth
        volume_formfactor = self.volume_formfactor
        volume_height = self.volume_height
        volume_origin = self.volume_origin
        volume_width = self.volume_width

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if axes_e_inverted is not UNSET:
            field_dict["axes_e_inverted"] = axes_e_inverted
        if axes_e_speed is not UNSET:
            field_dict["axes_e_speed"] = axes_e_speed
        if axes_x_speed is not UNSET:
            field_dict["axes_x_speed"] = axes_x_speed
        if axes_x_inverted is not UNSET:
            field_dict["axes_x_inverted"] = axes_x_inverted
        if axes_y_inverted is not UNSET:
            field_dict["axes_y_inverted"] = axes_y_inverted
        if axes_y_speed is not UNSET:
            field_dict["axes_y_speed"] = axes_y_speed
        if axes_z_inverted is not UNSET:
            field_dict["axes_z_inverted"] = axes_z_inverted
        if axes_z_speed is not UNSET:
            field_dict["axes_z_speed"] = axes_z_speed
        if extruder_count is not UNSET:
            field_dict["extruder_count"] = extruder_count
        if extruder_nozzle_diameter is not UNSET:
            field_dict["extruder_nozzle_diameter"] = extruder_nozzle_diameter
        if extruder_shared_nozzle is not UNSET:
            field_dict["extruder_shared_nozzle"] = extruder_shared_nozzle
        if heated_bed is not UNSET:
            field_dict["heated_bed"] = heated_bed
        if heated_chamber is not UNSET:
            field_dict["heated_chamber"] = heated_chamber
        if model is not UNSET:
            field_dict["model"] = model
        if name is not UNSET:
            field_dict["name"] = name
        if octoprint_key is not UNSET:
            field_dict["octoprint_key"] = octoprint_key
        if volume_custom_box is not UNSET:
            field_dict["volume_custom_box"] = volume_custom_box
        if volume_depth is not UNSET:
            field_dict["volume_depth"] = volume_depth
        if volume_formfactor is not UNSET:
            field_dict["volume_formfactor"] = volume_formfactor
        if volume_height is not UNSET:
            field_dict["volume_height"] = volume_height
        if volume_origin is not UNSET:
            field_dict["volume_origin"] = volume_origin
        if volume_width is not UNSET:
            field_dict["volume_width"] = volume_width

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        axes_e_inverted = (
            self.axes_e_inverted
            if isinstance(self.axes_e_inverted, Unset)
            else (None, str(self.axes_e_inverted).encode(), "text/plain")
        )
        axes_e_speed = (
            self.axes_e_speed
            if isinstance(self.axes_e_speed, Unset)
            else (None, str(self.axes_e_speed).encode(), "text/plain")
        )
        axes_x_speed = (
            self.axes_x_speed
            if isinstance(self.axes_x_speed, Unset)
            else (None, str(self.axes_x_speed).encode(), "text/plain")
        )
        axes_x_inverted = (
            self.axes_x_inverted
            if isinstance(self.axes_x_inverted, Unset)
            else (None, str(self.axes_x_inverted).encode(), "text/plain")
        )
        axes_y_inverted = (
            self.axes_y_inverted
            if isinstance(self.axes_y_inverted, Unset)
            else (None, str(self.axes_y_inverted).encode(), "text/plain")
        )
        axes_y_speed = (
            self.axes_y_speed
            if isinstance(self.axes_y_speed, Unset)
            else (None, str(self.axes_y_speed).encode(), "text/plain")
        )
        axes_z_inverted = (
            self.axes_z_inverted
            if isinstance(self.axes_z_inverted, Unset)
            else (None, str(self.axes_z_inverted).encode(), "text/plain")
        )
        axes_z_speed = (
            self.axes_z_speed
            if isinstance(self.axes_z_speed, Unset)
            else (None, str(self.axes_z_speed).encode(), "text/plain")
        )
        extruder_count = (
            self.extruder_count
            if isinstance(self.extruder_count, Unset)
            else (None, str(self.extruder_count).encode(), "text/plain")
        )
        extruder_nozzle_diameter = (
            self.extruder_nozzle_diameter
            if isinstance(self.extruder_nozzle_diameter, Unset)
            else (None, str(self.extruder_nozzle_diameter).encode(), "text/plain")
        )
        extruder_shared_nozzle = (
            self.extruder_shared_nozzle
            if isinstance(self.extruder_shared_nozzle, Unset)
            else (None, str(self.extruder_shared_nozzle).encode(), "text/plain")
        )
        heated_bed = (
            self.heated_bed
            if isinstance(self.heated_bed, Unset)
            else (None, str(self.heated_bed).encode(), "text/plain")
        )
        heated_chamber = (
            self.heated_chamber
            if isinstance(self.heated_chamber, Unset)
            else (None, str(self.heated_chamber).encode(), "text/plain")
        )
        model = self.model if isinstance(self.model, Unset) else (None, str(self.model).encode(), "text/plain")
        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")
        octoprint_key = (
            self.octoprint_key
            if isinstance(self.octoprint_key, Unset)
            else (None, str(self.octoprint_key).encode(), "text/plain")
        )
        volume_custom_box: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.volume_custom_box, Unset):
            volume_custom_box = (None, json.dumps(self.volume_custom_box.to_dict()).encode(), "application/json")

        volume_depth = (
            self.volume_depth
            if isinstance(self.volume_depth, Unset)
            else (None, str(self.volume_depth).encode(), "text/plain")
        )
        volume_formfactor = (
            self.volume_formfactor
            if isinstance(self.volume_formfactor, Unset)
            else (None, str(self.volume_formfactor).encode(), "text/plain")
        )
        volume_height = (
            self.volume_height
            if isinstance(self.volume_height, Unset)
            else (None, str(self.volume_height).encode(), "text/plain")
        )
        volume_origin = (
            self.volume_origin
            if isinstance(self.volume_origin, Unset)
            else (None, str(self.volume_origin).encode(), "text/plain")
        )
        volume_width = (
            self.volume_width
            if isinstance(self.volume_width, Unset)
            else (None, str(self.volume_width).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
        if axes_e_inverted is not UNSET:
            field_dict["axes_e_inverted"] = axes_e_inverted
        if axes_e_speed is not UNSET:
            field_dict["axes_e_speed"] = axes_e_speed
        if axes_x_speed is not UNSET:
            field_dict["axes_x_speed"] = axes_x_speed
        if axes_x_inverted is not UNSET:
            field_dict["axes_x_inverted"] = axes_x_inverted
        if axes_y_inverted is not UNSET:
            field_dict["axes_y_inverted"] = axes_y_inverted
        if axes_y_speed is not UNSET:
            field_dict["axes_y_speed"] = axes_y_speed
        if axes_z_inverted is not UNSET:
            field_dict["axes_z_inverted"] = axes_z_inverted
        if axes_z_speed is not UNSET:
            field_dict["axes_z_speed"] = axes_z_speed
        if extruder_count is not UNSET:
            field_dict["extruder_count"] = extruder_count
        if extruder_nozzle_diameter is not UNSET:
            field_dict["extruder_nozzle_diameter"] = extruder_nozzle_diameter
        if extruder_shared_nozzle is not UNSET:
            field_dict["extruder_shared_nozzle"] = extruder_shared_nozzle
        if heated_bed is not UNSET:
            field_dict["heated_bed"] = heated_bed
        if heated_chamber is not UNSET:
            field_dict["heated_chamber"] = heated_chamber
        if model is not UNSET:
            field_dict["model"] = model
        if name is not UNSET:
            field_dict["name"] = name
        if octoprint_key is not UNSET:
            field_dict["octoprint_key"] = octoprint_key
        if volume_custom_box is not UNSET:
            field_dict["volume_custom_box"] = volume_custom_box
        if volume_depth is not UNSET:
            field_dict["volume_depth"] = volume_depth
        if volume_formfactor is not UNSET:
            field_dict["volume_formfactor"] = volume_formfactor
        if volume_height is not UNSET:
            field_dict["volume_height"] = volume_height
        if volume_origin is not UNSET:
            field_dict["volume_origin"] = volume_origin
        if volume_width is not UNSET:
            field_dict["volume_width"] = volume_width

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patched_octo_printer_profile_request_volume_custom_box import (
            PatchedOctoPrinterProfileRequestVolumeCustomBox,
        )

        d = src_dict.copy()
        axes_e_inverted = d.pop("axes_e_inverted", UNSET)

        axes_e_speed = d.pop("axes_e_speed", UNSET)

        axes_x_speed = d.pop("axes_x_speed", UNSET)

        axes_x_inverted = d.pop("axes_x_inverted", UNSET)

        axes_y_inverted = d.pop("axes_y_inverted", UNSET)

        axes_y_speed = d.pop("axes_y_speed", UNSET)

        axes_z_inverted = d.pop("axes_z_inverted", UNSET)

        axes_z_speed = d.pop("axes_z_speed", UNSET)

        extruder_count = d.pop("extruder_count", UNSET)

        extruder_nozzle_diameter = d.pop("extruder_nozzle_diameter", UNSET)

        extruder_shared_nozzle = d.pop("extruder_shared_nozzle", UNSET)

        heated_bed = d.pop("heated_bed", UNSET)

        heated_chamber = d.pop("heated_chamber", UNSET)

        model = d.pop("model", UNSET)

        name = d.pop("name", UNSET)

        octoprint_key = d.pop("octoprint_key", UNSET)

        _volume_custom_box = d.pop("volume_custom_box", UNSET)
        volume_custom_box: Union[Unset, PatchedOctoPrinterProfileRequestVolumeCustomBox]
        if isinstance(_volume_custom_box, Unset):
            volume_custom_box = UNSET
        else:
            volume_custom_box = PatchedOctoPrinterProfileRequestVolumeCustomBox.from_dict(_volume_custom_box)

        volume_depth = d.pop("volume_depth", UNSET)

        volume_formfactor = d.pop("volume_formfactor", UNSET)

        volume_height = d.pop("volume_height", UNSET)

        volume_origin = d.pop("volume_origin", UNSET)

        volume_width = d.pop("volume_width", UNSET)

        patched_octo_printer_profile_request = cls(
            axes_e_inverted=axes_e_inverted,
            axes_e_speed=axes_e_speed,
            axes_x_speed=axes_x_speed,
            axes_x_inverted=axes_x_inverted,
            axes_y_inverted=axes_y_inverted,
            axes_y_speed=axes_y_speed,
            axes_z_inverted=axes_z_inverted,
            axes_z_speed=axes_z_speed,
            extruder_count=extruder_count,
            extruder_nozzle_diameter=extruder_nozzle_diameter,
            extruder_shared_nozzle=extruder_shared_nozzle,
            heated_bed=heated_bed,
            heated_chamber=heated_chamber,
            model=model,
            name=name,
            octoprint_key=octoprint_key,
            volume_custom_box=volume_custom_box,
            volume_depth=volume_depth,
            volume_formfactor=volume_formfactor,
            volume_height=volume_height,
            volume_origin=volume_origin,
            volume_width=volume_width,
        )

        patched_octo_printer_profile_request.additional_properties = d
        return patched_octo_printer_profile_request

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
