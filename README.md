# Afri-Flavours Hub E-Commerce Website

## Overview

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
![output.png](..%2F..%2Foutput.png)
## Design Choices

Design Choices
Colour Scheme
The colour scheme includes earth tones that represent African landscapes, with green highlights to evoke freshness and nature.
![Color Palette.png](..%2F..%2F..%2FDownloads%2FColor%20Palette.png)
Typography
The primary font is 'Roboto', chosen for its readability and professional appearance across devices. Secondary font 'Montserrat' is used for headings to add character.

Imagery
High-quality images of the products and cultural symbols are used to entice customers and provide a visual representation of the blog content.

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
#### Forms
*  User registration, login, and checkout forms are designed to be intuitive and secure.
#### Database Operations
* CRUD operations for products, orders, blog posts, and comments.
#### Additional Features
* Blog integration where users can engage with content related to African food and culture.
* Responsive design ensures functionality across all devices.
### Future Feature Enhancements
* Implementation of a recipe upload feature for users.
* Advanced search functionalities for blog posts and products.
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