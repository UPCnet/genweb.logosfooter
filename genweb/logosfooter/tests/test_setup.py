# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from genweb.logosfooter.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of genweb.logosfooter into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if genweb.logosfooter is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('genweb.logosfooter'))

    def test_uninstall(self):
        """Test if genweb.logosfooter is cleanly uninstalled."""
        self.installer.uninstallProducts(['genweb.logosfooter'])
        self.assertFalse(self.installer.isProductInstalled('genweb.logosfooter'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IGenwebLogosfooterLayer is registered."""
        from genweb.logosfooter.interfaces import IGenwebLogosfooterLayer
        from plone.browserlayer import utils
        self.failUnless(IGenwebLogosfooterLayer in utils.registered_layers())
