# Testing

> Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| bag | bag.html | ![screenshot](documentation/validation/w3c-bag.png) | Passed with no errors |
| checkout | checkout.html | ![screenshot](documentation/validation/w3c-checkout.png) | Passed with no errors |
| checkout | checkout_success.html | ![screenshot](documentation/validation/w3c-checkout-success.png) | Passed with no errors |
| courses | add_course.html | ![screenshot](documentation/validation/w3c-add-course-1.png) | My own code passed with no errors, but the code rendered by the summernote widget did not. (See [Bugs](#bugs) section. ) |
|  |  | ![screenshot](documentation/validation/w3c-add-course-2.png) | Summernote Errors |
|  |  | ![screenshot](documentation/validation/w3c-add-course-3.png) | Summernote Errors |
|  |  | ![screenshot](documentation/validation/w3c-add-course-4.png) | Summernote Errors |
| courses | course_detail.html | ![screenshot](documentation/validation/w3c-course-detail-1.png) | My own code passed with no errors, but the code rendered by summernote did not. (See [Bugs](#bugs) section. ) |
|  |  | ![screenshot](documentation/validation/w3c-course-detail-2.png) | Summernote Errors |
| courses | courses.html | ![screenshot](documentation/validation/w3c-courses.png) | Passed with no errors |
| courses | edit_course.html | ![screenshot](documentation/validation/w3c-edit-course-1.png) | My own code passed with no errors, but the code rendered by the summernote widget did not. (See [Bugs](#bugs) section. ) |
|  |  | ![screenshot](documentation/validation/w3c-edit-course-2.png) | Summernote Errors |
|  |  | ![screenshot](documentation/validation/w3c-edit-course-3.png) | Summernote Errors |
| home | index.html | ![screenshot](documentation/validation/w3c-index.png) | Passed with no errors |
| information | about.html | ![screenshot](documentation/validation/w3c-about-1.png) | My own code passed with no errors, but the code rendered by summernote did not. (See [Bugs](#bugs) section. ) |
|  |  | ![screenshot](documentation/validation/w3c-about-2.png) | Summernote Errors |
| information | contact_us.html | ![screenshot](documentation/validation/w3c-contact-us.png) | Passed with no errors |
| information | faq.html | ![screenshot](documentation/validation/w3c-faq.png) | Passed with no errors |
| newsletter | subscribe.html | ![screenshot](documentation/validation/w3c-newsletter.png) | Passed with no errors |
| profiles | profile.html | ![screenshot](documentation/validation/w3c-profile.png) | Passed with no errors |
| templates | 404.html | ![screenshot](documentation/validation/w3c-404.png) | Passed with no errors |
| templates | 500.html | ![screenshot](documentation/validation/w3c-500.png) | Passed with no errors |
| Allauth | signup.html | ![screenshot](documentation/validation/w3c-signup.png) | My own code passed, but the code rendered by allauth did not. This is a known bug on the signup page. (See [Bugs](#bugs) section. ) |
| Allauth | login.html | ![screenshot](documentation/validation/w3c-login.png) | Passed with no errors |
| Allauth | logout.html | ![screenshot](documentation/validation/w3c-logout.png) | Passed with no errors |
| Allauth | password_change.html | ![screenshot](documentation/validation/w3c-password-change.png) | Passed with no errors. Had one info warning regarding trailing slash on an input. This input was not my own code and was rendered by Allauth. (See [Bugs](#bugs) section.) |


### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| checkout | checkout.css | ![screenshot](documentation/validation/w3c-checkout-css.png) | Passed with no errors |
| profiles | profile.css | ![screenshot](documentation/validation/w3c-profile-css.png) | Passed with no errors |
| static | base.css | ![screenshot](documentation/validation/w3c-base-css.png) | Passed with no errors |

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| checkout | stripe_elements.js | ![screenshot](documentation/validation/jshint-stripe-elements.png) | Passed with one warning due to JSHint not recognizing the stripe function, which is defined by the Stripe JavaScript library. |
| profiles | countryfield.js | ![screenshot](documentation/validation/jshint-country-field.png) | Passed with no errors |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| bag | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/neon-beats-academy/main/bag/admin.py) | ![screenshot](documentation/validation/pep8-bag-admin.png) | Passed with no errors |
| bag | contexts.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/neon-beats-academy/main/bag/contexts.py) | ![screenshot](documentation/validation/pep8-bag-contexts.png) | Passed with no errors |
| bag | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/neon-beats-academy/main/bag/models.py) | ![screenshot](documentation/validation/pep8-bag-models.png) | Passed with no errors |
| bag | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/neon-beats-academy/main/bag/urls.py) | ![screenshot](documentation/validation/pep8-bag-urls.png) | Passed with no errors |
| bag | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/neon-beats-academy/main/bag/views.py) | ![screenshot](documentation/validation/pep8-bag-views.png) | Passed with no errors |
| checkout | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/neon-beats-academy/main/checkout/admin.py) | ![screenshot](documentation/validation/pep8-checkout-admin.png) | Passed with no errors |
| checkout | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/neon-beats-academy/main/checkout/forms.py) | ![screenshot](documentation/validation/pep8-checkout-forms.png) | Passed with no errors |
| checkout | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/neon-beats-academy/main/checkout/models.py) | ![screenshot](documentation/validation/pep8-checkout-models.png) | Passed with no errors |
| checkout | signals.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/neon-beats-academy/main/checkout/signals.py) | ![screenshot](documentation/validation/pep8-checkout-signals.png) | Passed with no errors |
| checkout | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/neon-beats-academy/main/checkout/urls.py) | ![screenshot](documentation/validation/pep8-checkout-urls.png) | Passed with no errors |
| checkout | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/neon-beats-academy/main/checkout/views.py) | ![screenshot](documentation/validation/pep8-checkout-views.png) | Passed with no errors |
| courses | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/neon-beats-academy/main/courses/admin.py) | ![screenshot](documentation/validation/pep8-courses-admin.png) | Passed with no errors |
| courses | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/neon-beats-academy/main/courses/forms.py) | ![screenshot](documentation/validation/pep8-courses-forms.png) | Passed with no errors |
| courses | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/neon-beats-academy/main/courses/models.py) | ![screenshot](documentation/validation/pep8-courses-models.png) | Passed with no errors |
| courses | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/neon-beats-academy/main/courses/urls.py) | ![screenshot](documentation/validation/pep8-courses-urls.png) | Passed with no errors |
| courses | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/neon-beats-academy/main/courses/views.py) | ![screenshot](documentation/validation/pep8-courses-views.png) | Passed with no errors |
| courses | widgets.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/neon-beats-academy/main/courses/widgets.py) | ![screenshot](documentation/validation/pep8-courses-widgets.png) | Passed with no errors |
| home | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/neon-beats-academy/main/home/admin.py) | ![screenshot](documentation/validation/pep8-home-admin.png) | Passed with no errors |
| home | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/neon-beats-academy/main/home/models.py) | ![screenshot](documentation/validation/pep8-home-models.png) | Passed with no errors |
| home | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/neon-beats-academy/main/home/urls.py) | ![screenshot](documentation/validation/pep8-home-urls.png) | Passed with no errors |
| home | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/neon-beats-academy/main/home/views.py) | ![screenshot](documentation/validation/pep8-home-views.png) | Passed with no errors |
| information | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/neon-beats-academy/main/information/admin.py) | ![screenshot](documentation/validation/pep8-info-admin.png) | Passed with no errors |
| information | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/neon-beats-academy/main/information/forms.py) | ![screenshot](documentation/validation/pep8-info-forms.png) | Passed with no errors |
| information | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/neon-beats-academy/main/information/models.py) | ![screenshot](documentation/validation/pep8-info-models.png) | Passed with no errors |
| information | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/neon-beats-academy/main/information/urls.py) | ![screenshot](documentation/validation/pep8-info-urls.png) | Passed with no errors |
| information | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/neon-beats-academy/main/information/views.py) | ![screenshot](documentation/validation/pep8-info-views.png) | Passed with no errors |
|  | manage.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/neon-beats-academy/main/manage.py) | ![screenshot](documentation/validation/pep8-manage.png) | Passed with no errors |
| neon_beats | settings.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/neon-beats-academy/main/neon_beats/settings.py) | ![screenshot](documentation/validation/pep8-neon-settings.png) | Passed with no errors |
| neon_beats | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/neon-beats-academy/main/neon_beats/urls.py) | ![screenshot](documentation/validation/pep8-neon-urls.png) | Passed with no errors |
| neon_beats | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/neon-beats-academy/main/neon_beats/views.py) | ![screenshot](documentation/validation/pep8-neon-views.png) | Passed with no errors |
| newsletter | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/neon-beats-academy/main/newsletter/admin.py) | ![screenshot](documentation/validation/pep8-newsletter-admin.png) | Passed with no errors |
| newsletter | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/neon-beats-academy/main/newsletter/forms.py) | ![screenshot](documentation/validation/pep8-newsletter-forms.png) | Passed with no errors |
| newsletter | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/neon-beats-academy/main/newsletter/models.py) | ![screenshot](documentation/validation/pep8-newsletter-models.png) | Passed with no errors |
| newsletter | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/neon-beats-academy/main/newsletter/urls.py) | ![screenshot](documentation/validation/pep8-newsletter-urls.png) | Passed with no errors |
| newsletter | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/neon-beats-academy/main/newsletter/views.py) | ![screenshot](documentation/validation/pep8-newsletter-views.png) | Passed with no errors |
| profiles | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/neon-beats-academy/main/profiles/admin.py) | ![screenshot](documentation/validation/pep8-profiles-admin.png) | Passed with no errors |
| profiles | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/neon-beats-academy/main/profiles/forms.py) | ![screenshot](documentation/validation/pep8-profiles-forms.png) | Passed with no errors |
| profiles | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/neon-beats-academy/main/profiles/models.py) | ![screenshot](documentation/validation/pep8-profiles-models.png) | Passed with no errors |
| profiles | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/neon-beats-academy/main/profiles/urls.py) | ![screenshot](documentation/validation/pep8-profiles-urls.png) | Passed with no errors |
| profiles | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/neon-beats-academy/main/profiles/views.py) | ![screenshot](documentation/validation/pep8-profiles-views.png) | Passed with no errors |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Home | About | Contact | Courses | Notes |
| --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/browsers/browser-chrome-home.png) | ![screenshot](documentation/browsers/browser-chrome-about.png) | ![screenshot](documentation/browsers/browser-chrome-contact.png) | ![screenshot](documentation/browsers/browser-chrome-courses.png) | Works as expected |
| Firefox | ![screenshot](documentation/browsers/browser-firefox-home.png) | ![screenshot](documentation/browsers/browser-firefox-about.png) | ![screenshot](documentation/browsers/browser-firefox-contact.png) | ![screenshot](documentation/browsers/browser-firefox-courses.png) | Works as expected |
| Edge | ![screenshot](documentation/browsers/browser-edge-home.png) | ![screenshot](documentation/browsers/browser-edge-about.png) | ![screenshot](documentation/browsers/browser-edge-contact.png) | ![screenshot](documentation/browsers/browser-edge-courses.png) | Works as expected |
| Safari | ![screenshot](documentation/browsers/browser-safari-home.png) | ![screenshot](documentation/browsers/browser-safari-about.png) | ![screenshot](documentation/browsers/browser-safari-contact.png) | ![screenshot](documentation/browsers/browser-safari-courses.png) | Works as expected |
| Opera | ![screenshot](documentation/browsers/browser-opera-home.png) | ![screenshot](documentation/browsers/browser-opera-about.png) | ![screenshot](documentation/browsers/browser-opera-contact.png) | ![screenshot](documentation/browsers/browser-opera-courses.png) | Works as expected |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Home | About | Contact | Courses | Notes | 
| --- | --- | --- | --- | --- | --- | 
| MacBook Pro (Real Device Test) | ![screenshot](documentation/responsiveness/responsive-macbook-pro-home.png) | ![screenshot](documentation/responsiveness/responsive-macbook-pro-about.png) | ![screenshot](documentation/responsiveness/responsive-macbook-pro-contact.png) | ![screenshot](documentation/responsiveness/responsive-macbook-pro-courses.png) | Works as expected |
| Desktop XL | ![screenshot](documentation/responsiveness/responsive-desktop-xl-home.png) | ![screenshot](documentation/responsiveness/responsive-desktop-xl-about.png) | ![screenshot](documentation/responsiveness/responsive-desktop-xl-contact.png) | ![screenshot](documentation/responsiveness/responsive-desktop-xl-courses.png) |  Works as expected |
| iPhone 15 Pro Max (Real Device Test) | ![screenshot](documentation/responsiveness/responsive-iphone-15-pro-max-home.png) | ![screenshot](documentation/responsiveness/responsive-iphone-15-pro-max-about.png) | ![screenshot](documentation/responsiveness/responsive-iphone-15-pro-max-contact.png) | ![screenshot](documentation/responsiveness/responsive-iphone-15-pro-max-courses.png) | Works as expected |
| iPhone SE | ![screenshot](documentation/responsiveness/responsive-iphone-se-home.png) | ![screenshot](documentation/responsiveness/responsive-iphone-se-about.png) | ![screenshot](documentation/responsiveness/responsive-iphone-se-contact.png) | ![screenshot](documentation/responsiveness/responsive-iphone-se-courses.png) | Works as expected | 
| iPhone 16 | ![screenshot](documentation/responsiveness/responsive-iphone-16-home.png) | ![screenshot](documentation/responsiveness/responsive-iphone-16-about.png) | ![screenshot](documentation/responsiveness/responsive-iphone-16-contact.png) | ![screenshot](documentation/responsiveness/responsive-iphone-16-courses.png) | Works as expected |    
| iPad Mini | ![screenshot](documentation/responsiveness/responsive-ipad-mini-home.png) | ![screenshot](documentation/responsiveness/responsive-ipad-mini-about.png) | ![screenshot](documentation/responsiveness/responsive-ipad-mini-contact.png) | ![screenshot](documentation/responsiveness/responsive-ipad-mini-courses.png) | Works as expected |  
| iPad Air | ![screenshot](documentation/responsiveness/responsive-ipad-air-home.png) | ![screenshot](documentation/responsiveness/responsive-ipad-air-about.png) | ![screenshot](documentation/responsiveness/responsive-ipad-air-contact.png) | ![screenshot](documentation/responsiveness/responsive-ipad-air-courses.png) | Works as expected |  
| Galaxy Tab | ![screenshot](documentation/responsiveness/responsive-galaxy-tab-home.png) | ![screenshot](documentation/responsiveness/responsive-galaxy-tab-about.png) | ![screenshot](documentation/responsiveness/responsive-galaxy-tab-contact.png) | ![screenshot](documentation/responsiveness/responsive-galaxy-tab-courses.png) | Works as expected |
| Galaxy S24 Ultra | ![screenshot](documentation/responsiveness/responsive-galaxy-s24-ultra-home.png) | ![screenshot](documentation/responsiveness/responsive-galaxy-s24-ultra-about.png) | ![screenshot](documentation/responsiveness/responsive-galaxy-s24-ultra-contact.png) | ![screenshot](documentation/responsiveness/responsive-galaxy-s24-ultra-courses.png) | Works as expected | 


## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/lighthouse/lighthouse-mobile-home.png) | ![screenshot](documentation/lighthouse/lighthouse-desktop-home.png) |  |
| Courses | ![screenshot](documentation/lighthouse/lighthouse-mobile-courses.png) | ![screenshot](documentation/lighthouse/lighthouse-desktop-courses.png) |  |
| Course detail | ![screenshot](documentation/lighthouse/lighthouse-mobile-course-detail.png) | ![screenshot](documentation/lighthouse/lighthouse-desktop-course-detail.png) |  |
| Add course | ![screenshot](documentation/lighthouse/lighthouse-mobile-add-course.png) | ![screenshot](documentation/lighthouse/lighthouse-desktop-add-course.png) |  |
| Edit course | ![screenshot](documentation/lighthouse/lighthouse-mobile-edit-course.png) | ![screenshot](documentation/lighthouse/lighthouse-desktop-edit-course.png) |  |
| Bag | ![screenshot](documentation/lighthouse/lighthouse-mobile-bag.png) | ![screenshot](documentation/lighthouse/lighthouse-desktop-bag.png) |  |
| Checkout | ![screenshot](documentation/lighthouse/lighthouse-mobile-checkout.png) | ![screenshot](documentation/lighthouse/lighthouse-desktop-checkout.png) |  |
| Checkout Success | ![screenshot](documentation/lighthouse/lighthouse-mobile-checkout-success.png) | ![screenshot](documentation/lighthouse/lighthouse-desktop-checkout-success.png) |  |
| Profile | ![screenshot](documentation/lighthouse/lighthouse-mobile-profile.png) | ![screenshot](documentation/lighthouse/lighthouse-desktop-profile.png) |  |
| About | ![screenshot](documentation/lighthouse/lighthouse-mobile-about.png) | ![screenshot](documentation/lighthouse/lighthouse-desktop-about.png) |  |
| Contact | ![screenshot](documentation/lighthouse/lighthouse-mobile-contact.png) | ![screenshot](documentation/lighthouse/lighthouse-desktop-contact.png) |  |
| Faq | ![screenshot](documentation/lighthouse/lighthouse-mobile-faq.png) | ![screenshot](documentation/lighthouse/lighthouse-desktop-faq.png) |  |
| Newsletter | ![screenshot](documentation/lighthouse/lighthouse-mobile-newsletter.png) | ![screenshot](documentation/lighthouse/lighthouse-desktop-newsletter.png) |  |
| Signup | ![screenshot](documentation/lighthouse/lighthouse-mobile-signup.png) | ![screenshot](documentation/lighthouse/lighthouse-desktop-signup.png) |  |
| Login | ![screenshot](documentation/lighthouse/lighthouse-mobile-login.png) | ![screenshot](documentation/lighthouse/lighthouse-desktop-login.png) |  |
| Logout | ![screenshot](documentation/lighthouse/lighthouse-mobile-logout.png) | ![screenshot](documentation/lighthouse/lighthouse-desktop-logout.png) |  |
| Change password | ![screenshot](documentation/lighthouse/lighthouse-mobile-change-password.png) | ![screenshot](documentation/lighthouse/lighthouse-desktop-change-password.png) |  |


## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | User Action | Expected Result | Screenshot | Pass/Fail |
| --- | --- | --- | --- | --- |
| Bag | | | | |
| | Add duplicate item to bag | Unable to add | ![screenshot](documentation/defensive/defence-bag-duplicate.png) | Pass |
| Logged In As Superuser | | | | |
| | Delete course on detail page | Delete modal appears to check I am sure | ![screenshot](documentation/defensive/defence-logged-in-course-detail-delete.png) | Pass |
| | Delete course on courses page | Delete modal appears to check I am sure | ![screenshot](documentation/defensive/defence-logged-in-courses-delete.png) | Pass |
| | Click account button | Superuser options appear | ![screenshot](documentation/defensive/defence-logged-in-account-dropdown.png) | Pass |
| | Head to course detail page | Edit/delete buttons present | ![screenshot](documentation/defensive/defence-logged-in-course-detail-buttons.png) | Pass |
| | Head to courses page | Edit/delete buttons present | ![screenshot](documentation/defensive/defence-logged-in-courses-buttons.png) | Pass |
| | Click product management | Add course page access | ![screenshot](documentation/defensive/defence-logged-in-course-add.png) | Pass |
| | Click edit course button | Edit course page access | ![screenshot](documentation/defensive/defence-logged-in-course-edit.png) | Pass |
| Logged In | | | | |
| | Click account button | Logged in options appear | ![screenshot](documentation/defensive/defence-logged-in-non-super-account-dropdown.png) | Pass |
| | Head to courses page | Edit/delete buttons not present | ![screenshot](documentation/defensive/defence-logged-in-non-super-courses-buttons.png) | Pass |
| | Head to course detail page | Edit/delete buttons not present | ![screenshot](documentation/defensive/defence-logged-in-non-super-course-detail-buttons.png) | Pass |
| | Attepmpt to access add course via url | Not authorised message apears | ![screenshot](documentation/defensive/defence-logged-in-non-super-url-course-add.png) | Pass |
| | Attempt to access edit course via url | Not authorised message apears | ![screenshot](documentation/defensive/defence-logged-in-non-super-url-course-edit.png) | Pass |
| Account | | | | |
| | Click account button | Logged out options appear | ![screenshot](documentation/defensive/defence-logged-out-account-dropdown.png) | Pass |
| | Try to login without verifying email | Verify page appears | ![screenshot](documentation/defensive/defence-logged-out-login-without-verify.png) | Pass |
| | Don't provide signup email | Error message appears | ![screenshot](documentation/defensive/defence-account-signup-email.png) | Pass |
| | Sign in with email that already has an account | Warning email sent to email | ![screenshot](documentation/defensive/defence-account-signup-duplicate-email.png) | Pass |
| | Enter invalid/blank password | Error message appears | ![screenshot](documentation/defensive/defence-account-password-errors.png) | Pass |
| | Input different passwords | Error message appears | ![screenshot](documentation/defensive/defence-account-password-mismatch.png) | Pass |
| | Input password similar to username (or the same) | Error message appears | ![screenshot](documentation/defensive/defence-account-password-similar.png) | Pass |
| Add | | | | |
| | Enter invalid/blank name | Error message appears | ![screenshot](documentation/defensive/defence-add-name.png) | Pass |
| | Enter invalid/blank difficulty | Error message appears | ![screenshot](documentation/defensive/defence-add-difficulty.png) | Pass |
| | Enter invalid/blank price | Error message appears | ![screenshot](documentation/defensive/defence-add-price.png) | Pass |
| | Enter invalid/blank letter | Error message appears | ![screenshot](documentation/defensive/defence-add-price-number.png) | Pass |
| | Enter invalid/blank description | Error message appears | ![screenshot](documentation/defensive/defence-add-description.png) | Pass |
| Message | | | | |
| | Try to add invalid course | Error message appears | ![screenshot](documentation/defensive/defence-message-add-invalid.png) | Pass |
| | Remove course from bag | Success message appears | ![screenshot](documentation/defensive/defence-message-bag-remove.png) | Pass |
| | Add item to bag | Success message appears and item visibly in bag | ![screenshot](documentation/defensive/defence-message-bag-add.png) | Pass |
| | Update course details | Success message appears | ![screenshot](documentation/defensive/defence-message-edit-updated.png) | Pass |
| | Edit a page | Alert message appears to inform you that you are editing | ![screenshot](documentation/defensive/defence-message-editing.png) | Pass |
| | Delete a course | Success message appears | ![screenshot](documentation/defensive/defence-message-delete-success.png) | Pass |
| | Add a course | Success message appears | ![screenshot](documentation/defensive/defence-message-add-success.png) | Pass |
| | Place an order | Success message appears | ![screenshot](documentation/defensive/defence-message-order-success.png) | Pass |
| Checkout | | | | |
| | Click checkout | Overlay appears to show my order is being processed | ![screenshot](documentation/defensive/defence-checkout-overlay.png) | Pass |
| | Place an order | Confirmation page appears | ![screenshot](documentation/defensive/defence-checkout-redirect.png) | Pass |
| | Enter expiration date in the past | Error message appears | ![screenshot](documentation/defensive/defence-checkout-card-expiration.png) | Pass |
| | Enter invalid card number | Error message appears | ![screenshot](documentation/defensive/defence-checkout-card-invalid.png) | Pass |
| | Enter blank card number | Error message appears | ![screenshot](documentation/defensive/defence-checkout-card-blank.png) | Pass |
| | Enter invalid/blank name | Error message appears | ![screenshot](documentation/defensive/defence-checkout-name.png) | Pass |
| | Enter invalid/blank email | Enter invalid/blank | ![screenshot](documentation/defensive/defence-checkout-email.png) | Pass |
| | Enter invalid/blank country | Error message appears | ![screenshot](documentation/defensive/defence-checkout-country.png) | Pass |
| | Enter invalid/blank town | Error message appears | ![screenshot](documentation/defensive/defence-checkout-town.png) | Pass |
| | Enter invalid/blank address | Error message appears | ![screenshot](documentation/defensive/defence-checkout-address.png) | Pass |
| | Enter invalid/blank postcode | Error message appears | ![screenshot](documentation/defensive/defence-checkout-card-post-code.png) | Pass |
| | Enter invalid/blank phone number | Error message appears | ![screenshot](documentation/defensive/defence-checkout-number.png) | Pass |
| Newsletter | | | | |
| | Enter invalid email | Error message appears | ![screenshot](documentation/defensive/defence-newsletter-email-valid.png) | Pass |
| | Enter blank email | Error message appears | ![screenshot](documentation/defensive/defence-newsletter-email-blank.png) | Pass |
| | Enter email address that is already subscribed | Error message appears | ![screenshot](documentation/defensive/defence-newsletter-email-duplicate.png) | Pass |
| | Click subscribe button | Success message appears | ![screenshot](documentation/defensive/defence-newsletter-message-subscribe.png) | Pass |
| Contact | | | | |
| | Click send message | Success message appears | ![screenshot](documentation/defensive/defence-contact-message-success.png) | Pass |
| | Enter invalid/blank message | Error message appears | ![screenshot](documentation/defensive/defence-contact-message.png) | Pass |
| | Enter invalid/blank email | Error message appears | ![screenshot](documentation/defensive/defence-contact-email.png) | Pass |
| | Enter invalid/blank name | Error message appears | ![screenshot](documentation/defensive/defence-contact-name.png) | Pass |
| Profile | | | | |
| | Click update profiel button | Success message appears | ![screenshot](documentation/defensive/defence-profile-message-updated.png) | Pass |


## User Story Testing

### Site User

| User Story | Criteria | Screenshot |
| --- | --- | --- |
| As a site user I can easily view products so that I can choose which ones to buy | | |
| | A clear link to all products will be featured on the home page | ![screenshot](documentation/user-stories/.png) |
| | A link to courses will be featured in the nav bar | ![screenshot](documentation/user-stories/.png) |
| As a site user I can see further details of a product so that I can decide if it is the right product for me | | |
| | When the user clicks on a product they will be directed to a product details page showing further details of the product | ![screenshot](documentation/user-stories/.png) |
| As a site user I can leave comments on a product so that I can ask the site owner a question or tell others what I thought of it | | |
| | Feature a comment section on the product detail page for logged in users | ![screenshot](documentation/user-stories/.png) |
| As a site user I can find information about the site so that I can understand what services the site offers | | |
| | Have an about page | ![screenshot](documentation/user-stories/.png) |
| | Have easily accessible information about the site displayed | ![screenshot](documentation/user-stories/.png) |
| As a site user I would like to contact the site owner so that they can answer any queries I have | | |
| | Contact us page created | ![screenshot](documentation/user-stories/.png) |
| | Form present to directly contact the site owner | ![screenshot](documentation/user-stories/.png) |
| As a site user I can add items to my basket so that they are saved while I continue shopping | | |
| | Have a basket available for users | ![screenshot](documentation/user-stories/.png) |
| | Have a button for adding the product to the basket on the product detail page | ![screenshot](documentation/user-stories/.png) |
| | Have a page for the basket | ![screenshot](documentation/user-stories/.png) |
| | Have a remove button to remove item from the basket | ![screenshot](documentation/user-stories/.png) |
| | User can clearly see the total before checkout | ![screenshot](documentation/user-stories/.png) |
| As a site user I can create an account and login so that I can have a personal account and order items | | |
| | For logged out users, create account and login links featured in the account drop-down of the navigation bar | ![screenshot](documentation/user-stories/.png) |
| | For logged in users, a logout link featured in the account drop-down of the navigation bar | ![screenshot](documentation/user-stories/.png) |
| As a site user I can securely enter my credit card details so that I can securely purchase a product | | |
| | Use Stripe for secure checkout | ![screenshot](documentation/user-stories/.png) |
| | Have a checkout page | ![screenshot](documentation/user-stories/.png) |
| As a site user I can view my order confirmation so I can make sure that I have not made any mistakes | | |
| | Order confirmation page displayed after order is processed | ![screenshot](documentation/user-stories/.png) |
| As a site user I would like to receive an order confirmation email of what I’ve ordered so that I can have a record of the order | | |
| | Users receive an email confirming their order when it has been processed | ![screenshot](documentation/user-stories/.png) |
| As a site user I can receive email confirmation after registering so that I can know my account was successfully created | | |
| | Email confirmation sent after account is created with verification link | ![screenshot](documentation/user-stories/.png) |
| As a site user I can search for products throughout the site so that I can find a specific product easily | | |
| | Have a search bar featured on every page | ![screenshot](documentation/user-stories/.png) |
| | Have a page that shows returned search results | ![screenshot](documentation/user-stories/.png) |
| As a site user I can view specific tiers of courses so that I can easily find courses suitable to my skill level | | |
| | Courses sorted into different tiers | ![screenshot](documentation/user-stories/.png) |
| | Course tiers easily accessible via navigation bar dropdown menu | ![screenshot](documentation/user-stories/.png) |
| | Courses split into tiers on all courses page | ![screenshot](documentation/user-stories/.png) |
| As a site user I can read frequently asked questions from other users so that I can find potential answers to my questions with ease | | |
| | FAQ section available for all users | ![screenshot](documentation/user-stories/.png) |
| As a site user I can easily navigate back to the main site if an error message appears so that I can continue shopping | | |
| | Custom 404 error page | ![screenshot](documentation/user-stories/.png) |
| | Custom 500 error page | ![screenshot](documentation/user-stories/.png) |
| As a site user I can subscribe to a newsletter so that I can stay up to date with new courses | | |
| | Newsletter page featured | ![screenshot](documentation/user-stories/.png) |
| | Easy subscribe method | ![screenshot](documentation/user-stories/.png) |
| | Information about the benefits of signing up to a newsletter | ![screenshot](documentation/user-stories/.png) |

### Returning Site User

| User Story | Criteria | Sreenshot |
| --- | --- | --- |
| As a returning site user I can change password so that I can keep my account up to date | | |
| | For logged in users a change password link will be available from the account dropdown | ![screenshot](documentation/user-stories/.png) |
| As a site user when logged I can have a user profile so that I can change my details | | | | | |
| | Form for logged in users to add/change their details | ![screenshot](documentation/user-stories/.png) |
| As a site user when logged in I can view my order history so that I can see what I have ordered | | | | | |
| | Order history section available for logged in users | ![screenshot](documentation/user-stories/.png) |

### Site Owner

| User Story | Criteria | Screenshot |
| --- | --- | --- |
| As a site owner I can add products to the site so that I can give my customers access to new products | | |
| | Have an add product form only available to superusers | ![screenshot](documentation/user-stories/.png) |
| | Enable superusers to upload an image of the product | ![screenshot](documentation/user-stories/.png) |
| As a site owner I can edit a product so that I can keep the details up to date or adjust the price | | |
| | When logged in, a superuser can edit any details of a product using an edit product form that is only accessible by superusers | ![screenshot](documentation/user-stories/.png) |
| | Have an edit product button on the product detail page that is only visible to site owners | ![screenshot](documentation/user-stories/.png) |
| As a site owner I can delete a product so that I can remove items that are no longer available | | |
| | Have a delete button on the product detail page that is only visible to superusers | ![screenshot](documentation/user-stories/.png) |
| | Have a warning box to make sure the superuser definitely wants to delete the product | ![screenshot](documentation/user-stories/.png) |
| | Make deleting a product only available to superusers | ![screenshot](documentation/user-stories/.png) |
| As a site owner I can log in to the admin panel so that I can view orders | | |
| | Admin panel featured | ![screenshot](documentation/user-stories/.png) |
| | Orders section featured in the admin panel | ![screenshot](documentation/user-stories/.png) |
| As a site owner I can log in to the admin panel so that I can check messages from site users | | |
| | Admin panel featured | ![screenshot](documentation/user-stories/.png) |
| | Contact section featured in admin panel | ![screenshot](documentation/user-stories/.png) |
| As a site owner I can change the about text so that I can keep users updated with any relevant information | | |
| | The site owner can update the about text from the admin panel | ![screenshot](documentation/user-stories/.png) |
| As a site owner I can manage products in the admin panel so that I have full control of them in one place | | |
| | Superusers able to add products in the admin panel | ![screenshot](documentation/user-stories/.png) |
| | Superusers able to edit products in the admin panel | ![screenshot](documentation/user-stories/.png) |
| | Superusers able to delete products in the admin panel | ![screenshot](documentation/user-stories/.png) |


