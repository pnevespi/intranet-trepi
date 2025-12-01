"""Portal settings tests."""

from plone import api

import pytest


class TestPortalSettings:
    """Test portal settings."""

    @pytest.mark.parametrize(
        "key,expected",
        [
            ("plone.smtp_host", "localhost"),
            ("plone.smtp_port", 25),
            ("plone.twitter_username", "pnevespi"),
            ("plone.default_language", "pt-br"),
            (
                "plone.available_languages",
                [
                    "pt-br",
                ],
            ),
        ],
    )
    def test_settings(self, portal, key: str, expected: str | int | list[str]):
        """Test that the portal title is set correctly."""
        value = api.portal.get_registry_record(key)
        assert value == expected
