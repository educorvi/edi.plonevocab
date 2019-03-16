# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s edi.plonevocab -t test_vocabulary_term.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src edi.plonevocab.testing.EDI_PLONEVOCAB_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/edi/plonevocab/tests/robot/test_vocabulary_term.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a VocabularyTerm
  Given a logged-in site administrator
    and an add VocabularyFolder form
   When I type 'My VocabularyTerm' into the title field
    and I submit the form
   Then a VocabularyTerm with the title 'My VocabularyTerm' has been created

Scenario: As a site administrator I can view a VocabularyTerm
  Given a logged-in site administrator
    and a VocabularyTerm 'My VocabularyTerm'
   When I go to the VocabularyTerm view
   Then I can see the VocabularyTerm title 'My VocabularyTerm'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add VocabularyFolder form
  Go To  ${PLONE_URL}/++add++VocabularyFolder

a VocabularyTerm 'My VocabularyTerm'
  Create content  type=VocabularyFolder  id=my-vocabulary_term  title=My VocabularyTerm

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the VocabularyTerm view
  Go To  ${PLONE_URL}/my-vocabulary_term
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a VocabularyTerm with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the VocabularyTerm title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
