"""Portal settings tests."""

from plone import api



class TestPortalSettings:
    """Test portal settings."""

    def test_settings(self, portal, key: str, expected: str | int | list[str]):
        """Test that the portal title is set correctly."""
        value = api.portal.get_registry_record(key)
        assert value == expected
