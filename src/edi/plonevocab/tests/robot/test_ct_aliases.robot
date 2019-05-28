# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s edi.plonevocab -t test_aliases.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src edi.plonevocab.testing.EDI_PLONEVOCAB_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/edi/plonevocab/tests/robot/test_aliases.robot
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

Scenario: As a site administrator I can add a Aliases
  Given a logged-in site administrator
    and an add Aliases form
   When I type 'My Aliases' into the title field
    and I submit the form
   Then a Aliases with the title 'My Aliases' has been created

Scenario: As a site administrator I can view a Aliases
  Given a logged-in site administrator
    and a Aliases 'My Aliases'
   When I go to the Aliases view
   Then I can see the Aliases title 'My Aliases'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Aliases form
  Go To  ${PLONE_URL}/++add++Aliases

a Aliases 'My Aliases'
  Create content  type=Aliases  id=my-aliases  title=My Aliases

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Aliases view
  Go To  ${PLONE_URL}/my-aliases
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Aliases with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Aliases title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
