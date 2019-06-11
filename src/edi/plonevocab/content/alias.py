# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Item
from plone.namedfile import field as namedfile
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer
from edi.plonevocab import _


class IAlias(model.Schema):
    """ Marker interface and Dexterity Python Schema for Alias
    """

    title = schema.TextLine(title=u"Titel es Alias Vocabulary Eintrages")

    key = schema.TextLine(title=u"Schlüsselwert",
                          description=u"Für diesen Wert sollen Alias-Einträge konfiguriert werden.")

    aliasentries = schema.List(title=u"Alias-Einträge",
                               value_type=schema.TextLine(),
                               description=u"Ein Eintrag pro Zeile")


@implementer(IAlias)
class Alias(Item):
    """
    """
