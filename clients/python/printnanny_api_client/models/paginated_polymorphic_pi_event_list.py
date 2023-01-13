from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pi_boot_command import PiBootCommand
    from ..models.pi_boot_status import PiBootStatus
    from ..models.pi_cam_command import PiCamCommand
    from ..models.pi_cam_status import PiCamStatus
    from ..models.pi_software_update_command import PiSoftwareUpdateCommand
    from ..models.pi_software_update_status import PiSoftwareUpdateStatus


T = TypeVar("T", bound="PaginatedPolymorphicPiEventList")


@attr.s(auto_attribs=True)
class PaginatedPolymorphicPiEventList:
    """
    Attributes:
        count (Union[Unset, int]):  Example: 123.
        next_ (Union[Unset, None, str]):  Example: http://api.example.org/accounts/?page=4.
        previous (Union[Unset, None, str]):  Example: http://api.example.org/accounts/?page=2.
        results (Union[Unset, List[Union['PiBootCommand', 'PiBootStatus', 'PiCamCommand', 'PiCamStatus',
            'PiSoftwareUpdateCommand', 'PiSoftwareUpdateStatus']]]):
    """

    count: Union[Unset, int] = UNSET
    next_: Union[Unset, None, str] = UNSET
    previous: Union[Unset, None, str] = UNSET
    results: Union[
        Unset,
        List[
            Union[
                "PiBootCommand",
                "PiBootStatus",
                "PiCamCommand",
                "PiCamStatus",
                "PiSoftwareUpdateCommand",
                "PiSoftwareUpdateStatus",
            ]
        ],
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.pi_boot_status import PiBootStatus
        from ..models.pi_cam_command import PiCamCommand
        from ..models.pi_cam_status import PiCamStatus
        from ..models.pi_software_update_command import PiSoftwareUpdateCommand
        from ..models.pi_software_update_status import PiSoftwareUpdateStatus

        count = self.count
        next_ = self.next_
        previous = self.previous
        results: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item: Dict[str, Any]

                if isinstance(results_item_data, PiCamStatus):
                    results_item = results_item_data.to_dict()

                elif isinstance(results_item_data, PiSoftwareUpdateStatus):
                    results_item = results_item_data.to_dict()

                elif isinstance(results_item_data, PiBootStatus):
                    results_item = results_item_data.to_dict()

                elif isinstance(results_item_data, PiCamCommand):
                    results_item = results_item_data.to_dict()

                elif isinstance(results_item_data, PiSoftwareUpdateCommand):
                    results_item = results_item_data.to_dict()

                else:
                    results_item = results_item_data.to_dict()

                results.append(results_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if next_ is not UNSET:
            field_dict["next"] = next_
        if previous is not UNSET:
            field_dict["previous"] = previous
        if results is not UNSET:
            field_dict["results"] = results

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pi_boot_command import PiBootCommand
        from ..models.pi_boot_status import PiBootStatus
        from ..models.pi_cam_command import PiCamCommand
        from ..models.pi_cam_status import PiCamStatus
        from ..models.pi_software_update_command import PiSoftwareUpdateCommand
        from ..models.pi_software_update_status import PiSoftwareUpdateStatus

        d = src_dict.copy()
        count = d.pop("count", UNSET)

        next_ = d.pop("next", UNSET)

        previous = d.pop("previous", UNSET)

        results = []
        _results = d.pop("results", UNSET)
        for results_item_data in _results or []:

            def _parse_results_item(
                data: object,
            ) -> Union[
                "PiBootCommand",
                "PiBootStatus",
                "PiCamCommand",
                "PiCamStatus",
                "PiSoftwareUpdateCommand",
                "PiSoftwareUpdateStatus",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_polymorphic_pi_event_type_0 = PiCamStatus.from_dict(data)

                    return componentsschemas_polymorphic_pi_event_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_polymorphic_pi_event_type_1 = PiSoftwareUpdateStatus.from_dict(data)

                    return componentsschemas_polymorphic_pi_event_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_polymorphic_pi_event_type_2 = PiBootStatus.from_dict(data)

                    return componentsschemas_polymorphic_pi_event_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_polymorphic_pi_event_type_3 = PiCamCommand.from_dict(data)

                    return componentsschemas_polymorphic_pi_event_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_polymorphic_pi_event_type_4 = PiSoftwareUpdateCommand.from_dict(data)

                    return componentsschemas_polymorphic_pi_event_type_4
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_polymorphic_pi_event_type_5 = PiBootCommand.from_dict(data)

                return componentsschemas_polymorphic_pi_event_type_5

            results_item = _parse_results_item(results_item_data)

            results.append(results_item)

        paginated_polymorphic_pi_event_list = cls(
            count=count,
            next_=next_,
            previous=previous,
            results=results,
        )

        paginated_polymorphic_pi_event_list.additional_properties = d
        return paginated_polymorphic_pi_event_list

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
