from custom_components.signalk_ha.mapping import (
    Conversion,
    angle_unit_for_path,
    apply_conversion,
    expected_units,
    lookup_mapping,
)


def test_apply_conversion_variants() -> None:
    assert apply_conversion(1.0, Conversion.RAD_TO_DEG) == 57.29577951308232
    assert apply_conversion(1.0, Conversion.MS_TO_KNOTS) == 1.9438444924406
    assert apply_conversion(300.0, Conversion.K_TO_C) == 26.850000000000023
    assert apply_conversion(100.0, Conversion.PA_TO_HPA) == 1.0
    assert apply_conversion(0.5, Conversion.RATIO_TO_PERCENT) == 50.0
    assert apply_conversion(10.0, None) == 10.0


def test_lookup_mapping_expected_units() -> None:
    mapping = lookup_mapping("navigation.speedOverGround")
    assert mapping is not None
    assert "m/s" in expected_units(mapping)

    assert lookup_mapping("navigation.unknown.path") is None


def test_angle_units_and_display_names() -> None:
    assert angle_unit_for_path("navigation.headingTrue") == "° T"
    assert angle_unit_for_path("navigation.headingMagnetic") == "° M"
    assert angle_unit_for_path("navigation.headingCompass") == "° C"
    assert angle_unit_for_path("environment.wind.angleApparent") == "°"

    sog = lookup_mapping("navigation.speedOverGround")
    assert sog is not None
    assert sog.display_name == "SOG"

    gwd = lookup_mapping("environment.wind.directionTrue")
    assert gwd is not None
    assert gwd.display_name == "GWD"
    assert gwd.unit == "° T"
    assert gwd.state_class is None
