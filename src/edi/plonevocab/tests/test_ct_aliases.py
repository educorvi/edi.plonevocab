# -*- coding: utf-8 -*-
from edi.plonevocab.content.aliases import IAliases  # NOQA E501
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


class AliasesIntegrationTest(unittest.TestCase):

    layer = EDI_PLONEVOCAB_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_ct_aliases_schema(self):
        fti = queryUtility(IDexterityFTI, name='Aliases')
        schema = fti.lookupSchema()
        self.assertEqual(IAliases, schema)

    def test_ct_aliases_fti(self):
        fti = queryUtility(IDexterityFTI, name='Aliases')
        self.assertTrue(fti)

    def test_ct_aliases_factory(self):
        fti = queryUtility(IDexterityFTI, name='Aliases')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IAliases.providedBy(obj),
            u'IAliases not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_aliases_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Aliases',
            id='aliases',
        )

        self.assertTrue(
            IAliases.providedBy(obj),
            u'IAliases not provided by {0}!'.format(
                obj.id,
            ),
        )
