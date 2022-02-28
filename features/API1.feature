Feature: Test the API with all combinations

  Scenario Outline: POST API request 
      When user sets the url for <param>
      And set the body in with "params2"
      Then should see a valid response <param>
      Examples:
          |param|
            |en |
      
