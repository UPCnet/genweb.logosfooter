from five import grok
from plone import api
from zope.interface import Interface

from plone.app.layout.viewlets.interfaces import IPortalFooter

from genweb.logosfooter.interfaces import IGenwebLogosfooterLayer

from genweb.banners import _
from genweb.core import utils

grok.context(Interface)


class logosFooterViewlet(grok.Viewlet):
    grok.name('genweb.logosfooter')
    grok.template('logosfooter')
    grok.viewletmanager(IPortalFooter)
    grok.layer(IGenwebLogosfooterLayer)

    def portal_url(self):
        return self.portal().absolute_url()

    def portal(self):
        return api.portal.get()

    def getLogosFooter(self):
        catalog = api.portal.get_tool(name='portal_catalog')
        lang = utils.pref_lang()
        return catalog.searchResults(portal_type='Logos_Footer',
                                     review_state=['published', 'intranet'],
                                     Language=lang,
                                     sort_on='getObjPositionInParent')

    def getAltAndTitle(self, altortitle):
        """ Funcio que extreu idioma actiu i afegeix al alt i al title de les imatges del banner
            el literal Obriu l'enllac en una finestra nova.
        """
        return '%s, %s' % (altortitle.decode('utf-8'),
            self.portal().translate(_('obrir_link_finestra_nova', default=u"(obriu en una finestra nova)")))
