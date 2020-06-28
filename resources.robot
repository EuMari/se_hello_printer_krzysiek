*** Settings ***
Documentation   Resource file with keywords and variables

Library		SeleniumLibrary

*** Variables ***

${browser}                  Firefox
${website}                  http://dry-brushlands-36461.herokuapp.com/
${other_user_page}          http://dry-brushlands-36461.herokuapp.com/user/Tester4

${login_valid_but_taken}    Tester2
${login_valid_free}         Newlogin
${pass_valid}               tester2
${pass_invalid}             Invalidpass
${email_valid_but_taken}    tester2@testy.pl
${email_valid_free}         someemail@bu.pl
${test_text}                Post dodany automatycznie - Robot Framework v2

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
${post_area}                css: #post



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
${unfollow}             Nie obserwujesz użytkownika Tester4.
${follow}               Obserwujesz użytkownika Tester4
${afer_post}            Twój post został opublikowany.

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

Input text in text area
   Input Text         ${post_area}     ${test_text}
