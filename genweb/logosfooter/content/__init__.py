from zope.interface import implements

from plone.dexterity.content import Item
from plone.dexterity.content import Container
from plone.app.contenttypes.interfaces import IFolder

from genweb.banners.content.banner import IBanner


class Logo(Item):
    implements(IBanner)


class LogoContainer(Container):
    implements(IFolder)
