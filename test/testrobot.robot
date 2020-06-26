*** Settings ***
Library   SeleniumLibrary

Suite Teardown   Close All Browsers


*** Variables ***

${browser}   Firefox
${website}   http://127.0.0.1:5000

${login_valid_but_taken}    Tester2
${login_valid_free}         Newlogin
${pass_valid}               tester2
${pass_invalid}             Invalidpass
${email_valid_but_taken}    tester2@testy.pl
${email_valid_free}         someemail@bu.pl

${selector_login}           css: #username
${selector_pass}            css: #password
${selector_pass2}           css: #password2
${selector_email}           css: #email
${selector_button}          css: #submit
${back_button}              css: #back
${go_to_register}           css: #registry
${go_to_explore}            css: #explore
${go_to_index_page}         css: #index
${go_to_user_page}          css: #user
${go_to_logout}             css: #logout
${go_to_edit_profile}       css: #edit_profile


${logging_sucess}       Hej, ${login_valid_but_taken}
${logging_fail}         Nieprawidłowy login lub hasło.
${logging_requ}         Hasło wypadło Ci z głowy?
${index_page}           Co u Ciebie?
${user_page}            Ostatnio zalogowany:
${edit_profile}         O mnie
${save_change}          Zmiany zapisane
${login_is_taken}       Użyj innego loginu
${email_is_taken}       Użyj innego adresu email
${different_pass}       Field must be equal to password.

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
   Close browser

Test 10 Check if navbar 'logout' direction works
   Go to website
   Logging with valid credentials
   Check if user is log in
   Click in '/logout' direction

Test 11 Check if '/edit_profile' direction and 'save' button works
   Go to website
   Logging with valid credentials
   Check if user is log in
   Go to /user page
   Go to /edit_profile page
   Click button           ${selector_button}
   Page Should Contain    ${save_change}
   Click button           ${back_button}
   Page Should Contain    ${user_page}

*** Keywords ***

Go to website
   Open Browser   about:blank         ${BROWSER}
   Go To                              ${WEBSITE}

Logging with valid credentials
   Wait Until Element Is Visible      ${selector_login}
   Entering login: valid, taken
   Entering valid password
   Click submit button

Entering login: valid, taken
    Wait Until Element Is Visible      ${selector_login}
    Input Text     ${selector_login}   ${login_valid_but_taken}

Entering login: valid, free
    Wait Until Element Is Visible      ${selector_login}
    Input Text     ${selector_login}   ${login_valid_free}

Entering valid password
    Input Text     ${selector_pass}    ${pass_valid}

Entering invalid password
    Input Text     ${selector_pass}    ${pass_invalid}

Entering email: valid, taken
    Input Text     ${selector_email}   ${email_valid_but_taken}

Entering email: valid, free
    Input Text     ${selector_email}   ${email_valid_free}

Confirming password with valid password
    Input Text     ${selector_pass2}   ${pass_valid}

Confirming password with different password
    Input Text     ${selector_pass2}   ${pass_invalid}

Click submit button
    Wait Until Element Is Visible      ${selector_button}
    Click Button   ${selector_button}

Check if user is log in
   Page Should Contain                 ${logging_sucess}
   Page Should Not Contain             ${logging_fail}

Check if user is NOT log in
   Page Should Contain                 ${logging_fail}
   Page Should Not Contain             ${logging_sucess}

Go to registration form
   Click Link                          ${go_to_register}

Go to /explore page
   Click Link                          ${go_to_explore}
   Page Should Not Contain             ${index_page}

Go to /user page
   Click Link                          ${go_to_user_page}
   Page Should Not Contain             ${index_page}
   Page Should Contain                 ${user_page}

Go to /edit_profile page
   Click Link                          ${go_to_edit_profile}
   Page Should Contain                 ${edit_profile}

Back to index page
   Click Link                          ${go_to_index_page}
   Wait Until Element Is Visible       ${selector_button}
   Page Should Contain                 ${index_page}

Click in '/logout' direction
   Click Link                          ${go_to_logout}
   Wait Until Element Is Visible       ${selector_login}
   Page Should Contain                 ${logging_requ}

Close browser
   Close All Browsers
