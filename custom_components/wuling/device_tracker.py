from __future__ import annotations

import logging

from homeassistant.components.device_tracker import (
    DOMAIN as ENTITY_DOMAIN,
    TrackerEntity as BaseEntity,
    SourceType,
)

from . import XEntity

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[entry.entry_id]['coordinator']
    for conv in coordinator.converters:
        if conv.parent or conv.domain != ENTITY_DOMAIN:
            continue
        async_add_entities([TrackerEntity(coordinator, conv)])


class TrackerEntity(XEntity, BaseEntity):
    @property
    def source_type(self) -> SourceType | str:
        """Return the source type, eg gps or router, of the device."""
        return SourceType.GPS

    @property
    def latitude(self) -> float | None:
        """Return latitude value of the device."""
        return self._attr_extra_state_attributes.get('latitude')

    @property
    def longitude(self) -> float | None:
        """Return longitude value of the device."""
        return self._attr_extra_state_attributes.get('longitude')
