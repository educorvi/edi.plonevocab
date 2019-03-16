# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s edi.plonevocab -t test_dictionary_key.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src edi.plonevocab.testing.EDI_PLONEVOCAB_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/edi/plonevocab/tests/robot/test_dictionary_key.robot
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

Scenario: As a site administrator I can add a DictionaryKey
  Given a logged-in site administrator
    and an add MenuDictionary form
   When I type 'My DictionaryKey' into the title field
    and I submit the form
   Then a DictionaryKey with the title 'My DictionaryKey' has been created

Scenario: As a site administrator I can view a DictionaryKey
  Given a logged-in site administrator
    and a DictionaryKey 'My DictionaryKey'
   When I go to the DictionaryKey view
   Then I can see the DictionaryKey title 'My DictionaryKey'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add MenuDictionary form
  Go To  ${PLONE_URL}/++add++MenuDictionary

a DictionaryKey 'My DictionaryKey'
  Create content  type=MenuDictionary  id=my-dictionary_key  title=My DictionaryKey

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the DictionaryKey view
  Go To  ${PLONE_URL}/my-dictionary_key
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a DictionaryKey with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the DictionaryKey title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
