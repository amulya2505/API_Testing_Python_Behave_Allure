# API_Testing_Python_Behave_Allure

I am using MAC , following instructions might be helpful for mac

Install Python first
brew install python3

(Latest stable version preferred.)

To install PIP  --
brew install pip


Install behave --
pip install behave


brew install allure


To run with behave --
behave -f allure  -o reports -f pretty --define env=prod 

For reports
allure serve reports        
