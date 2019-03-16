# -*- coding: utf-8 -*-
from plone.dexterity.content import Container
from plone.supermodel import model
from zope import schema
from zope.interface import implementer
from zope.schema.vocabulary import SimpleVocabulary

from edi.plonevocab import _

class IVocabularyFolder(model.Schema):
    """ Marker interface and Dexterity Python Schema for VocabularyFolder
    """

@implementer(IVocabularyFolder)
class VocabularyFolder(Container):
    """
    """
    def getVocabulary(self):
        return SimpleVocabulary([i.getTerm() for i in self.values()])
