# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import edi.plonevocab


class EdiPlonevocabLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=edi.plonevocab)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'edi.plonevocab:default')


EDI_PLONEVOCAB_FIXTURE = EdiPlonevocabLayer()


EDI_PLONEVOCAB_INTEGRATION_TESTING = IntegrationTesting(
    bases=(EDI_PLONEVOCAB_FIXTURE,),
    name='EdiPlonevocabLayer:IntegrationTesting',
)


EDI_PLONEVOCAB_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(EDI_PLONEVOCAB_FIXTURE,),
    name='EdiPlonevocabLayer:FunctionalTesting',
)


EDI_PLONEVOCAB_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        EDI_PLONEVOCAB_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='EdiPlonevocabLayer:AcceptanceTesting',
)
