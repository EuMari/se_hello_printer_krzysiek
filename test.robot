*** Settings ***
Documentation   Testing application functionality.
Metadata        Version 1.0
Metadata        Author  kbalko

Resource        resources.robot

Library   SeleniumLibrary

Suite Teardown   Close All Browsers

*** Test Cases ***

Test 1 Succcesful Logging with valid login and password
   Go to website
   Logging with valid credentials
   Check if user is log in
   Close browser

Test 2 Fail logging attempt with valid login and invalid password
   Go to website
   Entering login: valid, taken
   Entering invalid password
   Click submit button
   Check if user is NOT log in
   Close browser

Test 3 Fail logging attempt with not registred login and valid password
   Go to website
   Entering login: valid, free
   Entering valid password
   Click submit button
   Check if user is NOT log in
   Close browser

Test 4 Fail logging attempt with no input login and password
   Go to website
   Click submit button
   Page Should Not Contain   ${logging_sucess}
   Close browser

Test 5 Fail user registration attepmt with taken login
   Go to website
   Go to registration form
   Entering login: valid, taken
   Entering email: valid, free
   Entering valid password
   Confirming password with valid password
   Click submit button
   Page Should Contain   ${login_is_taken}
   Close browser

Test 6 Fail user registration attepmt with taken email
   Go to website
   Go to registration form
   Entering login: valid, free
   Entering email: valid, taken
   Entering valid password
   Confirming password with valid password
   Click submit button
   Page Should Contain   ${email_is_taken}
   Close browser

Test 7 Fail user registration attepmt - fail confirmation password
   Go to website
   Go to registration form
   Entering login: valid, free
   Entering email: valid, free
   Entering valid password
   Confirming password with different password
   Click submit button
   Page Should Contain   ${different_pass}
   Close browser

Test 8 Check if navbar '/explore' direction works
   Go to website
   Logging with valid credentials
   Check if user is log in
   Go to /explore page
   Back to index page
   Close browser

Test 9 Check if navbar '/user/<username>' direction works
   Go to website
   Logging with valid credentials
   Check if user is log in
   Go to /user page
   Back to index page
   Close Browser

Test 10 Check if navbar 'logout' direction works
   Go to website
   Logging with valid credentials
   Check if user is log in
   Click in '/logout' direction
   Close Browser

Test 11 Check if '/edit_profile' direction and 'save' button works
   Go to website
   Logging with valid credentials
   Check if user is log in
   Go to /user page
   Go to /edit_profile page
   Click submit button
   Page Should Contain    ${save_change}
   Click button           ${back_button}
   Page Should Contain    ${user_page}
   Close Browser

Test 12 Check if 'follow'/'unfollow' button works
   Go to website
   Logging with valid credentials
   Check if user is log in
   Go to                  ${other_user_page}
   Click submit button
   Page Should Contain    ${follow}
   Click submit button
   Page Should Contain    ${unfollow}
   Close Browser

Test 13 Check if user can add post
   Go to website
   Logging with valid credentials
   Check if user is log in
   Input text in text area
   Click submit button
   Page Should Contain    ${afer_post}
   Page Should Contain    ${test_text}
