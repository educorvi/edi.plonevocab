# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s edi.plonevocab -t test_menu_dictionary.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src edi.plonevocab.testing.EDI_PLONEVOCAB_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/edi/plonevocab/tests/robot/test_menu_dictionary.robot
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

Scenario: As a site administrator I can add a MenuDictionary
  Given a logged-in site administrator
    and an add MenuDictionary form
   When I type 'My MenuDictionary' into the title field
    and I submit the form
   Then a MenuDictionary with the title 'My MenuDictionary' has been created

Scenario: As a site administrator I can view a MenuDictionary
  Given a logged-in site administrator
    and a MenuDictionary 'My MenuDictionary'
   When I go to the MenuDictionary view
   Then I can see the MenuDictionary title 'My MenuDictionary'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add MenuDictionary form
  Go To  ${PLONE_URL}/++add++MenuDictionary

a MenuDictionary 'My MenuDictionary'
  Create content  type=MenuDictionary  id=my-menu_dictionary  title=My MenuDictionary

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the MenuDictionary view
  Go To  ${PLONE_URL}/my-menu_dictionary
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a MenuDictionary with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the MenuDictionary title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
