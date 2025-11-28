"""Portal settings tests."""

from plone import api


class TestPortalSettings:
    """Test that Portal configuration is correctly done."""

    def test_portal_social_media(self, portal):
        """Test portal Email."""
        value = api.portal.get_registry_record("plone.twitter_username")
        expected = "pnevespi"
        assert value == expected

    def test_portal_email(self, portal):
        """Test portal Email."""
        value = api.portal.get_registry_record("plone.email_from_name")
        expected = "Intranet Tribunal Eleitoral do PI"
        assert value == expected

    def test_portal_title(self, portal):
        """Test portal title."""
        value = api.portal.get_registry_record("plone.site_title")
        expected = "Intranet Tribunal Eleitoral do PI"
        assert value == expected
