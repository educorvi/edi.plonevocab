# -*- coding: utf-8 -*-
from edi.plonevocab.content.alias import IAlias  # NOQA E501
from edi.plonevocab.testing import EDI_PLONEVOCAB_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest


try:
    from plone.dexterity.schema import portalTypeToSchemaName
except ImportError:
    # Plone < 5
    from plone.dexterity.utils import portalTypeToSchemaName


class AliasIntegrationTest(unittest.TestCase):

    layer = EDI_PLONEVOCAB_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            'Aliases',
            self.portal,
            'parent_id',
            title='Parent container',
        )
        self.parent = self.portal[parent_id]

    def test_ct_alias_schema(self):
        fti = queryUtility(IDexterityFTI, name='Alias')
        schema = fti.lookupSchema()
        self.assertEqual(IAlias, schema)

    def test_ct_alias_fti(self):
        fti = queryUtility(IDexterityFTI, name='Alias')
        self.assertTrue(fti)

    def test_ct_alias_factory(self):
        fti = queryUtility(IDexterityFTI, name='Alias')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IAlias.providedBy(obj),
            u'IAlias not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_alias_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='Alias',
            id='alias',
        )

        self.assertTrue(
            IAlias.providedBy(obj),
            u'IAlias not provided by {0}!'.format(
                obj.id,
            ),
        )
