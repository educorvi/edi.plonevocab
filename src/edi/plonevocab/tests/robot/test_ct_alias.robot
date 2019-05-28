# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s edi.plonevocab -t test_alias.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src edi.plonevocab.testing.EDI_PLONEVOCAB_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/edi/plonevocab/tests/robot/test_alias.robot
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

Scenario: As a site administrator I can add a Alias
  Given a logged-in site administrator
    and an add Aliases form
   When I type 'My Alias' into the title field
    and I submit the form
   Then a Alias with the title 'My Alias' has been created

Scenario: As a site administrator I can view a Alias
  Given a logged-in site administrator
    and a Alias 'My Alias'
   When I go to the Alias view
   Then I can see the Alias title 'My Alias'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Aliases form
  Go To  ${PLONE_URL}/++add++Aliases

a Alias 'My Alias'
  Create content  type=Aliases  id=my-alias  title=My Alias

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Alias view
  Go To  ${PLONE_URL}/my-alias
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Alias with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Alias title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
