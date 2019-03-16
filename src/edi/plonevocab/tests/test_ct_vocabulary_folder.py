# -*- coding: utf-8 -*-
from edi.plonevocab.content.vocabulary_folder import IVocabularyFolder  # NOQA E501
from edi.plonevocab.testing import EDI_PLONEVOCAB_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class VocabularyFolderIntegrationTest(unittest.TestCase):

    layer = EDI_PLONEVOCAB_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_ct_vocabulary_folder_schema(self):
        fti = queryUtility(IDexterityFTI, name='VocabularyFolder')
        schema = fti.lookupSchema()
        self.assertEqual(IVocabularyFolder, schema)

    def test_ct_vocabulary_folder_fti(self):
        fti = queryUtility(IDexterityFTI, name='VocabularyFolder')
        self.assertTrue(fti)

    def test_ct_vocabulary_folder_factory(self):
        fti = queryUtility(IDexterityFTI, name='VocabularyFolder')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IVocabularyFolder.providedBy(obj),
            u'IVocabularyFolder not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_vocabulary_folder_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='VocabularyFolder',
            id='vocabulary_folder',
        )

        self.assertTrue(
            IVocabularyFolder.providedBy(obj),
            u'IVocabularyFolder not provided by {0}!'.format(
                obj.id,
            ),
        )

    def test_ct_vocabulary_folder_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='VocabularyFolder')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_vocabulary_folder_filter_content_type_false(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='VocabularyFolder')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'vocabulary_folder_id',
            title='VocabularyFolder container',
         )
        self.parent = self.portal[parent_id]
        obj = api.content.create(
            container=self.parent,
            type='Document',
            title='My Content',
        )
        self.assertTrue(
            obj,
            u'Cannot add {0} to {1} container!'.format(obj.id, fti.id)
        )
