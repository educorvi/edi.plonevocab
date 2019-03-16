# -*- coding: utf-8 -*-
from edi.plonevocab.content.vocabulary_term import IVocabularyTerm  # NOQA E501
from edi.plonevocab.testing import EDI_PLONEVOCAB_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class VocabularyTermIntegrationTest(unittest.TestCase):

    layer = EDI_PLONEVOCAB_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            'VocabularyFolder',
            self.portal,
            'vocabulary_term',
            title='Parent container',
        )
        self.parent = self.portal[parent_id]

    def test_ct_vocabulary_term_schema(self):
        fti = queryUtility(IDexterityFTI, name='VocabularyTerm')
        schema = fti.lookupSchema()
        self.assertEqual(IVocabularyTerm, schema)

    def test_ct_vocabulary_term_fti(self):
        fti = queryUtility(IDexterityFTI, name='VocabularyTerm')
        self.assertTrue(fti)

    def test_ct_vocabulary_term_factory(self):
        fti = queryUtility(IDexterityFTI, name='VocabularyTerm')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IVocabularyTerm.providedBy(obj),
            u'IVocabularyTerm not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_vocabulary_term_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='VocabularyTerm',
            id='vocabulary_term',
        )

        self.assertTrue(
            IVocabularyTerm.providedBy(obj),
            u'IVocabularyTerm not provided by {0}!'.format(
                obj.id,
            ),
        )

    def test_ct_vocabulary_term_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='VocabularyTerm')
        self.assertFalse(
            fti.global_allow,
            u'{0} is globally addable!'.format(fti.id)
        )
