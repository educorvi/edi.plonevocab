# -*- coding: utf-8 -*-
from edi.plonevocab.content.dictionary_key import IDictionaryKey  # NOQA E501
from edi.plonevocab.testing import EDI_PLONEVOCAB_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class DictionaryKeyIntegrationTest(unittest.TestCase):

    layer = EDI_PLONEVOCAB_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            'MenuDictionary',
            self.portal,
            'dictionary_key',
            title='Parent container',
        )
        self.parent = self.portal[parent_id]

    def test_ct_dictionary_key_schema(self):
        fti = queryUtility(IDexterityFTI, name='DictionaryKey')
        schema = fti.lookupSchema()
        self.assertEqual(IDictionaryKey, schema)

    def test_ct_dictionary_key_fti(self):
        fti = queryUtility(IDexterityFTI, name='DictionaryKey')
        self.assertTrue(fti)

    def test_ct_dictionary_key_factory(self):
        fti = queryUtility(IDexterityFTI, name='DictionaryKey')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IDictionaryKey.providedBy(obj),
            u'IDictionaryKey not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_dictionary_key_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='DictionaryKey',
            id='dictionary_key',
        )

        self.assertTrue(
            IDictionaryKey.providedBy(obj),
            u'IDictionaryKey not provided by {0}!'.format(
                obj.id,
            ),
        )

    def test_ct_dictionary_key_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='DictionaryKey')
        self.assertFalse(
            fti.global_allow,
            u'{0} is globally addable!'.format(fti.id)
        )

    def test_ct_dictionary_key_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='DictionaryKey')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'dictionary_key_id',
            title='DictionaryKey container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
