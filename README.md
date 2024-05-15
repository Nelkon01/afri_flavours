# Afri-Flavours Hub E-Commerce Website

## Overview
![logo](https://github.com/Nelkon01/afri_flavours/assets/54297166/7f0b5b2b-2777-425a-8139-91896aff7718)
Afri-Flavours Hub is a food e-commerce website developed using Django. It features user authentication, product management, a shopping cart, order processing, payment integration, a blog for sharing recipes and stories, and an admin dashboard for managing the website.

## Click [here](https://afri-flavours-0342f46728dc.herokuapp.com/) to live website.
## Table of Contents

<details>
<summary>Click to Expand</summary>

- [UX](#ux)dam
    * [Strategy](#strategy)
    * [Scope](#scope)
- [Data Structure](#data-structure)
    * [Database Choice](#database-choice)
    * [Database Models](#Database-models)
    * [ERD Diagram](#erd-diagram)
- [Design Choices](#design-choices)
    * [Colour Scheme](#colour-scheme)
    * [Typography](#typography)
    * [Imagery](#imagery)
- [User Stories](#user-stories)

  * [First Time Visitor Goals](#first-time-visitor-goals)
  * [Returning Visitor Goals](#returning-visitor-goals)
  * [Frequent User Goals](#frequent-user-goals)
  * 
      * [Implemented Elements](#implemented-elements)
        * [Forms](#forms)
        * [Database Operations](#database-operations)
        * [Additional Features](#additional-features)
        * [Future Feature Enhancements](#future-feature-enhancements)
- [Technologies Used](#technologies-used)
    * [Front-End Technologies](#front-end-technologies)
    * [Back-End Technologies](#back-end-technologies)
    * [Deployment and Hosting](#deployment-and-hosting)
    * [Version Control and Collaboration](#version-control-and-collaboration)
- [Defensive Programming](#defensive-programming)
- [Testing](#testing)
- [Deployment](#deployment)
- [Acknowledgements](#acknowledgements)

</details>

## UX

### Strategy
The website targets food enthusiasts interested in exploring and purchasing traditional African foods and ingredients, as well as learning about their cultural significance and preparation methods through the blog.

### Scope
Functional requirements include:
- User registration, login, and profile management.
- Browsing products by categories and managing shopping cart and checkout.
- Blog functionality where users can read and comment on posts related to African cuisine.
- Admin capabilities to manage product listings, user accounts, blog posts, and comments.

## Data Structure

### Database Choice
- **PostgreSQL**: Chosen for its robustness, scalability, and compatibility with Django.

### Database Models

#### Blog Models

```markdown
| Model   | Field         | Type                                    | Description                   |
|---------|---------------|-----------------------------------------|-------------------------------|
| Post    | title         | CharField(max_length=250)               | Title of the post             |
|         | author        | ForeignKey(User)                        | Author of the post            |
|         | image         | ImageField(upload_to='path')            | Image for the post            |
|         | body          | TextField()                             | Content of the post           |
|         | publish       | DateTimeField(auto_now_add=True)        | Publish date and time         |
|         | status        | CharField(max_length=10, choices=CHOICES) | Status of the post          |
| Comment | author        | CharField(max_length=100)               | Author of the comment         |
|         | body          | TextField()                             | Content of the comment        |
|         | created_on    | DateTimeField(auto_now_add=True)        | Creation date and time        |
|         | post          | ForeignKey(Post)                        | Associated post               |
|         | approved      | BooleanField(default=False)             | Whether the comment is approved |
```

#### Order Models
```markdown
| Model         | Field            | Type                                 | Description                         |
|---------------|------------------|--------------------------------------|-------------------------------------|
| Order         | order_number     | CharField(max_length=32, editable=False) | Unique order number              |
|               | user_profile     | ForeignKey(UserProfile, null=True)   | Associated user profile             |
|               | full_name        | CharField(max_length=50)             | Full name of the customer           |
|               | ...              | ...                                  | ...                                 |
| OrderLineItem | order            | ForeignKey(Order)                    | Associated order                    |
|               | product          | ForeignKey(Product)                  | Product purchased                   |
|               | quantity         | IntegerField()                       | Quantity of the product             |
|               | lineitem_total   | DecimalField(max_digits=6, decimal_places=2) | Total cost for line items       |
```

#### Product Models
```markdown
| Model    | Field          | Type                                   | Description                       |
|----------|----------------|----------------------------------------|-----------------------------------|
| Product  | category       | ForeignKey(Category, null=True)        | Category of the product           |
|          | sku            | CharField(max_length=254, null=True)   | Stock Keeping Unit                |
|          | name           | CharField(max_length=254)              | Name of the product               |
|          | description    | TextField()                            | Description of the product        |
|          | price          | DecimalField(max_digits=6, decimal_places=2) | Price of the product           |
|          | allergens      | ManyToManyField(Allergen)              | Allergens present in the product  |
|          | image          | ImageField(null=True)                  | Image of the product              |
``` 

#### Profile Models
```markdown
| Model    | Field          | Type                                   | Description                       |
|----------|----------------|----------------------------------------|-----------------------------------|
| UserProfile | user        | OneToOneField(User)                    | Associated user                   |
|          | phone_number   | CharField(max_length=20)               | Phone number of the user          |
|          | address_line1  | CharField(max_length=100)              | Primary address line              |
|          | city           | CharField(max_length=50)               | City                              |
|          | postcode       | CharField(max_length=20, null=True)    | Postal code                       |
|           | country        | CountryField(blank_label='Country', null=True) | Country of residence          |
``` 

### ERD Diagram
![output](https://github.com/Nelkon01/afri_flavours/assets/54297166/1806d4ba-8cdf-4f5e-8e99-b166a0a1fb16)

## Design Choices

### Colour Scheme
The colour scheme includes earth tones that represent African landscapes, with green highlights to evoke freshness and nature.
![Color Palette](https://github.com/Nelkon01/afri_flavours/assets/54297166/b86b77a0-3e36-4225-83c1-f555bc2896a7)

### Typography
The primary font used is **'Roboto'**, selected for its clarity and professional appearance, ensuring readability across all devices. **'Montserrat'** is utilized as the secondary font for headings, adding a distinctive character and enhancing the visual hierarchy of the content.

### Imagery
High-quality imagery is integral to the website, showcasing products and cultural symbols that appeal to customers and visually represent blog content.
- **Hero Image:** Features a captivating image of a woman holding premium quality fruits, symbolizing the superior foodstuff and ingredients available in the store.
- **Logo:** The logo incorporates the website's name, food-related icons, and a map of Africa, highlighting the store’s focus on African food and groceries, thereby reinforcing the geographical essence of the products offered.

### Favicon
The website's favicon mirrors the logo, maintaining brand consistency and enhancing the site's identity. This choice ensures that the website is easily recognizable and aligned with its overall branding strategy.
## Wireframes
wirefrea
  
**Home Page:**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/1e2c8427-c12b-413f-b735-052389f95d09)

**Add Review:**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/9a68b3c1-21a1-42bf-8b45-52040851b316)

**Edit Review:**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/6d7aac70-4005-489f-a92f-321424971c04)

**Product List:**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/951fcdad-f692-40db-b3c2-42d6c4e4c70d)

**Product Details:**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/211f5d61-5007-4bad-9850-189938a30c22)

**Expert Advice:**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/9b5dbb00-efc9-4268-a40a-794b33dee778)

**Blog:**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/4c05ad62-d2f1-4eaf-9387-976563ccb580)

**Post Detail:**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/d6abad5a-922a-498d-8a4e-85d8a1c7a4dc)

**Post Detail(with like - mobile view):**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/ac0a0019-4777-4f6b-98e0-492e5ba4eb00)

**Product List (Tablet View):**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/f2c7d22c-1d2e-40f1-a792-391052563f81)

## User Stories

### First Time Visitor Goals
1. As a First Time Visitor, I want to understand the purpose of the website so that I can determine if it meets my needs.
* Explore the homepage to learn about the products and services offered. 
* View a brief description or introduction about Afri-Flavours Hub.
2. As a First Time Visitor, I want to navigate the website easily so that I can find the information or products I am interested in.
* Access a well-structured navigation bar.
* Use a search function to quickly find specific products or information.
3. As a First Time Visitor, I want to see product categories clearly so that I can browse products by category.
* View a dropdown menu or sidebar with product categories.
* Click on categories to see relevant products.
4. As a First Time Visitor, I want to view product details so that I can make informed purchasing decisions.
* See detailed product descriptions, prices, and images.
* Read customer reviews to gauge product quality.
5. As a First Time Visitor, I want to understand the checkout process so that I know how to complete a purchase.
* Find clear instructions on how to add items to the cart and proceed to checkout.
* Understand payment options and delivery information.

### Returning Visitor Goals
1. As a Returning Visitor, I want to log into my account easily so that I can access my previous orders and saved information.

* Use a straightforward login process.
* Recover my password if I have forgotten it.
2. As a Returning Visitor, I want to view my order history so that I can track past purchases and reorder items.

* Access an order history section in my profile.
* See details of previous orders, including dates and order numbers.
3. As a Returning Visitor, I want to quickly find new products so that I can explore the latest offerings.

* See a “New Arrivals” section on the homepage or in the product categories.
* Receive notifications or highlights of new products.
4. As a Returning Visitor, I want to update my profile information so that my contact and delivery details are current.

* Edit my personal information and address in the profile section.
* Save changes to my profile easily.
5. As a Returning Visitor, I want to read blog updates so that I can stay informed about the latest information and tips.

* Access the blog section from the main menu.
* Read articles and leave comments or feedback.

### Frequent User Goals
1. As a Frequent User, I want to have a fast and efficient shopping experience so that I can complete my purchases quickly.

* Use a streamlined checkout process.
* Save payment details for faster transactions.

### Implemented Elements
### Features
**Navigation:**

- **Desktop**
<img width="1343" alt="Screenshot 2024-05-13 at 20 07 46" src="https://github.com/Nelkon01/afri_flavours/assets/54297166/174d5a22-340e-4fcb-9bad-4a1ff233ffa2">


<hr>
  
- **Tablet**
<img width="1245" alt="Screenshot 2024-05-13 at 20 08 20" src="https://github.com/Nelkon01/afri_flavours/assets/54297166/0a1ec50b-63a6-403f-aadd-5d5d2bbcf2d6">


<hr> 

- **Mobile**

<img width="554" alt="Screenshot 2024-05-13 at 20 09 32" src="https://github.com/Nelkon01/afri_flavours/assets/54297166/9e036f81-509e-4164-968e-c333a5221f61">

<hr>


### User Access Levels

- **Logged in as SuperUser**
  - Superusers have full access to all admin features and can manage products, orders, and user permissions.
<img width="559" alt="Screenshot 2024-05-13 at 20 11 33" src="https://github.com/Nelkon01/afri_flavours/assets/54297166/c38f3769-5644-4aa7-b255-bbb5e0acbba2">

<hr>

- **Not logged in**
  - Visitors can browse products and read blog posts but must log in to make purchases or leave comments.
<img width="1675" alt="Screenshot 2024-05-13 at 21 36 30" src="https://github.com/Nelkon01/afri_flavours/assets/54297166/d5d2145e-3ad3-4359-a0a8-b0e044d4e505">
<img width="1674" alt="Screenshot 2024-05-13 at 21 37 16" src="https://github.com/Nelkon01/afri_flavours/assets/54297166/95e0eb24-6b98-41be-8837-bbcbcbfd0935">

<hr>

- **Logged in as Regular User**
  - Regular users can browse, purchase products, and interact with the blog content.
<img width="1677" alt="Screenshot 2024-05-13 at 20 20 33" src="https://github.com/Nelkon01/afri_flavours/assets/54297166/ffa14aa2-2f48-4858-803c-2beac8f99b05">

<hr>

### Navigation

- **Standard Hamburger Menu for Mobile:**
  - On mobile devices, a "hamburger" menu is used to simplify navigation, providing a consistent interface for users on smaller screens.
<img width="567" alt="Screenshot 2024-05-13 at 20 22 29" src="https://github.com/Nelkon01/afri_flavours/assets/54297166/e0a82334-766e-49f8-8089-6c1a0bb992ac">

<hr>

### Authentication

- **Sign in/Sign up:**
  - Our website offers a streamlined and user-centric sign-in and sign-up process prioritizing convenience and accessibility.
  - **Easy Password Recovery:** The sign-in page includes a "Forgot Password" link, allowing users to reset their passwords easily.
  - **Sign-in:** Users can log in via username or email. New users are provided with a prominent link to sign up.
  - **Sign-up:** The sign-up page links to the sign-in page for registered users, displays clear error messages for duplicate usernames or emails, and ensures unique usernames and emails for security.
<img width="840" alt="Screenshot 2024-05-13 at 20 23 41" src="https://github.com/Nelkon01/afri_flavours/assets/54297166/b0426cf3-8007-4f46-9e0a-a2b2b861641d">
<img width="1675" alt="Screenshot 2024-05-13 at 20 24 09" src="https://github.com/Nelkon01/afri_flavours/assets/54297166/86fb8bcc-8935-4c62-8105-36a32c621408">

<hr>

### Products Page

- **Overview:**
  - Our Products Page provides a seamless shopping experience, enhancing the journey from browsing to purchasing.
  - **Product Information:** Users receive essential details about each product, ensuring informed decisions.
  - **Quantities & Descriptions:** The product detail page includes clear information such as name, price, rating, and category. Users can easily select desired quantities.
  - **Allergen Information:** Allergen details are provided for users with dietary restrictions, ensuring transparency and safety.
<img width="1662" alt="Screenshot 2024-05-13 at 20 26 00" src="https://github.com/Nelkon01/afri_flavours/assets/54297166/93e8775c-1789-481e-912b-ff0ff242dcd2">
<img width="1665" alt="Screenshot 2024-05-13 at 20 26 28" src="https://github.com/Nelkon01/afri_flavours/assets/54297166/a58a88df-0448-4e85-b587-35ec70d05237">

<hr>

### Bag & Checkout

- **Functionality:**
  - Our Bag & Checkout process ensures a smooth transaction for users.
  - **Bag Page:** Users can manage their selected products, adjust quantities, or remove items, with product images, names, prices, and SKUs displayed.
  - **Checkout Page:** Designed for simplicity and security, the checkout form collects essential shipping and payment details. Users can review their order in a summary before completing the purchase.
<img width="1676" alt="Screenshot 2024-05-13 at 20 30 38" src="https://github.com/Nelkon01/afri_flavours/assets/54297166/3735895c-8525-4235-95b5-f2df19215af6">
<img width="1662" alt="Screenshot 2024-05-13 at 20 31 28" src="https://github.com/Nelkon01/afri_flavours/assets/54297166/cecffffd-55ae-4e46-bb2a-7a160b48b61d">
<img width="1124" alt="Screenshot 2024-05-13 at 20 33 58" src="https://github.com/Nelkon01/afri_flavours/assets/54297166/7f8c4640-0b2f-4e10-9f94-6027bc4eaf19">
<img width="444" alt="Screenshot 2024-05-13 at 20 34 03" src="https://github.com/Nelkon01/afri_flavours/assets/54297166/57ce80bd-6379-4cff-a44c-57143e0c33f1">

<hr>

### Profile

- **Features:**
  - The profile feature provides a personalized hub for managing account details and tracking order history.
  - **My Profile Page:** Users can view and update their default delivery information, ensuring up-to-date shipping details.
  - **Order History:** Users have access to a comprehensive list of past orders, organized by order number, facilitating easy reordering or tracking.
<img width="1672" alt="Screenshot 2024-05-13 at 20 34 50" src="https://github.com/Nelkon01/afri_flavours/assets/54297166/d071e1c9-8dd9-499b-bca7-d2acc57e890e">

<hr>

### Blog

- **Content:**
  - Our blog offers a wealth of insights related to African food, recipes, and more.
  - **Informative Content:** The blog includes health tips, wellness advice, and recipes, with easy navigation through posts.
  - **Post Details:** Users can read entire posts and contribute to the discourse by leaving their own comments on the page
<img width="1679" alt="Screenshot 2024-05-13 at 20 40 50" src="https://github.com/Nelkon01/afri_flavours/assets/54297166/5d6b5e52-5937-4892-87de-8b11697f427b">

<hr>

### Comments

- **Engagement:**
  - The comment feature allows users to interact with blog content, fostering community engagement.
<img width="1651" alt="Screenshot 2024-05-13 at 20 45 26" src="https://github.com/Nelkon01/afri_flavours/assets/54297166/e3525cac-2e63-47f7-9c00-af7321ec4bd1">

<hr>

### Messages & Notifications

- **Feedback:**
  - Success messages are displayed for actions such as logging in, adding products to the bag, updating the bag, and removing products.
  - Alerts notify superusers/admins of edits to products.
<img width="740" alt="Screenshot 2024-05-13 at 20 30 05" src="https://github.com/Nelkon01/afri_flavours/assets/54297166/cd5d4711-73ba-4ce9-a052-a3912c02ad5e">
<img width="236" alt="Screenshot 2024-05-13 at 20 10 40" src="https://github.com/Nelkon01/afri_flavours/assets/54297166/d3bc329a-61bd-48d0-9ac0-b69910ed6b35">

<hr>

### Admin Permissions

- **Capabilities:**
  - Admins can edit or delete products on the products page.
  - Admins can add products via the product management section.
<img width="1510" alt="Screenshot 2024-05-13 at 21 07 02" src="https://github.com/Nelkon01/afri_flavours/assets/54297166/e73367aa-26f9-4f2c-94c7-28572c701eed">

<hr>

### Error Handling

- **Error Pages:**
  - **404 Error Page:** Customized page displayed when a page doesn’t exist.
  - **500 Error Page:** Shown for server errors.
  - These pages provide information about the error and suggested next steps.
<img width="1680" alt="Screenshot 2024-05-13 at 21 31 15" src="https://github.com/Nelkon01/afri_flavours/assets/54297166/3dfd1064-a38a-4e5f-88ca-1faefe989bad">
<img width="1680" alt="Screenshot 2024-05-13 at 21 33 45" src="https://github.com/Nelkon01/afri_flavours/assets/54297166/6624166a-d1ea-4352-b22a-6f355568b695">

<hr>


#### Forms
*  User registration, login, and checkout forms are designed to be intuitive and secure.
#### Database Operations
* CRUD operations for products, orders and blog posts.
#### Additional Features
* Blog integration where users can engage with African food and culture content.
* Responsive design ensures functionality across all devices.
### Future Feature Enhancements

|   | **FEATURES**                                                                                                                                   | **PRIORITY** |
|---|------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| 1 | Implementing a feature that will allow users to favourite products for later with a wishlist,  ensuring they never miss out on products.       | LOW          |
| 2 | Implementing a live chat support system to provide instant assistance and answer queries.                                                      | HIGH         |
| 3 | Offer personalized discounts based on user preferences and purchasing behaviour.                                                               | MEDIUM       |
| 4 | Introduce an Affiliate Program, allowing earning while users shop and refer others to our platform.                                            | MEDIUM       |
| 5 | Support to cater to a wider user base, allowing users from different regions and language preferences to access and use the Afri-Flavours shop | HIGH         |
| 6 | Implementation of a recipe upload feature for users.                                                                                           | HIGH         |
| 7 | Advanced search functionalities for blog posts and products.                                                                                   | HIGH         |

# Compatibility and Responsive Testing
Extensive testing was conducted on the website. It's responsiveness and features was tested on a variety of devices & browsers as noted in the table below:

| **TOOL / Device**           | **BROWSER** | **OS**                         | **SCREEN WIDTH** |
|-----------------------------|-------------|--------------------------------|------------------|
| iPhone 14 Plus v16.0        | Safari      | iOS 17.1                       | 1284x2778 px     |
| iPhone 6S v12.1             | Safari      | iOS, v12.1                     | 375 x 559 px     |
| Samsung Galaxy A52 v11.0    | Chrome      | Android, v11.0                 | 412 x 777 px     |
| Moto G9 Play v10.0          | Firefox     | Android, v10.0                 | 412 x 804 px     |
| OnePlus 6T v9.0             | Edge        | Android, v9.0                  | 412 x 757 px     |
| Samsung Galaxy A10 v9.0     | Samsung     | Android, v9.0                  | 412 x 734 px     |
| Samsung Galaxy Tab S7 v11.0 | Chrome      | Android, v11.0                 | 753 x 1037 px    |
| iPad Air                    | Safari      | Ipad Os 17.1                   | 768 x 954 px     |
| windows 11                  | Firefox     | Browser Version 115.0          | 1920 x 955 px    |
| Macbook Pro                 | Safari      | Safari 17.1 on macOS Sononma   | 1920 x 955 px    |
| windows 11                  | Yandex      | Yandex & Browser Version=14.12 | 1920 x 955 px    |

### Most Popular browser & Operating System

| Device             | Browser               | Operating System | Description                                              |
|--------------------|-----------------------|------------------|----------------------------------------------------------|
| iPhone             | Safari                | iOS              | Popular combination with significant market share        |
| Android Smartphone | Chrome                | Android          | Widely used browser on the Android platform              |
| Desktop/Laptop     | Chrome                | Windows          | Popular browser on the Windows operating system          |
| Desktop/Laptop     | Chrome                | MacOS            | Popular browser on the macOS operating system            |
| Desktop/Laptop     | Edge                  | Windows          | Microsoft Edge is gaining popularity among users         |
| Other              | Firefox/Samsung/Opera | Various          | Represents a compromise due to limited testing resources |

The choices in the table are base on the browser market share data provided by [gs.statcounter.com](https://gs.statcounter.com/). Chrome and Safari are the dominant browsers, so they are included for testing on different devices and operating systems. Edge is also included as it has a noticeable market share. Since firefox, Samsung Internet and Opera have smaller market shares, they are grouped under the "Other" category to represent a compromise due to limited testing resources.

| **BROWSER**      | **PERCENTAGE** |
|------------------|----------------|
| Chrome           | 63.55%         |
| Safari           | 19.95%         |
| Edge             | 5.13%          |
| Opera            | 2.99%          |
| Firefox          | 2.79%          |
| Samsung Internet | 2.38%          |

**Browser Market Share Worldwide - July 2023**

## Accessibility Testing
To ensure our website is accessible, I have conducted extensive testing to ensure that it caters for users with disabilities.
* Home Page - Lighthouse Audit (Desktop)

* Home Page - Lighthouse Audit (Mobile)

* Products Page - Lighthouse Audit (Desktop)

* Products Page - Lighthouse Audit (Mobile)

* Blog Page - Lighthouse Audit (Desktop)

* Blog Page - Lighthouse Audit (Mobile)

* Blog Post Details - Lighthouse Audit (Desktop)


**NOTES**
- The website has been tested for accessibility using Lighthouse Audit on Google Chrome.
- The low scores in performance are due to the type of images used on the website. This is a trade-off between image quality and performance. However better image optimization can be done to improve performance, and this will be done in the future.

## Manual Testing
Extensive Manual Testing was conducted to ensure the functionality and usability of the website. 
<details>
<summary>Validation Testing</summary>

The following site were used to aid in validation testing:

- **[CSS Validator](https://jigsaw.w3.org/css-validator/)**

**BLOG.CSS:**



<hr>

**CHECKOUT.CSS:**




<hr>

**PROFILE.CSS:**



<hr>

**BASE.CSS:**



<hr>

The following site were used to aid in validation testing:

- **[HTML Validator](https://validator.w3.org/)**

**HOME PAGE:**



<hr>

**PRODUCTS PAGE:**



<hr>

**PRODUCTS DETAILS PAGE:**



<hr>

**BLOG PAGE:**



<hr>

**BLOG PAGE DETAILS:**




<hr>

**REVIEWS PAGE:**



<hr>


**LOGOUT PAGE**



<hr>

**LOGIN PAGE**



<hr>

**REGISTER PAGE**



<hr>

**RECOVER PASSWORD PAGE**



<hr>

**MY PROFILE PAGE**



**SHOPPING BAG PAGE**



<hr>

**CHECKOUT PAGE**

<hr>

**CHECKOUT SUCCESS PAGE**



<hr>



**404 PAGE**



<hr>

**500 PAGE**



<hr>

The following site were used to aid in validation testing:

**[JS validation](https://jshint.com)**

**STRIPE_ELEMENT.JS**



<hr>

**QUANTITY_INPUT_SCRIPT**



<hr>

**COUNTRYFIELD.JS** 



<hr>

The following site were used to aid in validation testing:



</details>
<hr>

## Automated Testing
- Manual Testing was conducted due to time constrains.
- The examination of each app's views will be carried out using Django unittest module in future developments.

## Bugs and Defects
**DEFECTS** were documented in github using a custom issue template. 


### 

**Purchase confirmation email not received**
- During the final testing phase of store's functionality, I encountered a significant bug related to the purchase confirmation email system. Upon completing a purchase, I expected to receive a confirmation email detailing the order. However, the email failed to be delivered to the test users, leading to concerns about the reliability of the purchase process.
  - This has been fixed by updating the email settings in the settings.py file to include the correct email host, port, and credentials. The email backend was also updated to use the SMTP protocol for sending emails.

**Security Vulnerability - Unauthorized Access to User reviews / Order History**
- While conducting a review in the platform's security, I identified a bug that poses a significant risk to user accounts and their associated reviews. This bug allows unauthorized users to access and edit reviews, also order history that belonging to other user's accounts. Furthermore, the bug enables users to copy links that lead directly to other user's accounts, granting unauthorized access.
    - This has been fixed by implementing a custom decorator that checks the user's ID against the user ID in the URL. If the IDs do not match, the user is redirected to the home page. This ensures that only the user who created the review can access and edit it.

### Outstanding Defects
 - The active class on the navbar is not working as expected. The active class is not being applied to the correct page when the user navigates to a different page. This issue is likely due to the incorrect URL being used to determine the active class. The issue will be resolved by updating the URL in the navbar template to match the URL of the current page.

## Technologies Used
Several technologies have been used to create this project namely:

| Technology               | Description                                                                                                     |
|--------------------------|-----------------------------------------------------------------------------------------------------------------|
| Django                   | A high-level Python web framework used for rapid development, database interactions, and secure authentication. |
| Python                   | The core programming language used to build the entire application, ensuring it is fully functional.            |
| JavaScript               | Provides dynamic interactivity to the messages and enhances the functionality of the timepicker.                |
| Bootstrap                | Ensures a responsive design with its comprehensive front-end component library.                                 |
| Git                      | Version control system used for tracking changes and maintaining the project's codebase.                        |
| PostgreSQL               | Relational database management system employed to store and manage the project's data.                          |
| GitHub                   | Platform used for development, code management, and tracking changes.                                           |
| Font Awesome             | Library used to obtain icons, enhancing the overall design of the website.                                      |
| Google Developer Tools   | Primary tool for bug detection, testing responsiveness, and resolving issues across the website.                |
| Heroku                   | Platform used to deploy the website.                                                                            |
| Jigsaw                   | Tool used to validate CSS code.                                                                                 |
| W3 HTML                  | Tool used to validate HTML code.                                                                                |
| Jshint                   | Tool used to validate JavaScript code.                                                                          |
| Coloors                  | Tool used to generate the color palette for the website design.                                                 |
| AWS Amazon               | Service used to store all static files and images.                                                              |
| Stripe                   | Platform used to handle all payments on the website.                                                            |
| Lighthouse               | Tool used to test the accessibility and performance of the website.                                             |
| Balsamiq                 | Tool used to create wireframes, providing a visual representation of the website layout and structure.          |
| Markdown Table Generator | Tool used to create tables in Markdown format.                                                                  |
| Pycharm                  | Integrated development environment (IDE) used to develop the project.                                           |

### Languages
- HTML
- CSS
- Python
- JavaScript 

### Frameworks, Libraries & Programs Used
- Django
- Bootstrap
- PostgreSQL
- GitHub
- Font Awesome
- Google Developer Tools
- Heroku
- W3 HTML
- Jshint
- Coloors
- AWS Amazon
- Lighthouse
- Balsamiq
- AmIResponsive
- Markdown Table Generator

## Deployment
### Prerequisites
To run this project, you need a ElephantSQL, AWS Amazon, Sripe & Gmail account:

**ElephantSQL Set Up Account:**
1. Visit the [ElephantSQL](https://www.elephantsql.com/) website.
2. Sign up for an account if you don't have one.
3. After signing in, you will be redirected to the ElephantSQL dashboard.
4. Click on "Create New Instance" to create a new PostgreSQL database instance.
5. Choose a suitable plan for your needs.
6. Configure the database settings, such as the region and database name.
7. Click on "Create" to create the database instance.
8. Once the instance is created, you will see the details of your database, including the hostname, port, username and password.
**Retrieve the Database URL:**
1. In the ElephantSQL dashboard, locate your newly created database instance.
2. Click on the instance to view its details.
3. In the "Details" tab, you will find the connection details for your database, including the URL.
**Set Environmental Variables:**
1. After obtaining the database URL, you need to set it as an environmental variable in your development environment.
2. The specific steps to set environmental variables depend on your operating system and development environment.
3. In general, you can set the environmental variable by adding the following line to your **'env.py'** file or the environment configuration of your development enviroment: **DATABASE_URL=<YOUR_DATABASE_URL>**
4. Replace **"<YOUR_DATABASE_URL>"** with the actual database URL you obtained from ElephantSQL.

<hr>

**AWS Amazon Set Up Account/ AWS S3 Bucket:**
1. Create an [account](https://aws.amazon.com/) on AWS Amazon if you don't have one.
2. Login to your account and within the search bar type in 'S3'.
3. Within the S3 page click on the "Create Bucket".
4. Put the name that you want (i'd recommend naming your bucket to match your Heroku app name) on the bucket and select the region which is closest to you.
5. Uncheck "Block Public Access" and acknowledge that the bucket will be made public. Click on "Create Bucket"
6. Inside the bucket click on "Properties" tab. Below "Static Website Hosting" click "Edit" and change the "Static Website Hosting" hosting option to "Enabled". Copy the default values for the index and error documents and click "Save".
7. Underneath "Object Ownership" select "ACLs enabled".
10. Click on the "Permissions" tab, paste that into the Cross-origin resource sharing (CORS) section:
  ```
    [
        {
            "AllowedHeaders": [
            "Authorization"
            ],
            "AllowedMethods": [
            "GET"
            ],
            "AllowedOrigins": [
            "*"
            ],
            "ExposeHeaders": []
        }
    ]
  ```
10. Within the "Bucket Policy" section. Click "Edit" and then "Policy Generator".
11. Click the "Select Type of Policy" dropdown and select "S3 Bucket Policy" and within "Pricipal" type "*" to allow all principals. In "Actions" section select "GetObject".
12. Copy the "ARN" that is located in the previous tab.
13. Back to AWS policy generator, paste it into the "Amazon Resource Name (ARN)" box at the bottom. Click on the "Add Statement" button, then "Generate Policy".
14. Copy the policy that's been generated and paste into the "Bucket Policy Editor".
15. Before saving, add /* at the end of your "Resource Key", this will allow access to all resources within the bucket.
16. Once saved, scroll down to the "Access Control List (ACL)" and click "Edit".
17. Next to "Everyone (public access)", check the "list" checkbox and save your changes.

**Identify and Access Management (IAM) Set Up**
1. Search for IAM within the AWS navigation bar and select it.
2. Click "User Groups" that can be seen in the side-bar and then click "Create group" and name the group "manage-your-project-name".
3. Click "Policies" and then "Create Policy". There is now a button to go to the next page to add tags. Tags are
optional, but you must click it to get to the review policy page.
4. Navigate to the JSON tab and click "Import Managed Policy", within here search for "S3" and select "AmazonS3FullAccess" followed by "Import".
5. Follow the exemple bellow:
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:*",
                "s3-object-lambda:*"
            ],
            "Resource": [
                "YOUR-ARN-NO-HERE",
                "YOUR-ARN-NO-HERE/*"
            ]
        }
    ]
}

```
1. Ensure the policy has been given a name and a short description, the click "Create Policy".
2. Click "User Groups". Select your group.
3. Go to the "permissions" tab, open the "Add permissions" dropdown, and click "Attach policies".
4. Select the policy and click "Add permissions" at the bottom.

**Retrieve access keys**
1. Go to IAM and select 'Users'.
2. Select the user for whom you wish to create a CSV file.
3. Select the 'Security Credentials' tab
4. Scroll to 'Access Keys' and click 'Create access key'
5. Select 'Application running outside AWS', and click next
6. On the next screen, you can leave the 'Description tag value' blank. Click 'Create Access Key'
7. Click the 'Download .csv file' button

**Connecting AWS to the Project**
1. Within your terminal install the following packages:

```
  pip3 install boto3
  pip3 install django-storages
```

2. Freeze the requirement by typing:

```
  pip3 freeze > requirements.txt
```
3. Add "storages" to your installed apps within your settings.py file.
4. At the bottom of the settings.py file add the following code.
```
if 'USE_AWS' in os.environ:
   # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

  # Bucket Config
  AWS_STORAGE_BUCKET_NAME = 'bucket-name'
  AWS_S3_REGION_NAME = 'region-name'
  AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
  AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
  AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
```
5. Add the following keys in you Heroku app config Vars: 'AWS_ACCESS_KEY_ID' & 'AWS_SECRET_ACCESS_KEY'. This can be found in your CSV file.
6. Add the key "USE_AWS", and set to True in your Heroku app.
7. Remove the "DISABLE_COLLECSTATIC" variable from Heroku.
8. Inside the settings.py file, add the following code into your Bucket config if statement:
```
    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```

9. In your root directory create a file called "custom_storages.py". Add the following code:
```
  from django.conf import settings
  from storages.backends.s3boto3 import S3Boto3Storage
  
  
  class StaticStorage(S3Boto3Storage):
      location = settings.STATICFILES_LOCATION
  
  
  class MediaStorage(S3Boto3Storage):
      location = settings.MEDIAFILES_LOCATION
```
10. Go back to your AWS S3 bucket and click on "Create Folder", name this folder as "Media".
11. In the "Media" file click "Upload > Add files" and select the images for your site.
12. Under "Permissions" select the option "Grant public-read access" and click  "Upload".

## Stripe Payments 

- The Stripe Payments is set up as the online payment processing and credit card processing platform for the purchases.
You will need a stripe account which you can sign up for [here](https://dashboard.stripe.com/register)

### Payments
- To set up stripe payments you can follow their guide [here](https://stripe.com/ie/guides)

### API Keys
1. Click on 'Developers' in the navbar-side.
2. Beside 'Overview' click on the API Keys and you will see your 'Publishable key' & 'Secret key'.

### Adding your Keys to your Heroku app

1. Go to you app in Heroku website, navigate to the config vars section under settings.
2. Add your generated keys in the config vars:
  ```
  STRIPE_PUBLIC_KEY = '<INSERT_YOUR_PUBLISHABLE_KEY>'
  STRIPE_SECRET_KEY = '<INSERT_YOUR_SECRET_KEY>'
  ```

3. Finally, back in your settings.py file in django, insert the following keys, near to the bottom of the file:
  ```
  STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
  STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')
  ```

## Gmail Set up (Sending Real Emails with Django)

- If you've already got a Gmail account you can just log in and go to your settings.
- If you don't have one just go to [gmail.com](gmail.com) and create an account before starting this.

1. To prepare Gmail, we need to go to the account settings in the upper right. Click accounts and import.
2. Then other Google account settings.
3. Go to the security tab and under, signing into Google. Turn on 2-step verification.
4. This will allow you to create an app password specific to your Django app. That will allow it to authenticate and use our Gmail account to send emails.
5. To turn it on just click get started, enter your password.
6. Then you'll have to select a verification method.
7. You can select to send a verification code via text or you can choose any method you prefer.
8. Once you've verified and turned on two-step verification. You'll see a new option called app passwords under the signing in to Google heading.
9. Click on that enter your password again if needed.
10. Then on the app password screen, select mail for the app. Then under device type, select other and type in Django.
11. With that done we'll be given a 16 character password which I'll copy.
12.  then go to my Heroku app to enter it as a config variable.
13. Call the variable EMAIL_HOST_PASS. And paste it in and click Add. Also need another variable called EMAIL_HOST_USER.
14. The last step then is just to add a few settings to your settings.py, add the following code:

  ```
  if 'DEVELOPMENT' in os.environ:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    DEFAULT_FROM_EMAIL = '<your_example_email_here>@example.com'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
    DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')
  ```
    
## Fork and Clone the Repository
To make a copy or ‘fork’ the repository:

1. Login to your own GitHub account.
2. Navigate to [my repository](https://github.com/Nelkon01/afri_flavours).
3. In the top right corner of the page, click 'fork' option to create and copy of the original.

## Making a Local Clone
1. Under the repository name, click on the ‘code’ tab.
2. In the clone box, HTTPS tab, click on the clipboard icon .
3. In your IED open GitBash.
4. Changed the current working directory to the location you want the cloned directory to be made.
5. Type ‘git clone’ and then paste the URL copied from GitHub.
6. Press enter and the local clone will be created.

## Development Deployment

### Running the Project in PyCharm

To get started with local development in PyCharm, follow these steps:

1. **Clone the Repository:**
   - Open PyCharm.
   - Go to `File` > `New Project from Version Control` > `Git`.
   - Enter the repository URL and click `Clone`.

2. **Create a Virtual Environment:**
   - Open the terminal in PyCharm.
   - Run the following command to create a virtual environment:
     ```bash
     python3 -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows:
       ```bash
       venv\Scripts\activate
       ```
     - On macOS and Linux:
       ```bash
       source venv/bin/activate
       ```

3. **Install Dependencies:**
   - With the virtual environment activated, install the required packages by running:
     ```bash
     pip install -r requirements.txt
     ```

4. **Set Up Environment Variables:**
   - Create a file named `.env` in the root directory of your project.
   - Add the following environment variables to the `.env` file:
     ```plaintext
     DATABASE_URL=<YOUR_DATABASE_URL>
     DEVELOPMENT=True
     SECRET_KEY=<YOUR_SECRET_KEY>
     AWS_ACCESS_KEY_ID=<YOUR_AWS_ACCESS_KEY_ID>
     AWS_SECRET_ACCESS_KEY=<YOUR_AWS_SECRET_ACCESS_KEY>
     EMAIL_HOST_PASS=<YOUR_EMAIL_HOST_PASS>
     EMAIL_HOST_USER=<YOUR_EMAIL_HOST_USER>
     ```

5. **Configure Django Settings:**
   - Open `settings.py` in your Django project.
   - Add the following code to load the environment variables:
     ```python
     from decouple import config


     DATABASE_URL = config('DATABASE_URL')
     SECRET_KEY = config('SECRET_KEY')
     AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
     AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
     EMAIL_HOST_PASS = config('EMAIL_HOST_PASS')
     EMAIL_HOST_USER = config('EMAIL_HOST_USER')
     ```

6. **Apply Database Migrations:**
   - Run the following command to apply database migrations:
     ```bash
     python manage.py migrate
     ```

7. **Create a Superuser:**
   - Run the following command to create a superuser account:
     ```bash
     python manage.py createsuperuser
     ```

8. **Run the Development Server:**
   - Start the development server by running:
     ```bash
     python manage.py runserver
     ```

9. **Access the Application:**
   - Open your web browser and go to `http://127.0.0.1:8000` to see your application running locally.

---

### Additional Configuration

**Debugging:**
- To set up debugging in PyCharm, configure a Django Server run configuration:
  - Go to `Run` > `Edit Configurations`.
  - Click on the `+` button and select `Django Server`.
  - Set the `Host` to `127.0.0.1` and the `Port` to `8000`.
  - Apply the changes and start debugging.

**Git Integration:**
- To enable Git integration in PyCharm:
  - Go to `VCS` > `Enable Version Control Integration`.
  - Select `Git` and click `OK`.
  - Use the `Commit` and `Push` buttons in the toolbar to manage your commits and push them to the repository.

With these steps, you should be able to run and develop your project in PyCharm effectively.

## Production Deployment

To deploy your application on Heroku, follow the steps below:

1. **Create a Heroku Account:**
   - Visit the [Heroku](https://signup.heroku.com/login) website.
   - Sign up for a free account or log in if you already have one.

2. **Create a New Heroku App:**
   - Once you are logged in to your Heroku account, click on the "New" button and select "Create new app".
   - Choose a unique name for your app. This name will be used in the App's URL.
   - Select the region closest to your location for better performance.

3. **Connect the App to Your Git Repository:**
   - After creating the app, go to the "Deploy" tab in your app's dashboard.
   - Choose the deployment method based on your Git repository: (e.g. GitHub).
   - Connect your app to the appropriate repository and branch.

4. **Configure Environment Variables:**
   - In the "Settings" tab of your Heroku app's dashboard, locate the "Config Vars" section.
   - Set the necessary environment variables required for your application.
   - Click on the "Reveal Config Vars" button to add the key-value pairs for your environment variables:

     | **KEY**               | **VALUE**          |
     |-----------------------|--------------------|
     | DATABASE_URL          | `<YOUR_VALUE>`     |
     | AWS_SECRET_ACCESS_KEY | `<YOUR_VALUE>`     |
     | AWS_ACCESS_KEY_ID     | `<YOUR_VALUE>`     |
     | USE_AWS               | `True`             |
     | EMAIL_HOST_PASS       | `<YOUR_VALUE>`     |
     | EMAIL_HOST_USER       | `<YOUR_VALUE>`     |
     | SECRET_KEY            | `<YOUR_VALUE>`     |
     | STRIPE_PUBLIC_KEY     | `<YOUR_VALUE>`     |
     | STRIPE_SECRET_KEY     | `<YOUR_VALUE>`     |
     | STRIPE_WH_SECRET      | `<YOUR_VALUE>`     |
     | COLLECT_STATIC        | `1`                |

5. **Deploy the Application:**
   - In the "Deploy" tab, scroll down to the "Manual Deploy" section.
   - Click on the "Deploy Branch" button to deploy your application.
   - Heroku will start building and deploying your application based on the code from your connected Git repository.

6. **Monitor the Deployment:**
   - Once the deployment process is complete, you can view the deployment logs to ensure everything is working correctly.
   - In the "Activity" tab, you will find the deployment logs, which can help you identify any issues or errors that may have occurred during the deployment process.

7. **Access Your Deployed Application:**
   - After a successful deployment, you can access your application by visiting the URL provided in your Heroku app's dashboard.
   - Click on the "Open App" button or open the URL in a web browser to see your application live.

## Credits
Throughout the process of building the PowerProtein website, I would like to acknowledge the following:

**Online Sources:**
- [Code Institue Template](https://github.com/Code-Institute-Org/ci-full-template)
- [Stack Overflow](https://stackoverflow.co/)
- [Django Documentation](https://docs.djangoproject.com/en/4.2/)
- [MDN Web Docs](https://developer.mozilla.org/en-US/)

**Modules and Libraries:**
- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [JavaScript](https://www.javascript.com/)
- [Font Awesome](https://fontawesome.com/)
- [jQuery](https://jquery.com/)
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
- [Django allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
- [AWS](https://aws.amazon.com/)
- [Stripe](https://stripe.com/ie)
- [Git](https://git-scm.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [Pexels](https://www.pexels.com/)
- [Markdown Best Practices](https://www.markdownguide.org/basic-syntax/)

## Content

- The blog post content was taken from here:
  - [Chef Lola's kitchen Amala Recipe](https://cheflolaskitchen.com/amala-recipe/)
## Media
- [FreePik](https://www.freepik.com/) - The Hero Images and the Allergen Images was gotten on freepik. 
- [Google Fonts](https://fonts.google.com/) - The fonts were sourced using Google Fonts.
- [Font Awesome](https://fontawesome.com/) - The icons was taken from Font Awesome.
- [Mermaid](https://mermaid.live/) - The diagrams was created with Mermaid website.
- [Google Images](https://www.google.com/imghp?hl=en) - Most of the products images & blog images was taken from google images. 

## Useful links
[Wade Williams](https://wadewilliams.com/software/generating-erd-for-django-applications/) - This was very useful to generate the ERD for the project.

## Acknowledgments

**Tutorials and Inspiration:**
- The walkthrough project 'Boutique Ado' from Code Institute, It helped me a lot to build the website and also gave me some new ideas to put on my website.  
- The Template for the GUI for this project was provided by [Code Institue Template](https://github.com/Code-Institute-Org/ci-full-template)

**People:**
- Malia Havlicek- Very sincere gratitude to my mentor for her guidance, support, and encouragement throughout the project.
- The Code Institute Slack for tips and guidance.
- My friends and family for their support and feedback.