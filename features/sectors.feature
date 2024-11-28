@alten
@sectors

Feature: Sectors menu
"""
      AS a user I WANT to check the access to the Sectors section of Alten to verify the correct functionality of the section.
      """

  @sectors_01
  Scenario: Sectors - Public Administration
    Given user navigating to the website 'https://www.alten.es/'
    And user clicks on the main section of sectors
    When user clicks on the section public administration
    Then user verifies the next text 'ALTEN, experto digital para generar impacto en el sector público' in the screen public administration

  @sectors_02
  Scenario: Sectors - Aeronautic
    Given user navigating to the website 'https://www.alten.es/'
    And user clicks on the main section of sectors
    When user clicks on the section aeronautic
    Then user verifies the next text 'Descarbonizar el futuro de la aviación' in the screen aeronautic

