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
| courses | add_course.html | ![screenshot](documentation/validation/w3c-add-course-1.png) | My own code passed, but the code rendered by the summernote widget did not. |
|  |  | ![screenshot](documentation/validation/w3c-add-course-2.png) | |
|  |  | ![screenshot](documentation/validation/w3c-add-course-3.png) | |
|  |  | ![screenshot](documentation/validation/w3c-add-course-4.png) | |
| courses | course_detail.html | ![screenshot](documentation/validation/w3c-course-detail-1.png) | My own code passed, but the code rendered by summernote did not. |
|  |  | ![screenshot](documentation/validation/w3c-course-detail-2.png) | |
| courses | courses.html | ![screenshot](documentation/validation/w3c-courses.png) | Passed with no errors |
| courses | edit_course.html | ![screenshot](documentation/validation/w3c-edit-course-1.png) | My own code passed, but the code rendered by the summernote widget did not. |
|  |  | ![screenshot](documentation/validation/w3c-edit-course-2.png) | |
|  |  | ![screenshot](documentation/validation/w3c-edit-course-3.png) | |
| home | index.html | ![screenshot](documentation/validation/w3c-index.png) | Passed with no errors |
| information | about.html | ![screenshot](documentation/validation/w3c-about-1.png) | My own code passed, but the code rendered by summernote did not. |
|  |  | ![screenshot](documentation/validation/w3c-about-2.png) | |
| information | contact_us.html | ![screenshot](documentation/validation/w3c-contact-us.png) | Passed with no errors |
| information | faq.html | ![screenshot](documentation/validation/w3c-faq.png) | Passed with no errors |
| newsletter | subscribe.html | ![screenshot](documentation/validation/w3c-newsletter.png) | Passed with no errors |
| profiles | profile.html | ![screenshot](documentation/validation/w3c-profile.png) | Passed with no errors |
| templates | 404.html | ![screenshot](documentation/validation/w3c-404.png) | Passed with no errors |
| templates | 500.html | ![screenshot](documentation/validation/w3c-500.png) | Passed with no errors |
| Allauth | signup.html | ![screenshot](documentation/validation/w3c-signup.png) | My own code passed, but the code rendered by allauth did not. This is a known bug on the signup page. |
| Allauth | login.html | ![screenshot](documentation/validation/w3c-login.png) | Passed with no errors |
| Allauth | logout.html | ![screenshot](documentation/validation/w3c-logout.png) | Passed with no errors |
| Allauth | password_change.html | ![screenshot](documentation/validation/w3c-password-change.png) | Passed with no errors |


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

