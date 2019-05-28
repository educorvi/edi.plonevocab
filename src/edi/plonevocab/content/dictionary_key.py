# -*- coding: utf-8 -*-
from plone.dexterity.content import Container
from plone.supermodel import model
from zope import schema
from zope.interface import implementer

from edi.plonevocab import _

class IDictionaryKey(model.Schema):
    """ Marker interface and Dexterity Python Schema for DictionaryKey
    """

    title = schema.TextLine(title=u"Titel")
    key = schema.TextLine(title=u"Key", description=u"Überschrift des Submenüs")

@implementer(IDictionaryKey)
class DictionaryKey(Container):
    """
    """
    def getDictKey(self):
        return [i.getTerm() for i in self.values()]
