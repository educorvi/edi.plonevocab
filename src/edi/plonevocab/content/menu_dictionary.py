# -*- coding: utf-8 -*-
from plone.dexterity.content import Container
from plone.supermodel import model
from zope import schema
from zope.interface import implementer

from edi.plonevocab import _

class IMenuDictionary(model.Schema):
    """
    """
    title = schema.TextLine(title=u"Titel")

@implementer(IMenuDictionary)
class MenuDictionary(Container):
    """
    """
    def getMenuDict(self):
        ret = {}
        for i in self.values():
            ret[i.key] = i.getDictKey()
        return ret
