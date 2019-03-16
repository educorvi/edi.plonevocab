# -*- coding: utf-8 -*-
from plone.autoform import directives
from plone.dexterity.content import Item
from plone.supermodel import model
from zope import schema
from zope.interface import implementer
from zope.schema.vocabulary import SimpleTerm

from edi.plonevocab import _

class IVocabularyTerm(model.Schema):
    """ Marker interface and Dexterity Python Schema for VocabularyTerm
    """
    
    value = schema.TextLine(title=u"Value", description=u"Keine Umlaute, Sonderzeichen, Leerzeichen, eindeutiger Wert innerhalb eines Ordners.")
    token = schema.TextLine(title=u"Token", description=u"keine Umlaute, Sonderzeichen, Leerzeichen, oft werden für Value und Token die\
                                                          selben Werte verwendet.")

@implementer(IVocabularyTerm)
class VocabularyTerm(Item):
    """
    """
    def getTerm(self):
        return SimpleTerm(value=self.value, token=self.token, title=self.title)
