# Afri-Flavours Hub E-Commerce Website

## Overview
![logo](https://github.com/Nelkon01/afri_flavours/assets/54297166/7f0b5b2b-2777-425a-8139-91896aff7718)
Afri-Flavours Hub is a food e-commerce website developed using Django. It features user authentication, product management, a shopping cart, order processing, payment integration, a blog for sharing recipes and stories, and an admin dashboard for managing the website.

## Click [here](https://afri-flavours-0342f46728dc.herokuapp.com//) to live website.
## Table of Contents

<details>
<summary>Click to Expand</summary>

- [UX](#ux)
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

* 

|   | **FEATURES**                                                                                                                                    | **PRIORITY** |
|---|-------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| 1 | Implementing a feature that will allow users to favourite products for later with a wishlist,  ensuring they never miss out on products.        | LOW          |
| 2 | Implementing a live chat support system to provide instant assistance and answer queries.                                                   | HIGH         |
| 3 | Offer personalized discounts based on user preferences and purchasing behaviour.                                                                 | MEDIUM       |
| 4 | Introduce an Affiliate Program, allowing earning while users shop and refer others to our platform.                               | MEDIUM       |
| 5 | Support to cater to a wider user base, allowing users from different regions and language preferences to access and use the Afri-Flavours shop | HIGH         |
| 6 | Implementation of a recipe upload feature for users.                                                                                            | HIGH         |
| 7 | Advanced search functionalities for blog posts and products.                                                                                    | HIGH         |

### Technologies Used
#### Front-End Technologies
* HTML5
* CSS3
* JavaScript: Used for dynamic features like the shopping cart.
#### Back-End Technologies
* Django: The core framework for the application.
* PostgreSQL: For database management.
#### Deployment and Hosting
* Heroku: Platform for hosting the application.
#### Version Control and Collaboration
* Git: Used for version control.
* GitHub: Hosts the project repository and facilitates version tracking and collaboration.
#### Defensive Programming
* Implemented input validations to prevent SQL injection and cross-site scripting, error handling to manage unexpected failures.

### Testing
Includes automated tests written with Django's testing framework to ensure that all components of the application function as expected.

### Deployment
Includes detailed steps on setting up the environment, configuring databases, and deploying to Heroku.

### Acknowledgements
Thanks to all contributors, including the development team, project managers, and the community of users who provided valuable feedback.
