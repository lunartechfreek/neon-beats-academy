# [NeonBeats Academy](https://neon-beats-academy-74fa20163bce.herokuapp.com)

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/lunartechfreek/neon-beats-academy)](https://github.com/lunartechfreek/neon-beats-academy/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/lunartechfreek/neon-beats-academy)](https://github.com/lunartechfreek/neon-beats-academy/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/lunartechfreek/neon-beats-academy)](https://github.com/lunartechfreek/neon-beats-academy)

![screenshot](documentation/mockup.png)

Source: [amiresponsive](https://ui.dev/amiresponsive?url=https://neon-beats-academy-74fa20163bce.herokuapp.com)

NeonBeats is a website made for educational purposes for my fifth project portfolio in software development that I am studying with the Code Institute. The website is an e-commerce store aimed at users who are looking into learning how to DJ and want to buy a course. While designing this website I took into account the real world demands that users would have for a real e-commerce website. To adhere to these demands I created a dynamic store that creates pages for when a new course is added, lets store owners add, edit and delete courses, and also control other page content such as about, newsletter, and FAQ’s. 

The website features a bag, fully functional checkout system, newsletter and allows users to save their details through the use of user profile. The website gives live feedback messages and statements to guide users and make their shopping experience a simple and pleasant one. Finally the site sends real emails to users for when they purchase a course, signup to our newsletter, and make an account. The website is fully responsive no matter what device it is used on. 

I have applied the technologies I have learnt so far and used HTML5, CSS3, Javascript, and Django to create the website. Other technologies used are listed in the technologies used section further down the page.

## UX

### The 5 Planes of UX

#### 1. Strategy Plane
##### Purpose
- Provide a seamless and intuitive e-commerce experience for customers to browse, filter, and purchase products.
- Empower site owners to manage the store's course selection and customer orders efficiently.

##### Primary User Needs
- Guest users need to browse courses and checkout with ease.
- Registered customers need a streamlined shopping experience with account and order history features.
- Site owners need robust tools for course and order management.

##### Business Goals
- Drive sales by providing a user-friendly shopping experience.
- Build customer loyalty through personalized and efficient account features.
- Maintain an organized and up-to-date course selection.

#### 2. Scope Plane
##### Features
- A full list of [Features](#features) can be viewed in detail below.

##### Content Requirements
- Course details, including name, price, description, tier, and images.
- Clear prompts and instructions for browsing, filtering, and purchasing.
- Order details, confirmation pages, and email notifications.
- Secure payment processing using Stripe.
- Payment success emails sent to users.
- 404 page for lost users.
- 500 page for errors.

#### 3. Structure Plane
##### Information Architecture
- **Navigation Menu**:
  - Links to Home, Courses, Bag, Newsletter, About, Faq, Contact Us and Account sections.
- **Hierarchy**:
  - Prominent course categories and filters for easy navigation.
  - Cart and checkout options displayed prominently for convenience.

##### User Flow
1. Guest user browses the store → filters and sorts courses by tier, price, or name.
2. Guest user adds items to the cart → proceeds to checkout.
3. Guest user creates an account or logs in during checkout → completes purchase.
4. Returning customers log in → view past orders and track purchase history.
5. Site owners manage courses → add, update, or delete courses and tier.
6. Users signup to the newsletter → potentially receive advanced notice of upcoming sales.

#### 4. Skeleton Plane
##### Wireframe Suggestions
- A full list of [Wireframes](#wireframes) can be viewed in detail below.

#### 5. Surface Plane
##### Visual Design Elements
- **[Colours](#colour-scheme)**: see below.
- **[Typography](#typography)**: see below.

### Colour Scheme

I used [coolors.co](https://coolors.co/fafafa-ff02ff-0aeaf1-8dff0a-ffe91a-28003d-020202) to generate my color palette.

- `#FAFAFA` - Seasalt
- `#FF02FE` - Fuchsia
- `#OAEAF1` - Fluorescent Cyan
- `#8DEFOA` - Chartreuse
- `#FFE91A` - Canary
- `#28003D` - Russian Violet
- `#020202` - Black

![screenshot](documentation/coolors.png)

I wanted to go for a neon theme due to the name of the site so I chose Russian Violet. I also felt that this aligned with the theme of DJing and nightclubs. To resemble this best as possible I made my main back ground dark and had all the other elements a selection of neon colours to try to resemble bright neon lights against a dark club backdrop. 

I used colour in other ways such as my main logo text. I added a colour gradient to it and then added another gradient to the hover effect. Now when you hover over it the colours of NeonBeats slightly flicker giving the effect of strobe lights in a nightclub. Another way I used colour was in my course tiers. Each course tier had its own card colour, and also had its own picture them. For example beginners courses had a green card and their pictures all had a blue tone to them. 

### Contrast Grid

I used [Contrast Grid Eight Shapes](https://contrast-grid.eightshapes.com/) to check all of my colours for accessibility against each other.

![screenshot](documentation/contrast-grid.png)

### Typography

- [Orbitron](https://fonts.google.com/specimen/Roboto+Mono) was used for the primary headers and titles.
- [Roboto Mono](https://fonts.google.com/specimen/Orbitron) was used for all other secondary text.
- [Font Awesome](https://fontawesome.com) icons were used throughout the site, such as the social media icons in the footer.

I chose to use Orbitron for all of the headers and titles because I felt that it had a very retro and robotic feel to it which relates to the neon theme I have chosen. 

I chose Roboto Mono to compliment it because it naturally compliments Orbitron due to its quite robotic and box like nature.

## User Stories

### Site User

- As a site user I can easily view products so that I can choose which ones to buy.

- As a site user I can see further details of a product so that I can decide if it is the right product for me.

- As a site user I can find information about the site and so that I can understand what services the site offers.

- As a site user I would like to contact the site owner so that they can answer any queries I have.

- As a site user I can add items to my basket so that they are saved while I continue shopping.

- As a site user I can create an account and login so that I can have a personal account and order items.

- As a site user I can securely enter my credit card details so that I can securely purchase a product.

- As a site user I can view my order confirmation so I can make sure that I have not made any mistakes.

- As a site user I would like to receive an order confirmation email of what I’ve ordered so that I can have a record of the order.

- As a site user I can receive email confirmation after registering so that I can know my account was successfully created.

- As a site user I can receive email confirmation after subscribing so that I know I am successfully signed up to the newsletter.

- As a site user I can view specific tiers of courses so that i can easily find courses suitable to my skill level.

- As a site user i can read frequently asked questions from other users so that i can find potential answers to my questions with ease.

- As a site user I can easily navigate back to the main site if an error message appears so that I can continue shopping.

- As a site user I can subscribe to a newsletter so that i can stay up to date with new courses.

- As a site site user I can leave comments product so that I can ask the site owner a question or tell others what I thought of it. 

- As a site user I can search for products throughout the site so that I can find a specific product easily.

### Returning Site User

- As a returning site user I can change password so that I can keep my account up to date.

- As a site user when logged I can have a user profile so that I can change my details.

- As a site user when logged in I can view my order history so that I can see what I have ordered

- As a returning site user when logged in I can edit my name and email address on the profile page so that I can keep my account up to date.

### Guest Site User

- As a guest user I would like to browse products without needing to register so that I can shop freely before deciding to create an account.

### Site Owner

- As a site owner I can add products to the site so that I can give my customers access to new products.

- As a site owner I can edit a product so that I can keep the details up to date or adjust the price.

- As a site owner I can delete a product so that I can remove items that are no longer available.

- As a site owner I can log in to the admin panel so that I can view orders.

- As a site owner I can log in to the admin panel so that I can check messages from site users.

- As a site owner I can change the about text so that I can keep users updated with any relevant information.

- As a site owner I can manage products in the admin panel so that i have full control of them in one place. 

- As a site owner I can dynamically create pages for courses so I can avoid the page being too cluttered.

- As a site owner I can make sure the users order is processed even if checkout is interrupted so that the user still receives their order.

## Wireframes

To follow best practice, wireframes were developed for mobile, tablet, and desktop sizes.
I've used [Balsamiq](https://balsamiq.com/wireframes) to design my site wireframes.

| Page | Mobile | Tablet | Desktop |
| --- | --- | --- | --- |
| Index | ![screenshot](documentation/wireframes/mobile-index.png) | ![screenshot](documentation/wireframes/tablet-index.png) | ![screenshot](documentation/wireframes/desktop-index.png) |
| Courses | ![screenshot](documentation/wireframes/mobile-courses.png) | ![screenshot](documentation/wireframes/tablet-courses.png) | ![screenshot](documentation/wireframes/desktop-courses.png) |
| Course Detail | ![screenshot](documentation/wireframes/mobile-course-detail.png) | ![screenshot](documentation/wireframes/tablet-course-detail.png) | ![screenshot](documentation/wireframes/desktop-course-detail.png) |
| Add Course | ![screenshot](documentation/wireframes/mobile-add-course.png) | ![screenshot](documentation/wireframes/tablet-add-course.png) | ![screenshot](documentation/wireframes/desktop-add-course.png) |
| Edit Course | ![screenshot](documentation/wireframes/mobile-edit-course.png) | ![screenshot](documentation/wireframes/tablet-edit-course.png) | ![screenshot](documentation/wireframes/desktop-edit-course.png) |
| Bag | ![screenshot](documentation/wireframes/mobile-bag.png) | ![screenshot](documentation/wireframes/tablet-bag.png) | ![screenshot](documentation/wireframes/desktop-bag.png) |
| Checkout | ![screenshot](documentation/wireframes/mobile-checkout.png) | ![screenshot](documentation/wireframes/tablet-checkout.png) | ![screenshot](documentation/wireframes/desktop-checkout.png) |
| Checkout Success | ![screenshot](documentation/wireframes/mobile-checkout-success.png) | ![screenshot](documentation/wireframes/tablet-checkout-success.png) | ![screenshot](documentation/wireframes/desktop-checkout-success.png) |
| Profile | ![screenshot](documentation/wireframes/mobile-profile.png) | ![screenshot](documentation/wireframes/tablet-profile.png) | ![screenshot](documentation/wireframes/desktop-profile.png) |
| About | ![screenshot](documentation/wireframes/mobile-about.png) | ![screenshot](documentation/wireframes/tablet-about.png) | ![screenshot](documentation/wireframes/desktop-about.png) |
| Contact | ![screenshot](documentation/wireframes/mobile-contact-us.png) | ![screenshot](documentation/wireframes/tablet-contact-us.png) | ![screenshot](documentation/wireframes/desktop-contact-us.png) |
| FAQ | ![screenshot](documentation/wireframes/mobile-faq.png) | ![screenshot](documentation/wireframes/tablet-faq.png) | ![screenshot](documentation/wireframes/desktop-faq.png) |
| Newsletter | ![screenshot](documentation/wireframes/mobile-newsletter.png) | ![screenshot](documentation/wireframes/tablet-newsletter.png) | ![screenshot](documentation/wireframes/desktop-newsletter.png) |
| Signup | ![screenshot](documentation/wireframes/mobile-signup.png) | ![screenshot](documentation/wireframes/tablet-signup.png) | ![screenshot](documentation/wireframes/desktop-signup.png) |
| Login | ![screenshot](documentation/wireframes/mobile-login.png) | ![screenshot](documentation/wireframes/tablet-login.png) | ![screenshot](documentation/wireframes/desktop-login.png) |
| Logout | ![screenshot](documentation/wireframes/mobile-logout.png) | ![screenshot](documentation/wireframes/tablet-logout.png) | ![screenshot](documentation/wireframes/desktop-logout.png) |
| Change Password | ![screenshot](documentation/wireframes/mobile-password-change.png) | ![screenshot](documentation/wireframes/tablet-password-change.png) | ![screenshot](documentation/wireframes/desktop-password-change.png) |
| 404 | ![screenshot](documentation/wireframes/mobile-404.png) | ![screenshot](documentation/wireframes/tablet-404.png) | ![screenshot](documentation/wireframes/desktop-404.png) |
| 404 | ![screenshot](documentation/wireframes/mobile-404.png) | ![screenshot](documentation/wireframes/tablet-404.png) | ![screenshot](documentation/wireframes/desktop-404.png) |

## Features

### Existing Features

| Feature | Notes | Screenshot |
| --- | --- | --- |
| Logo | The logo is fixed on the navigation bar on the far left so the user always knows which website that they are on and that they aren’t being redirected to any other sites when browsing. The logo is also a link back to the home page when clicked for easy navigation for users. I made the logo a blend of neon colours to go with the theme and name of the site. | ![screenshot](documentation/features/logo.png) |
| | The logo also has a fun hover effect which makes the gradient move ever so slightly to resemble lights on a dance floor when hovered on and off. | ![screenshot](documentation/features/logo-hover.png) |
| Mobile Logo | I used just the image logo on mobile so that users could recognize it but also it is small so wouldn't clutter the header. It also acts as a link back to the home page. | ![screenshot](documentation/features/mobile-logo.png) |
| Favicon | I used just the image logo on mobile so that users could recognize it but also it is small so wouldn't clutter the header. It also acts as a link back to the home page. | ![screenshot](documentation/features/favicon.png) |
| Navigation Bar | The navigation bar is fixed at the top of the page and consists of the logo, page links, and the account menu. The links have a hover class applied to them and change colour when hovered over. They also have an active class and change colour when the user is on that page so the user always knows what page they are on. The hover styles and active class can be seen in the screnshot. | ![screenshot](documentation/features/nav-bar.png) |
|  | The navigation bar is fixed at the top of the page and consists of the logo, page links, and the account menu. The links have a hover class applied to them and increase in size when hovered over. They also have an active class and change colour when the user is on that page so the user always knows what page they are on. | ![screenshot](documentation/features/hamburger-menu.png) |
| Dropdown Menu | On screens with a width below 992px when the hamburger menu is clicked the links are displayed neatly in a drop down menu instead. | ![screenshot](documentation/features/dropdown-menu.png) |
| Account Menu | The account menu is on to the navigation bar at the top of the screen and features links related to the users account such as their profile, login, logout, sign up and change password. If the user is a superuser it will have a product The links displayed are dependant on whether the user is logged in or not. |  |
|  | Logged In | ![screenshot](documentation/features/logged-in-account-menu.png) |
|  | Logged Out | ![screenshot](documentation/features/logged-out-account-menu.png) |
|  | Superuser | ![screenshot](documentation/features/super-user-account-menu.png) |
| Dynamic Bag Button | The bag button is located at the top right of the header. It is white when it is empty and then changes blue when an item is in the bag. It also displays the total price of the bag when it is populated. |  |
|  | Empty Bag | ![screenshot](documentation/features/empty-bag.png) |
|  | Bag with Items | ![screenshot](documentation/features/items-bag.png) |
| Dynamic Page Title | The page title is dynamically rendered for each page. It is displayed at the top of every page but is pushed down the page so as to show a lot of the hero banner when the page is first loaded. With the banner constantly changing colours behind it I used a text shadow to make the letters pop a bit and also for better accessibility. | ![screenshot](documentation/features/dynamic-title.png) |
| Bag Scrollable Preview | When an item is added to the bag a success message will appear with a preview of the bag items. If the bag has multiple items the items become scrollable to avoid making the message box to large and cluttering the page. | ![screenshot](documentation/features/bag-preview.png) |
| Dynamic Hero Image | The background is changed for every page through use of classes and template tags. On the course detail page it is dynamically changed to whatever the course image is. If no image was uploaded then it would be filled by a placeholder image instead. |  |
|  | General Banner | ![screenshot](documentation/features/dynamic-banner.png) |
|  | Dynamic course detail page banner that displays the course image as the banner. It will display a fallback image if no course image is found. | ![screenshot](documentation/features/dynamic-course-banner.png) |
| Footer | The footer sits at the bottom of every page and contains links to the companies social media accounts. When these are clicked they are opened in a new window to avoid taking the user away from the website. Each footer icon also has a hover effect applied to it. | ![screenshot](documentation/features/footer.png) |
| Home Page | The home page features a message and large button so users can easily start shopping. | ![screenshot](documentation/features/home.png) |
| Add/Edit Course Form | The add course form contains fields for tier, name, description, difficulty, price and image. The edit form is pre-populated with the course details already in the database and shows a preview of the image. |  |
|  | Add Course | ![screenshot](documentation/features/add-course-form.png) |
|  | Edit Course | ![screenshot](documentation/features/edit-course-form.png) |
| Summernote Widget | I incorporated summernote for the description field so that users could properly format the description due to some being fairly long. I used a summernote widget on the add/edit a course pages so that they would have full control over the content and could add features like paragraphs, bold etc. | ![screenshot](documentation/features/summernote.png) |
| Difficulty | I used a widget to display the course difficulty in a scrollable dropdown menu. | ![screenshot](documentation/features/difficulty.png) |
| Image field | The image field has a select image button. On the add course page it just shows a message saying which image you have selected. But on the edit course page it shows you a preview of the image stored in the database and gives you the option to remove it with a checkbox. Each also has a message displayed to show the new image selected if you are adding or changing the image. |  |
|  | Add Course Image Field | ![screenshot](documentation/features/add-course-image.png) |
|  | Edit Course Image Field | ![screenshot](documentation/features/edit-course-image.png) |
| Course Details | The course details are displayed on a dynamically created page using the id. It displays all of the information related to the course that was defined in the add/edit course form. It displays course details such as name, image, price, difficuly and what tier the course is in which is a clickable link. | ![screenshot](documentation/features/course-detail.png) |
| Course Detail Buttons | Buttons for the user to keep shopping and be redirected back to the courses page, or  add the course to the bag. | ![screenshot](documentation/features/course-detail-buttons.png) |
| Disabled Add To Bag Button | Because the site only sells digital products, it would only cause confusion. To avoid this the add to bag button is clearly disabled when the item is already in the bag and the text changes to 'ALREDY IN BAG'. Also the cursor changed from pointer to `not-allowed` on hover to even further emphasize to the user that they can not add this item to their bag again. | ![screenshot](documentation/features/course-disabled-button.png) |
| Edit/Delete Buttons | On the course detail and courses page, there are edit and delete buttons that are only displayed to superusers. Each has a hover class to change colour when hovered over. | ![screenshot](documentation/features/edit-delete-btns.png) |
| Delete Modal | When a superuser chooses to delete an course, a modal appears asking them if to confirm. This was done to make sure the superuser definatly wants to delete it and it wasn’t just clicked by mistake. | ![screenshot](documentation/features/delete-modal.png) |
| Course Cards | On the all courses and the course search page I displayed the courses on cards in bright colours to stand out against the dark background. The image and course names are fully clickable as a link to the course detail page. When the image is hovered over it zooms in slightly to show its clickable. The course name and tier links have hover classes applied to them to expand and show they are clickable links. | ![screenshot](documentation/features/course-cards.png) |
| Dynamic Course Card Rows | I have used logic to display a different amount of course cards on each row depending on the screen size. |  |
|  | Mobile - One Card | ![screenshot](documentation/features/1-course-card-row.png) |
|  | Tablet - Two Cards | ![screenshot](documentation/features/2-course-card-row.png) |
|  | Desktop - Three Cards | ![screenshot](documentation/features/3-course-card-row.png) |
|  | Large Desktop - Four Cards | ![screenshot](documentation/features/course-cards.png) |
| Placeholder Image | If a user does not upload a course image a placeholder is used instead. | ![screenshot](documentation/features/placeholder.png) |
| Tier Buttons | On the courses page the user can choose to filter the courses via tier by using colourful buttons at the top. Each button is the same colour as the card colour that is defined for that difficulty. Each button has a hoverclass for user feedback | ![screenshot](documentation/features/tier-buttons.png) |
| About | The about section is fully editable by the site owner so that they can update the about text whenever they like. | ![screenshot](documentation/features/about.png) |
| Updated On | On the about page it displays to the user when the about text was last edited so that can see how up to date it is. | ![screenshot](documentation/features/updated-on.png) |
| Contact Form | The contact form is a way for a user to contact the site owner and ask any questions they have. This was done using a contact form. The site owner will then be able to view the users query in the admin panel. | ![screenshot](documentation/features/contact-form.png) |
| User Profile | Each user has a profile page that is created dynamically. This is filled with the users address details if they chose to save them, or blank if they have not placed an order yet. They can add/update their information here and submit using an update button. The fields are for phone number and address information. The country field is a pre-populated dropdown. | ![screenshot](documentation/features/profile.png) |
| Order History | On the profile page there is an order history section that displays all of the users previous orders. Each order number acts as a link to the order details page that was previously shown to the user when they place their order. The fields shown are order number, date, items, and order total. | ![screenshot](documentation/features/order-history.png) |
| View a Previous Order | This displays the order success page that is displayed to the user when they place an order. To ensure no confusion an alert message pops up to show that the user is viewing a previous order. This also a message that tells the user that they would have already recieved a confirmation email for this order. |  |
|  | Previous Order Details Page | ![screenshot](documentation/features/checkout-success.png) |
|  | Alert Message | ![screenshot](documentation/features/previous-order-alert.png) |
| Shopping Bag | The bag page features a list of your items with the image and price, and the option to remove the item. It also features an order total and two buttons to keep shopping or checkout. | ![screenshot](documentation/features/bag.png) |
| Checkout Form | The checkout form fields are name, email, phone number followed by address details. The number and address details are pre-populated if the user is logged in and has saved their information to the database. A checkbox is also featured to give the user the option to save their information for next time. | ![screenshot](documentation/features/checkout-form.png) |
| Order Confirmation Email | When the user has completed their order an email is sent to them with details of their order. | ![screenshot](documentation/features/subscribe-email.png) |
| Card Payment Field | The card payment field provides live feedback to users if they are incorrectly entering information |  |
|  | Card Field Blank | ![screenshot](documentation/features/card-blank.png) |
|  | Card Field Invalid | ![screenshot](documentation/features/card-invalid.png) |
|  | Card Field Expiration Date In The Past | ![screenshot](documentation/features/card-expiration.png) |
|  | Card Field Invalid Post Code | ![screenshot](documentation/features/card-post-code.png) |
| Checkout Order Summary | An order summary is featured to provide the user with a summary of the items they are purchasing. | ![screenshot](documentation/features/order-summary.png) |
| Checkout Buttons | Featured at the bottom of the checkout forms are two buttons. One to continue shopping and one to checkout. There is also a dynamic message at the bottom giving users a warning of how much they are about to spend before they press checkout button | ![screenshot](documentation/features/checkout-buttons.png) |
| Overlay | When the user clicks checkout on the checkout page an overlay appears with a spinning icon to provide feedback that their order is being processed. | ![screenshot](documentation/features/overlay.png) |
| Image Feedback Statements | Feedback statements are used to provide the user with a statement telling them which image they are going to be uploading before the click submit. This is so they can check that they selected the right one |  |
|  | Add image feedback statement | ![screenshot](documentation/features/feedback-add-image.png) |
|  | Edit image feedback statement | ![screenshot](documentation/features/feedback-edit-image.png) |
| Subscribe Feedback Statement | Feedback statement is used to provide the user with information about why the field was invalid. | ![screenshot](documentation/features/feedback-subscribe-email.png) |
| Subscribe Email | Email sent to user when they subscribe to our newsletter. | ![screenshot](documentation/features/subscribe-email.png) |
| Newsletter Information | Information about the newsletter pursuading the user to subscribe. | ![screenshot](documentation/features/newsletter-info.png) |
| Subscribe Section | Email field for user to fill out with subscribe button | ![screenshot](documentation/features/subscribe-field.png) |
| FAQ Accordian | Frequently asked questions displayed in accordian with dropdown answers on click. Questions are ordered by importance as set by the superuser in the admin panel where they are added. If questions are of duplicate importance they are then ordered by the `created_on` field.  | ![screenshot](documentation/features/faq-accordian.png) |
| FAQ Contact Us Button | Button featured for the user incase their question has not been answered. The button links to the contact us page so that they can message us directly. | ![screenshot](documentation/features/faq-contact-button.png) |
|  | Error: Course add form invalid | ![screenshot](documentation/features/message-error-add.png) |
|  | Success: Item added to bag and preview displayed | ![screenshot](documentation/features/message-bag-add.png) |
|  | Success: Item successfully removed from bag | ![screenshot](documentation/features/message-bag-remove.png) |
|  | Success: Course successfully deleted | ![screenshot](documentation/features/message-delete-success.png) |
|  | Success: Course successfully updated | ![screenshot](documentation/features/message-edit-updated.png) |
|  | Success: Order confirmed | ![screenshot](documentation/features/message-order-success.png) |
|  | Success: Course successfully added | ![screenshot](documentation/features/message-success-add.png) |
|  | Alert: Informing the superuser they are editing a course | ![screenshot](documentation/features/message-editing.png) |
| Sign Up | There is a sign up page for users to create an account. | ![screenshot](documentation/features/signup.png) |
| Login | There is a login page for users to login. | ![screenshot](documentation/features/login.png) |
| Logout | There is a logout page confirming that the user defiantly wants to logout. | ![screenshot](documentation/features/logout.png) |
| Change Password | There is a change password page for users that want to change their password. | ![screenshot](documentation/features/change-password.png) |
| 404 Error Page | There is a 404 error page incase users enter a wrong URL. There is a button on this page to easily navigate users back to the site. | ![screenshot](documentation/features/404-page.png) |
| 500 Error Page | There is a 500 error page and there is a button on this page to easily navigate users back to the site. | ![screenshot](documentation/features/500-page.png) |
| SEO | SEO optimization with a sitemap.xml, robots.txt, and other features such as: |  |
|  | Appropriate meta tags to improve search engine visibility. | ![screenshot](documentation/features/seo-meta.png) |
|  | About `h2` text | ![screenshot](documentation/features/seo-about.png) |
|  | Courses `h2` text | ![screenshot](documentation/features/seo-courses.png) |
|  | Index Page Title | ![screenshot](documentation/features/seo-title.png) |
| Marketing | Social media presence is available in the footer using external links, as well as a Facebook Marketplace wireframe in the README for future integrations. | ![screenshot](documentation/features/footer.png) |
| Heroku Deployment | The site is deployed to Heroku, making it accessible online for users. | ![screenshot](documentation/features/heroku.png) |


### Future Features

- **Returning Site User: Edit Name and Email on Profile Page**: Give returning users the ability to to edit their name and email on the profile page.

- **Site User: Product search**: Give users the ability to search for courses as the site grows and more are added.

- **Site Owner: Extra Courses Pages**: As the site grows I would add pagination to dynamically render pages for the courses.

- **Site Owner: Add Webhooks to Checkout**: Add webhooks to make sure a users order is still processed even if an error occurs during the checkout process.

- **Site User: Leave comments about a Course**: Give users the option to comment on each course to give feedback to other users.


## Tools & Technologies

| Tool / Tech | Use |
| --- | --- |
| [![badge](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://markdown.2bn.dev) | Generate README and TESTING templates. |
| [![badge](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) | Version control. (`git add`, `git commit`, `git push`) |
| [![badge](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) | Secure online code storage. |
| [![badge](https://img.shields.io/badge/Gitpod-grey?logo=gitpod&logoColor=FFAE33)](https://gitpod.io) | Cloud-based IDE for development. |
| [![badge](https://img.shields.io/badge/HTML-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML) | Main site content and layout. |
| [![badge](https://img.shields.io/badge/CSS-grey?logo=css3&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS) | Design and layout. |
| [![badge](https://img.shields.io/badge/JavaScript-grey?logo=javascript&logoColor=F7DF1E)](https://www.javascript.com) | User interaction on the site. |
| [![badge](https://img.shields.io/badge/jQuery-grey?logo=jquery&logoColor=0769AD)](https://jquery.com) | User interaction on the site. |
| [![badge](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) | Back-end programming language. |
| [![badge](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) | Hosting the deployed back-end site. |
| [![badge](https://img.shields.io/badge/Bootstrap-grey?logo=bootstrap&logoColor=7952B3)](https://getbootstrap.com) | Front-end CSS framework for modern responsiveness and pre-built components. |
| [![badge](https://img.shields.io/badge/Django-grey?logo=django&logoColor=092E20)](https://www.djangoproject.com) | Python framework for the site. |
| [![badge](https://img.shields.io/badge/PostgreSQL-grey?logo=postgresql&logoColor=4169E1)](https://www.postgresql.org) | Relational database management. |
| [![badge](https://img.shields.io/badge/Cloudinary-grey?logo=cloudinary&logoColor=3448C5)](https://cloudinary.com) | Online static file storage. |
| [![badge](https://img.shields.io/badge/WhiteNoise-grey?logo=python&logoColor=FFFFFF)](https://whitenoise.readthedocs.io) | Serving static files with Heroku. |
| [![badge](https://img.shields.io/badge/Stripe-grey?logo=stripe&logoColor=008CDD)](https://stripe.com) | Online secure payments of e-commerce products/services. |
| [![badge](https://img.shields.io/badge/Gmail_API-grey?logo=gmail&logoColor=EA4335)](https://mail.google.com) | Sending emails in my application. |
| [![badge](https://img.shields.io/badge/Balsamiq-grey?logo=barmenia&logoColor=CE0908)](https://balsamiq.com/wireframes) | Creating wireframes. |
| [![badge](https://img.shields.io/badge/Font_Awesome-grey?logo=fontawesome&logoColor=528DD7)](https://fontawesome.com) | Icons. |
| [![badge](https://img.shields.io/badge/ChatGPT-grey?logo=openai&logoColor=75A99C)](https://chat.openai.com) | Help debug, troubleshoot, and explain things. |
| [![badge](https://img.shields.io/badge/Mermaid-grey?logo=mermaid&logoColor=FF3670)](https://mermaid.live) | Generate an interactive diagram for the data/schema. |
| [![Fonticon](https://img.shields.io/badge/Fonticon%20-grey)](https://gauger.io/fonticon/) | Used to generate favicon. |
| [![Coolors](https://img.shields.io/badge/Coolors%20-grey)](https://coolors.co/ffffff-919396-ff0505-373f47-25292e-020c0e) | Used to generate my colour palette. |
| [![Contrast Grid Eight Shapes](https://img.shields.io/badge/Contrast%20Grid%20Eight%20Shapes%20-grey)](https://contrast-grid.eightshapes.com/) | Used to generate contrast grid. |
| [![Google Fonts](https://img.shields.io/badge/Google%20Fonts%20-grey)](https://fonts.google.com/) | Used for fonts. |
| [![Am I Responsive?](https://img.shields.io/badge/AmI%20Responsive%20-grey)](https://ui.dev/amiresponsive) | used to generate preview imagery of the responsive design used throughout the website. |
| [![Chrome DevTools](https://img.shields.io/badge/Chrome%Devtools%20-grey)](https://developer.chrome.com/docs/devtools/) | used to check my responsive design and to run my lighthouse report. |

## Database Design

### Data Model

Entity Relationship Diagrams (ERD) help to visualize database architecture before creating models. Understanding the relationships between different tables can save time later in the project.

I have used `Mermaid` to generate an interactive ERD of my project.

```mermaid
erDiagram
    UserProfile {
        string user
        string default_phone_number
        string default_street_address1
        string default_street_address2
        string default_town_or_city
        string default_county
        string default_postcode
        string default_country
    }

    UserProfile ||--o| User : "1-to-1"

    Order {
        string order_number
        string user_profile
        string full_name
        string email
        string phone_number
        string country
        string postcode
        string town_or_city
        string street_address1
        string street_address2
        string county
        datetime date
        decimal order_total
        decimal grand_total
    }

    Order ||--o| UserProfile : "Many-to-1"

    OrderLineItem {
        string order
        string course
        decimal lineitem_total
    }

    Order ||--o| OrderLineItem : "1-to-Many"
    Course ||--o| OrderLineItem : "1-to-Many"

    Course {
        string tier
        string sku
        string name
        string description
        int difficulty
        decimal price
        string image
    }

    Course ||--o| CourseTier : "Many-to-1"

    CourseTier {
        string tier_name
        string description
    }

    About {
        string about_text
        string about_image
        datetime updated_on
    }

    ContactUs {
        string name
        string email
        string message
        bool read
    }

    FAQ {
        string question
        string answer
        int importance
        datetime created_on
        datetime updated_on
    }

    Newsletter {
        string email
        datetime date_subscribed
    }

    NewsletterInfo {
        string newsletter_info
        datetime updated_on
    }

```

source: [Mermaid](https://mermaid.live/edit#pako:eNqVVctu2zAQ_BWBZ9swbTkKdAtSFAjQJ9pcCgMCLa4cIhKpkks4buJ_Lyk_KlmU4-ok7y53dmaW1ivJFQeSEtAfBFtrVi1l5J5HA_qbVoUoIXrdh_xjUAu5jqzL9oIcCmZLzOonJSGTtlpdKHI_ATBjnGswhl5ZNxusQ7WRmdJZLnA7WJQrKy-ka2XQq3H5vD402C1lX6q3t_FYvTWhKI2WhI5RjemSHGu_au4yfUGVjw9p5tXO6j1CL1nYsswkq_oZqJgoe9GL7nQItg8NKXNR9vc8fs_bc7s4Q0BRQfPSCkMuKlYeNESFrOwn3WZL3k7uupa0jDt66f37zOQ2ZOEnIeEBoRqyMsRFm8DQpWskXKP3R-vinpbLT-iH8_X3DciVBzpH-jRQBFiYZ9uLBXePg8m1qFEo-S8nJEZcFIXI3WXa9rWotcj7rVxqDWfCdInuf_0UhzsX8KxVEWaaXcfiNMDdSlkM9GI-niG84ECqxaaz0rb2rzzrId0riSzHRxNA-49rX7kb1kFeKVVGGhg_w_t49z2A9NuC6Zp5ZCXNpr0o3mNR1Uojk3mIaO4w20SvU-ELbEwJiEEDzxh3_iYyY1fexBXwwZYPslAhdU8FmXAV141LRqQC7Qbi7pva9FwSfALnE_G7yZl-9mu5c3XMovqxlTlJUVsYkX23w1eYpAUrjYvWTJL0lbyQ9HYyp4t4enubzKZzOqXxiGxJSimdxDFNkvkNndFFcrPYjcgfpVwHOpkmi2k8i-fzJE5onMRNu19Nco-plV0_HbB2fwHBzowm)

I have used `pygraphviz` and `django-extensions` to auto-generate an ERD.

The steps taken were as follows:
- In the terminal: `sudo apt update`
- then: `sudo apt-get install python3-dev graphviz libgraphviz-dev pkg-config`
- then type `Y` to proceed
- then: `pip3 install django-extensions pygraphviz`
- in my `settings.py` file, I added the following to my `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    ...
    'django_extensions',
    ...
]
```
- back in the terminal: `python3 manage.py graph_models -a -o erd.png`
- drag the new `erd.png` file into my `documentation/` folder
- removed `'django_extensions',` from my `INSTALLED_APPS`
- finally, in the terminal: `pip3 uninstall django-extensions pygraphviz -y`

![screenshot](documentation/erd.png)

source: [medium.com](https://medium.com/@yathomasi1/1-using-django-extensions-to-visualize-the-database-diagram-in-django-application-c5fa7e710e16)

## Agile Development Process

### GitHub Projects

[GitHub Projects](https://www.github.com/lunartechfreek/neon-beats-academy/projects) served as an Agile tool for this project. Through it, EPICs, User Stories, issues/bugs, and Milestone tasks were planned, then subsequently tracked on a regular basis using the Kanban project board.

![screenshot](documentation/gh-projects.png)

### GitHub Issues

[GitHub Issues](https://www.github.com/lunartechfreek/neon-beats-academy/issues) served as an another Agile tool. There, I managed my User Stories and Milestone tasks, and tracked any issues/bugs.

| Link | Screenshot |
| --- | --- |
| [![GitHub issues](https://img.shields.io/github/issues/lunartechfreek/neon-beats-academy)](https://github.com/lunartechfreek/neon-beats-academy/issues) | ![screenshot](documentation/issues-1.png) |
| [![GitHub issues](https://img.shields.io/github/issues/lunartechfreek/neon-beats-academy)](https://github.com/lunartechfreek/neon-beats-academy/issues) | ![screenshot](documentation/issues-2.png) |
| [![GitHub issues](https://img.shields.io/github/issues/lunartechfreek/neon-beats-academy)](https://github.com/lunartechfreek/neon-beats-academy/issues) | ![screenshot](documentation/issues-3.png) |
| [![GitHub closed issues](https://img.shields.io/github/issues-closed/lunartechfreek/neon-beats-academy)](https://github.com/lunartechfreek/neon-beats-academy/issues?q=is%3Aissue+is%3Aclosed) | ![screenshot](documentation/issues-closed.png) |

### MoSCoW Prioritization

I've decomposed my Epics into User Stories for prioritizing and implementing them. Using this approach, I was able to apply "MoSCow" prioritization and labels to my User Stories within the Issues tab.

- **Must Have**: guaranteed to be delivered - required to Pass the project (*max ~60% of stories*)
- **Should Have**: adds significant value, but not vital (*~20% of stories*)
- **Could Have**: has small impact if left out (*the rest ~20% of stories*)
- **Won't Have**: not a priority for this iteration - future features

## Ecommerce Business Model

This site sells goods to individual customers, and therefore follows a **Business to Customer** model. It is of the simplest **B2C** forms, as it focuses on individual transactions, and doesn't need anything such as monthly/annual subscriptions.

It is still in its early development stages, although it already has a newsletter, and links for social media marketing.

Social media can potentially build a community of users around the business, and boost site visitor numbers, especially when using larger platforms such a Facebook.

A newsletter list can be used by the business to send regular messages to site users. For example, what items are on special offer, new courses in stock, updates to business hours, notifications of events, and much more!

## SEO & Marketing

### Keywords

I've identified some appropriate keywords to align with my site, that should help users when searching online to find my page easily from a search engine. This included a series of the following keyword types:

- Short-tail (head terms) keywords
- Long-tail keywords

I've also played around with [Word Tracker](https://www.wordtracker.com) a bit to check the frequency of some of my site's primary keywords (only until the free trial expired).

### Sitemap

I've used [XML-Sitemaps](https://www.xml-sitemaps.com) to generate a sitemap.xml file. This was generated using my deployed site URL: https://neon-beats-academy-74fa20163bce.herokuapp.com

After it finished crawling the entire site, it created a [sitemap.xml](sitemap.xml), which I've downloaded and included in the repository.

### Robots

I've created the [robots.txt](robots.txt) file at the root-level. Inside, I've included the default settings:

```txt
User-agent: *
Disallow:
Sitemap: https://neon-beats-academy-74fa20163bce.herokuapp.com/sitemap.xml
```

Further links for future implementation:
- [Google search console](https://search.google.com/search-console)
- [Creating and submitting a sitemap](https://developers.google.com/search/docs/advanced/sitemaps/build-sitemap)
- [Managing your sitemaps and using sitemaps reports](https://support.google.com/webmasters/answer/7451001)
- [Testing the robots.txt file](https://support.google.com/webmasters/answer/6062598)

### Social Media Marketing

Creating a strong social base (with participation) and linking that to the business site can help drive sales. Using more popular providers with a wider user base, such as Facebook, typically maximizes site views.

I've created a mockup Facebook business account using the [Balsamiq template](https://code-institute-org.github.io/5P-Assessments-Handbook/files/Facebook_Mockups.zip) provided by Code Institute.

![screenshot](documentation/mockup-facebook.png)

### Newsletter Marketing

I have incorporated a newsletter sign-up form on my application, to allow users to supply their email address if they are interested in learning more. 

⚠️ OPTION 1: RECOMMENDED ⚠️

**Custom Django Model Newsletter**


    ```python
    def subscribe(request):
    """
    Handle the subscription form and display the latest newsletter information.
    """
    # Handle the subscription form submission
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            # Check if the email is already subscribed
            if Newsletter.objects.filter(email=email).exists():
                messages.error(
                    request, "You are already subscribed to the newsletter!")
            else:
                form.save()
                messages.success(
                    request, "Thank you for subscribing to our newsletter!")
                _send_subscribe_email(request, email)
    else:
        form = NewsletterForm()

    newsletter_info = NewsletterInfo.objects.order_by('-updated_on').first()

    # Fallback if no NewsletterInfo entry exists
    if not newsletter_info:
        newsletter_info = NewsletterInfo(
            newsletter_info="No newsletter information available.",
            updated_on="Unknown"
        )

    context = {
        'form': form,
        'newsletter_info': newsletter_info,
    }

    return render(request, 'newsletter/subscribe.html', context)
    ```

## Testing

> [!NOTE]
> For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The live deployed application can be found deployed on [Heroku](https://neon-beats-academy-74fa20163bce.herokuapp.com).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), then finally, click **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables to match your private `env.py` file.

> [!IMPORTANT]
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

| Key | Value |
| --- | --- |
| `CLOUDINARY_URL` | user-inserts-own-cloudinary-url |
| `HOST` | user-inserts-own-host-url |
| `DATABASE_URL` | user-inserts-own-postgres-database-url |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `EMAIL_HOST_PASS` | user-inserts-own-gmail-api-key |
| `EMAIL_HOST_USER` | user-inserts-own-gmail-email-address |
| `SECRET_KEY` | any-random-secret-key |
| `STRIPE_PUBLIC_KEY` | user-inserts-own-stripe-public-key |
| `STRIPE_SECRET_KEY` | user-inserts-own-stripe-secret-key |
| `STRIPE_WH_SECRET` | user-inserts-own-stripe-webhook-secret |

Heroku needs some additional files in order to deploy properly.

- [requirements.txt](requirements.txt)
- [Procfile](Procfile)

You can install this project's **[requirements.txt](requirements.txt)** (*where applicable*) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **[Procfile](Procfile)** can be created with the following command:

- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace `app_name` with the name of your primary Django app name; the folder where `settings.py` is located*

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either (*recommended*):

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (*replace `app_name` with your app name*)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

### Cloudinary API

This project uses the [Cloudinary API](https://cloudinary.com) to store media assets online, due to the fact that Heroku doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.

- For "Primary Interest", you can choose **Programmable Media for image and video API**.
- *Optional*: edit your assigned cloud name to something more memorable.
- On your Cloudinary Dashboard, you can copy your **API Environment Variable**.
- Be sure to remove the leading `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.
    - `cloudinary://123456789012345:AbCdEfGhIjKlMnOpQrStuVwXyZa@1a2b3c4d5)`
- This will go into your own `env.py` file, and Heroku Config Vars, using the **key** of `CLOUDINARY_URL`.

### PostgreSQL

This project uses a [Code Institute PostgreSQL Database](https://dbs.ci-dbs.net) for the Relational Database with Django.

> [!CAUTION]
> - PostgreSQL databases by Code Institute are only available to CI Students.
> - You must acquire your own PostgreSQL database through some other method if you plan to clone/fork this repository.
> - Code Institute students are allowed a maximum of 8 databases.
> - Databases are subject to deletion after 18 months.

To obtain my own Postgres Database from Code Institute, I followed these steps:

- Submitted my email address to the CI PostgreSQL Database link above.
- An email was sent to me with my new Postgres Database.
- The Database connection string will resemble something like this:
    - `postgres://<db_username>:<db_password>@<db_host_url>/<db_name>`
- You can use the above URL with Django; simply paste it into your `env.py` file and Heroku Config Vars as `DATABASE_URL`.

### Stripe API

This project uses [Stripe](https://stripe.com) to handle the ecommerce payments.

Once you've created a Stripe account and logged-in, follow these series of steps to get your project connected.

- From your Stripe dashboard, click to expand the "Get your test API keys".
- You'll have two keys here:
	- `STRIPE_PUBLIC_KEY` = Publishable Key (starts with **pk**)
	- `STRIPE_SECRET_KEY` = Secret Key (starts with **sk**)

As a backup, in case users prematurely close the purchase-order page during payment, we can include Stripe Webhooks.

- From your Stripe dashboard, click **Developers**, and select **Webhooks**.
- From there, click **Add Endpoint**.
	- `https://neon-beats-academy-74fa20163bce.herokuapp.com/checkout/wh/`
- Click **receive all events**.
- Click **Add Endpoint** to complete the process.
- You'll have a new key here:
	- `STRIPE_WH_SECRET` = Signing Secret (Wehbook) Key (starts with **wh**)

### Gmail API

This project uses [Gmail](https://mail.google.com) to handle sending emails to users for purchase order confirmations.

Once you've created a Gmail (Google) account and logged-in, follow these series of steps to get your project connected.

- Click on the **Account Settings** (cog icon) in the top-right corner of Gmail.
- Click on the **Accounts and Import** tab.
- Within the section called "Change account settings", click on the link for **Other Google Account settings**.
- From this new page, select **Security** on the left.
- Select **2-Step Verification** to turn it on. (*verify your password and account*)
- Once verified, select **Turn On** for 2FA.
- Navigate back to the **Security** page, and you'll see a new option called **App passwords** (*search for it at the top, if not*).
- This might prompt you once again to confirm your password and account.
- Select **Mail** for the app type.
- Select **Other (Custom name)** for the device type.
    - Any custom name, such as "Django" or `neon-beats-academy`
- You'll be provided with a 16-character password (API key).
    - Save this somewhere locally, as you cannot access this key again later!
    - If your 16-character password contains *spaces*, make sure to remove them entirely.
    - `EMAIL_HOST_PASS` = user's 16-character API key
    - `EMAIL_HOST_USER` = user's own personal Gmail email address

### WhiteNoise

This project uses the [WhiteNoise](https://whitenoise.readthedocs.io/en/latest/) to aid with static files temporarily hosted on the live Heroku site.

To include WhiteNoise in your own projects:

- Install the latest WhiteNoise package:
    - `pip install whitenoise`
- Update the `requirements.txt` file with the newly installed package:
    - `pip freeze --local > requirements.txt`
- Edit your `settings.py` file and add WhiteNoise to the `MIDDLEWARE` list, above all other middleware (apart from Django’s "SecurityMiddleware"):

```python
# settings.py

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # any additional middleware
]
```


### Local Development

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the [requirements.txt](requirements.txt) file.

- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level, and include the same environment variables listed above from the Heroku deployment steps.

> [!IMPORTANT]
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

Sample `env.py` file:

```python
import os

os.environ.setdefault("CLOUDINARY_UR", "user-inserts-own-cloudinary-url")
os.environ.setdefault("HOST", "user-inserts-own-host-url")
os.environ.setdefault("DATABASE_URL", "user-inserts-own-postgres-database-url")
os.environ.setdefault("EMAIL_HOST_PASS", "user-inserts-own-gmail-host-api-key")
os.environ.setdefault("EMAIL_HOST_USER", "user-inserts-own-gmail-email-address")
os.environ.setdefault("SECRET_KEY", "any-random-secret-key")
os.environ.setdefault("STRIPE_PUBLIC_KEY", "user-inserts-own-stripe-public-key")
os.environ.setdefault("STRIPE_SECRET_KEY", "user-inserts-own-stripe-secret-key")
os.environ.setdefault("STRIPE_WH_SECRET", "user-inserts-own-stripe-webhook-secret")  # only if using Stripe Webhooks

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
os.environ.setdefault("DEVELOPMENT", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` (*Windows/Linux*) or `⌘+C` (*Mac*)
- Make any necessary migrations: `python3 manage.py makemigrations --dry-run` then `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate --plan` then `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (*if applicable*): `python3 manage.py loaddata file-name.json` (*repeat for each file*)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

If you'd like to backup your database models, use the following command for each model you'd like to create a fixture for:

- `python3 manage.py dumpdata your-model > your-model.json`
- *repeat this action for each model you wish to backup*
- **NOTE**: You should never make a backup of the default *admin* or *users* data with confidential information.

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://www.github.com/lunartechfreek/neon-beats-academy).
2. Locate and click on the green "Code" button at the very top, above the commits and files.
3. Select whether you prefer to clone using "HTTPS", "SSH", or "GitHub CLI", and click the "copy" button to copy the URL to your clipboard.
4. Open "Git Bash" or "Terminal".
5. Change the current working directory to the location where you want the cloned directory.
6. In your IDE Terminal, type the following command to clone the repository:
	- `git clone https://www.github.com/lunartechfreek/neon-beats-academy.git`
7. Press "Enter" to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://www.github.com/lunartechfreek/neon-beats-academy)

**Please Note**: in order to directly open the project in Gitpod, you should have the browser extension installed. A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, you make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository. You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://www.github.com/lunartechfreek/neon-beats-academy).
2. At the top of the Repository, just below the "Settings" button on the menu, locate and click the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

There are no remaining major differences between the local version when compared to the deployed version online.

## Credits

### Content

| Source | Notes |
| --- | --- |
| [Markdown Builder](https://markdown.2bn.dev) | Help generating Markdown files |
| [Boutique Ado](https://codeinstitute.net) | Code Institute walkthrough project inspiration |
| [Bootstrap](https://getbootstrap.com) | Various components / responsive front-end framework |
| [Cloudinary](https://cloudinary.com) | Cloud storage for static/media files |
| [Whitenoise](https://whitenoise.readthedocs.io) | Static file service |
| [Stripe](https://docs.stripe.com/payments/elements) | Online payment services |
| [Gmail API](https://developers.google.com/gmail/api/guides) | Sending payment confirmation emails |
| [Python Tutor](https://pythontutor.com) | Additional Python help |
| [ChatGPT](https://chatgpt.com) | Help with code logic and explanations, content and complete course image |
| [TinyPNG](https://tinypng.com/) | Used for images |
| [Coolors](https://coolors.co/fafafa-ff02ff-0aeaf1-8dff0a-ffe91a-28003d-020202 ) | Used for palette |
| [ContrastGridEightShapes](https://contrast-grid.eightshapes.com/?version=1.1.0&background-colors=&foreground-colors=%23FAFAFA%0D%0A%23FF02FF%0D%0A%230AEAF1%0D%0A%238DFF0A%0D%0A%23FFE91A%0D%0A%2328003D%0D%0A%23020202&es-color-form__tile-size=compact&es-color-form__show-contrast=aaa&es-color-form__show-contrast=aa&es-color-form__show-contrast=aa18&es-color-form__show-contrast=dnp ) | Used for contrast grid |


### Media

- Images

- Banners
    - [About](https://www.wallpaperflare.com/riddim-dubstep-dj-dark-people-music-wallpaper-cozaq/download/2880x1800)
    - [Add Course](https://www.wallpaperflare.com/riddim-dubstep-dj-crowds-arms-wallpaper-cvvdz/download/2880x1800 )
    - [Bag](https://www.wallpaperflare.com/riddim-dubstep-dj-crowds-music-wallpaper-cvjje)
    - [Contact](https://www.wallpaperflare.com/riddim-dubstep-dj-crowds-music-wallpaper-cvovo/download/2880x1800)
    - [Edit](https://pixabay.com)
    - [Courses](https://www.wallpaperflare.com/red-corded-headphones-and-gray-dj-controller-headset-music-wallpaper-tghtc/download/2880x1800)
    - [Edit](https://www.wallpaperflare.com/dj-edm-marshmello-wallpaper-goxib/download/2880x1800)
    - [404](https://www.wallpaperflare.com/gray-and-black-dj-controller-photography-music-vinyl-record-wallpaper-ptepc/download/2880x1800)
    - [500](https://www.wallpaperflare.com/black-vinyl-turntable-turntables-dj-music-technology-record-wallpaper-pbsja/download/2880x1800)
    - [FAQ](https://www.wallpaperflare.com/selective-focus-photo-of-dj-controller-mixer-device-audio-wallpaper-zjstx )
    - [Home](https://www.wallpaperflare.com/riddim-dubstep-dj-dark-crowds-wallpaper-cvzxy/download)
    - [Newsletter](https://www.wallpaperflare.com/headphones-on-dj-turntable-pioneer-cdj2000-equipment-mixer-wallpaper-wnznq/download/2880x1800)
    - [Fallback](https://www.wallpaperflare.com/black-vinyl-record-turntables-music-technology-arts-culture-and-entertainment-wallpaper-hveub/download/2880x1800)
    - [Profile](https://www.ibizarocks.com/stories/new-artists-ibiza-2023-2/)
    - [Success](https://www.wallpaperflare.com/dj-headphones-gadgets-tech-technology-wallpaper-uvjoe)

- Logo
    - [Logo](https://pixabay.com)

- Courses
    - [Intro](https://www.wallpaperflare.com/black-pioneer-dj-turntable-turntables-mixing-consoles-music-wallpaper-pujpd/download/2880x1800)
    - [101](https://www.wallpaperflare.com/dj-turntable-purple-music-hand-party-arts-culture-and-entertainment-wallpaper-hxiie/download/2880x1800)
    - [Advanced](https://www.wallpaperflare.com/men-s-black-fitted-cap-music-heart-house-avicii-people-real-people-wallpaper-iaqd/download/2880x1800)
    - [Skills](https://www.wallpaperflare.com/rukes-photography-crowds-lights-dj-wallpaper-cobyg/download/2880x1800)
    - [4 Deck](https://www.wallpaperflare.com/man-performing-dj-music-with-crowd-during-nighttime-man-standing-on-stage-in-front-of-people-and-turntable-wallpaper-ztbng/download/2880x1800)
    - [RekordBox](https://www.wallpaperflare.com/riddim-dubstep-dj-crowds-people-wallpaper-coyfw/download/2880x1800)
    - [Scratching](https://www.wallpaperflare.com/riddim-dubstep-dj-crowds-people-wallpaper-coyda/download/2880x1800)
    - [Complete](https://chatgpt.com)

| Source | Notes |
| --- | --- |
| [Gauger.io](https://gauger.io/fonticon/) | Generating the favicon |
| [Wallpaper Flare](https://www.wallpaperflare.com/) | Compressing images < 5MB |
| [Font Awesome](https://fontawesome.com) | Icons used throughout the site |
| [TinyPNG](https://tinypng.com) | Compressing images < 5MB |
| [CompressPNG](https://compresspng.com) | Compressing images > 5MB |
| [CloudConvert](https://cloudconvert.com/webp-converter) | Converting images to `.webp` |

### Acknowledgements

- I would like to thank my Code Institute mentor, [Tim Nelson](https://www.github.com/TravelTimN) for the support throughout the development of this project.
- I would like to thank the [Code Institute](https://codeinstitute.net) Tutor Team for their assistance with troubleshooting and debugging some project issues.
- I would like to thank the [Code Institute Slack community](https://code-institute-room.slack.com) for the moral support; it kept me going during periods of self doubt and impostor syndrome.
- I would like to thank my partner, for believing in me, and allowing me to make this transition into software development.
- I would like to thank my employer, for supporting me in my career development change towards becoming a software developer.

