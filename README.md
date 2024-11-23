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
| Sign Up | There is a sign up page for users to create an account. | ![screenshot](documentation/features/sign-up.png) |
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

newsletter
faq
duplicate bag button


| SEO | SEO optimization with a sitemap.xml, robots.txt, and appropriate meta tags to improve search engine visibility. | ![screenshot](documentation/features/seo.png) |

| 404 | The 404 error page will indicate when a user has navigated to a page that doesn't exist, replacing the default Heroku 404 page with one that ties into the site's look and feel. | ![screenshot](documentation/features/404.png) |



