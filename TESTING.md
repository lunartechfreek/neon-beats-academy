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

