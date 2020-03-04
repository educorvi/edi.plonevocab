# -*- coding: utf-8 -*-
from plone.dexterity.content import Container
from plone.supermodel import model
from zope import schema
from zope.interface import implementer, provider
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.interfaces import IContextSourceBinder

from edi.plonevocab import _

class IVocabularyFolder(model.Schema):
    """ Marker interface and Dexterity Python Schema for VocabularyFolder
    """
    title = schema.TextLine(title=u'Titel')
    vocabid = schema.TextLine(title=u"Id des Vocabularies Beispiel: uvc.desinfektionsmittel.wirkung")

@implementer(IVocabularyFolder)
class VocabularyFolder(Container):
    """
    """
    @provider(IContextSourceBinder)
    def getVocabulary(self):
        return SimpleVocabulary([i.getTerm() for i in self.values()])
