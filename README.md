# API_Testing_Python_Behave_Allure
I am using MAC , following instructions might be helpful for mac

### Install Python first: ###
1.Run `brew install python3` <br>
2. To check if python is successfully install, use `python --version` <br>
3. (Latest stable version preferred.) <br>

### To install PIP ###
1.Run `brew install pip` <br>
2. check version by running `pip --version` <br>


### Install behave ###
1.Run `pip install behave` <br>
2. check version by running `behave --version` <br>

### for reporting, Install allure ###
1.`brew install allure` <br>
2. check version by running `allure --version` <br>


### To run your tests with behave ###
`behave -f allure  -o reports -f pretty --define env=prod` <br> 

### For reports ###
`allure serve reports`  <br>      

### OR ### 
We can also use `pip install requirements.txt`
