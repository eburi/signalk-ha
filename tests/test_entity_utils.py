from types import SimpleNamespace

from custom_components.signalk_ha.entity_utils import (
    build_object_id,
    entity_id_prefix_for_entry,
    normalize_entity_id_prefix,
)


def test_normalize_entity_id_prefix() -> None:
    assert normalize_entity_id_prefix(None) == ""
    assert normalize_entity_id_prefix(123) == ""
    assert normalize_entity_id_prefix("   ") == ""
    assert normalize_entity_id_prefix("signalk") == "signalk_"
    assert normalize_entity_id_prefix("signalk_") == "signalk_"
    assert normalize_entity_id_prefix(" Signal K ") == "signal_k_"


def test_entity_id_prefix_for_entry() -> None:
    entry = SimpleNamespace(data={"entity_id_prefix": "Signal K"})
    assert entity_id_prefix_for_entry(entry) == "signal_k_"


def test_build_object_id() -> None:
    assert build_object_id("navigation.speedOverGround") == "navigation_speedoverground"
    assert (
        build_object_id("navigation.speedOverGround", prefix="signalk_")
        == "signalk_navigation_speedoverground"
    )
