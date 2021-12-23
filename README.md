*A site to sell graphic design services built with the Django full stack MVC framework, Postgres, and Stripe. This application allows site owners to manage and sell products as well as receive requests for custom-built products.*

![ms3-screenshot](/static/images/ms4-screenshot.png)

Users can make use of this site to browse through various categories to find an illustration or rendering that they can purchase and download without shipping costs, purchase physical goods such as art prints, where shipping costs may apply, or request custom-built products. This Django project is part of the Code Institute's milestone project 4.

You can visit the page right [here!](https://codeinstitute-django-shop-ms4.herokuapp.com/)





### Table of Contents

- [Project](#project)
  - [Project Introduction](#project-introduction)
  - [User Story and Goals](#user-story-and-goals)
    - [External user's goal:](#external-users-goal)
    - [Site owner's goal:](#site-owners-goal)
- [Features](#features)
  - [Features Implemented](#features-implemented)
- [Design](#design)
  - [Database schema for user profile](#database-schema-for-user-profile)
  - [Database schema for categories and product](#database-schema-for-categories-and-product)
  - [Database schema for checkout](#database-schema-for-checkout)
  - [View of all tables created in Postgres](#view-of-all-tables-created-in-postgres)
  - [UX Design Choices](#ux-design-choices)
  - [Wireframes and Layout](#wireframes-and-layout)
    - [Homepage](#homepage)
    - [Catalog Page](#catalog-page)
    - [Cart Page](#cart-page)
    - [Checkout Page](#checkout-page)
    - [Order Review Page](#order-review-page)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
  - [Python Syntax Check](#python-syntax-check)
  - [HTML on W3C Validator](#html-on-w3c-validator)
  - [CSS on W3C Jigsaw Validator](#css-on-w3c-jigsaw-validator)
  - [JavaScript on JSHint ExtendsClass](#javascript-on-jshint-extendsclass)
  - [Performance Test with Lighthouse](#performance-test-with-lighthouse)
- [Issues and Bug fixes](#issues-and-bug-fixes)
  - [Known Issues](#known-issues)
  - [Never Do This](#never-do-this)
  - [A Bug Raised by Google Chrome](#a-bug-raised-by-google-chrome)
- [Django Deployment at Heroku](#django-deployment-at-heroku)
  - [Heroku Postgres Setup](#heroku-postgres-setup)
  - [Heroku Database Address](#heroku-database-address)
  - [Django Postgres Packages](#django-postgres-packages)
  - [Link to Heroku Postgres DB in Django Application](#link-to-heroku-postgres-db-in-django-application)
  - [Migrate Schema to Heroku Postgres Database](#migrate-schema-to-heroku-postgres-database)
  - [Import Data to Heroku Database](#import-data-to-heroku-database)
  - [Create Superuser](#create-superuser)
  - [Setup Database Choice Depending on Project Environment](#setup-database-choice-depending-on-project-environment)
  - [Web Server Setup](#web-server-setup)
  - [Procfile](#procfile)
  - [Heroku Temporary Hosting Settings](#heroku-temporary-hosting-settings)
  - [Setup Heroku Hostname](#setup-heroku-hostname)
  - [Git Commit](#git-commit)
  - [Deployment to Heroku with Git](#deployment-to-heroku-with-git)
  - [Test Heroku Site](#test-heroku-site)
  - [Heroku Automatic Deploy Settings](#heroku-automatic-deploy-settings)
  - [Create Secret Key](#create-secret-key)
  - [Set Secret Key in Settings](#set-secret-key-in-settings)
  - [Set Debug in Settings](#set-debug-in-settings)
  - [Git Commit and Automatic Deployment](#git-commit-and-automatic-deployment)
- [Deployment of Static Files on Amazon](#deployment-of-static-files-on-amazon)
  - [Create Account](#create-account)
  - [Find Storage S3 Service in the AWS Management Console](#find-storage-s3-service-in-the-aws-management-console)
  - [AWS Bucket Settings](#aws-bucket-settings)
  - [Properties](#properties)
  - [Permission and Policy](#permission-and-policy)
  - [Access Control](#access-control)
- [IAM - Identity and Access Management](#iam---identity-and-access-management)
  - [Create group](#create-group)
  - [Create policy](#create-policy)
  - [Attache Policy to Group](#attache-policy-to-group)
  - [Create User](#create-user)
- [Connect Django with AWS](#connect-django-with-aws)
  - [Install Dependencies for Django to Use AWS](#install-dependencies-for-django-to-use-aws)
  - [Register Django Storages in Django](#register-django-storages-in-django)
  - [Add Keys to Heroku](#add-keys-to-heroku)
  - [Set Custom Storage File](#set-custom-storage-file)
  - [Set Custom Storage in Django Settings](#set-custom-storage-in-django-settings)
  - [Commit to Update to Heroku](#commit-to-update-to-heroku)
  - [Check AWS S3 Bucket](#check-aws-s3-bucket)
  - [Adding Cache Expire Date](#adding-cache-expire-date)
  - [Upload Images to AWS S3](#upload-images-to-aws-s3)
- [Stripe Settings in Heroku](#stripe-settings-in-heroku)
  - [Adding Stripe Keys to Heroku](#adding-stripe-keys-to-heroku)
  - [Create New Stripe Webhook for Heroku](#create-new-stripe-webhook-for-heroku)
  - [Adding Stripe Signing Secret to Heroku](#adding-stripe-signing-secret-to-heroku)
  - [Test Stripe Webhook](#test-stripe-webhook)
- [Sending Emails](#sending-emails)
  - [Verify Superuser Email in Heroku](#verify-superuser-email-in-heroku)
  - [Gmail Configuration](#gmail-configuration)
  - [Setup Gmail Credentials in Heroku Settings](#setup-gmail-credentials-in-heroku-settings)
  - [Django Email Settings](#django-email-settings)
- [Deployment Summary](#deployment-summary)
  - [Test Payment](#test-payment)
  - [Test Email](#test-email)
- [Attribution and Credits](#attribution-and-credits)





---

## Project



### Project Introduction

As part of a student project at Code Institute, I chose to write a Code Institute inspired e-commerce application for graphic design services to apply and use Django, Postgres, HTML, CSS, and JavaScript. In addition to these technologies, I have used the UIkit library as well as some custom CSS where it was needed. In this application, users can view and purchase offerings from the site owner, search for particular products using keywords, and register an account to order and manage custom-built products or view their own order history.



### User Story and Goals

#### External user's goal: 

Users are able to browse, search, and purchase existing graphical designs or request custom-built products to address their needs. The user can fill out a form describing their needs, including fields such as type and format of the image, get an automatic quote, and then pay. If the user does not purchase the custom-built product, the custom product will be saved so that the user can come back later to further formulate the custom product and purchase the service when ready.

#### Site owner's goal:

The site owner can earn money by selling existing graphic designs in digital or physical form, as well as earning money for doing freelance design work. Logging in as a super user, the site owner can create and categorise new products. Information such as whether physical products need to be shipped out, or if custom orders require the site owner's skills to produce a custom product, is highlighted. Once the custom product is completed, the site owner can upload the image, making the image available to the user.

[back to top](#table-of-contents)





---

## Features



### Features Implemented

This site consists of a **landing page** to introduce the visitor to the site and its offerings, with a permanent **search bar** on top. 

A call to action button in the middle leads the user to the **catalog page** where all designs are loaded as **preview cards**. The catalog page has an additional menu that reflects all **product categories** in the database. By clicking on the different categories, the user can quickly grasp the content offered. 

Clicking on the card will lead the visitor to the **product detail page**, where the graphic design is presented in a larger image with information about the category, price, and description of the product. The user can click on the image to view the image in a **lightbox** to inspect the product without obstruction. The user can **choose the quantity** and choose to add the product to the cart. If the product is offered as a **physical product**, such as an art print, an **option to choose the print size** of the image will be presented. In addition, when the product is categorized as artwork, the **shipping cost will be calculated** for this category as well. Besides the "add to cart" button, another link to request custom artwork is presented, giving the user the option or hint of this graphic design service.

A **login** or **signup page** will be presented as a requirement if the user chooses to **request a custom artwork**. The user can then **choose the type** of the image, such as 3D rendering or hand-drawn illustration, and a format, such as book cover or digital image, which forms the basis to **calculate the custom product price**. A description field to describe the task or imagery, as well as an **image upload button**, gives the user the option to further describe the project. The **custom product** will be saved and the user can choose to **edit or delete** the product. Users are not obliged to purchase the product.

By **adding a product to the cart**, the product will be multiplied by the chosen quantity and saved in the bag. The bag view is straight-forward and offers the form and button to further adjust the quantity if needed.

In this assessment project, two **types of products** are considered: digital goods with no format and no delivery cost; and prints with various formats with delivery costs when the total is less than $50. If mixed goods such as digital goods and physical goods are bought together, the free shipping applies when the total is over $50. When visiting the project, you can click on the "Artwork" category where the prices are set to below $50 so that you can test this feature.

The checkout button in this view will lead the user to the **checkout** where the actual **payment form** and fields are required to be filled in with the user's information before the actual **payment with Stripe** can be initiated. Once the payment has been initiated, the payment will be evaluated. After successful evaluation, the user will receive a **success message** and the product will be saved for both the user and the site owner to review the order or **order history**. The user can review the order, see the **order invoice**, and have the option to **download** the product. If the user has created a custom product, the product is saved and editable in the **my custom product page**. The site owner can see and review all the purchased products on the **order review page** or log in to the Django admin area to do the same. Products such as physical products or custom-built **orders are highlighted** for the site owner to action the required tasks. Furthermore, the site owner can **see all custom products** created in the catalog view.

[back to top](#table-of-contents)



---

## Design



### Database schema for user profile

```bash
# UserProfile model

# UserProfile table
user = models.OneToOneField(User, on_delete=models.CASCADE)
default_phone_number = models.CharField(max_length=20, null=True, blank=True)
default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
default_county = models.CharField(max_length=80, null=True, blank=True)
default_postcode = models.CharField(max_length=20, null=True, blank=True)
default_country = CountryField(blank_label='Country', null=True, blank=True)

```



### Database schema for categories and product

```bash
# Product model

# Category table
name = models.CharField(max_length=254)
friendly_name = models.CharField(max_length=254, null=True, blank=True)

# Type table

name = models.CharField(max_length=254)
friendly_name = models.CharField(max_length=254, null=True, blank=True)

# Format table
name = models.CharField(max_length=254)
friendly_name = models.CharField(max_length=254, null=True, blank=True)


# Relationship to above Category, Type and Format in 'Product' table
category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
type = models.ForeignKey('Type', null=True, blank=True, on_delete=models.SET_NULL)
format = models.ForeignKey('Format', null=True, blank=True, on_delete=models.SET_NULL)

# Other fields in 'Product' table
sku = models.CharField(max_length=12, null=True, blank=True)
name = models.CharField(max_length=254)
created_by = models.CharField(max_length=50, null=True, blank=True)
description = models.TextField()
has_sizes = models.BooleanField(default=False, null=True, blank=True)
price = models.DecimalField(max_digits=6, decimal_places=2)
rating = models.IntegerField(null=True, blank=True)
image_url = models.URLField(max_length=1024, null=True, blank=True)
image = models.ImageField(null=True, blank=True)

```



### Database schema for checkout

```bash
# Checkout model

# Order table
# Relationship to UserProfile table
user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, 
                                 null=True, blank=True, related_name='orders')
# Other fields in Order table
order_number = models.CharField(max_length=32, null=False, editable=False)
full_name = models.CharField(max_length=50, null=False, blank=False)
email = models.EmailField(max_length=254, null=False, blank=False)
phone_number = models.CharField(max_length=20, null=False, blank=False)
country = CountryField(blank_label='Country *', null=False, blank=False)
postcode = models.CharField(max_length=20, null=True, blank=True)
town_or_city = models.CharField(max_length=40, null=False, blank=False)
street_address1 = models.CharField(max_length=80, null=False, blank=False)
street_address2 = models.CharField(max_length=80, null=True, blank=True)
county = models.CharField(max_length=80, null=True, blank=True)
date = models.DateTimeField(auto_now_add=True)
delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
original_bag = models.TextField(null=False, blank=False, default='')
stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')


# Orderline table
# Relationship to Order table above
order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
# Relationship to Product table
product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
# Other fields in Orderline table
product_size = models.CharField(max_length=20, null=True, blank=True)
quantity = models.IntegerField(null=False, blank=False, default=0)
lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

```



### View of all tables created in Postgres

Other then the tables declared above, the list includes the default Django tables, and the allauth tables created during the allauth setup.

```
                     List of relations
 Schema |             Name              | Type  |  Owner
--------+-------------------------------+-------+----------
 public | account_emailaddress          | table | theodorC
 public | account_emailconfirmation     | table | theodorC
 public | auth_group                    | table | theodorC
 public | auth_group_permissions        | table | theodorC
 public | auth_permission               | table | theodorC
 public | auth_user                     | table | theodorC
 public | auth_user_groups              | table | theodorC
 public | auth_user_user_permissions    | table | theodorC
 public | checkout_order                | table | theodorC
 public | checkout_orderlineitem        | table | theodorC
 public | django_admin_log              | table | theodorC
 public | django_content_type           | table | theodorC
 public | django_migrations             | table | theodorC
 public | django_session                | table | theodorC
 public | django_site                   | table | theodorC
 public | products_category             | table | theodorC
 public | products_format               | table | theodorC
 public | products_product              | table | theodorC
 public | products_type                 | table | theodorC
 public | profiles_userprofile          | table | theodorC
 public | socialaccount_socialaccount   | table | theodorC
 public | socialaccount_socialapp       | table | theodorC
 public | socialaccount_socialapp_sites | table | theodorC
 public | socialaccount_socialtoken     | table | theodorC
(24 rows)
```

[back to top](#table-of-contents)



---

### UX Design Choices

The navigation throughout this application is designed to be intuitive. To keep the design simple, the base colors are neutral and low-profile, while the product cards are designed to spark with their own aura and keep the eye busy and therefore focused on the content. To test or try something new, I chose to use the UIkit CSS library, as I have used Bootstrap and Materialized in previous milestone projects.

[back to top](#table-of-contents)





### Wireframes and Layout

The application layout is fairly simple and consists of the navigation bar, off-canvas menus for the mobile view, and a search bar. The catalog view is the highlight, where product cards are presented in a masonry layout with an additional category menu that users can use to click through the different categories offered.



#### Homepage

[image here]



#### Catalog Page

[image here]



#### Cart Page

[image here]



#### Checkout Page

[image here]



#### Order Review Page

[image here]



[back to top](#table-of-contents)





---

## Technologies Used



This project is written in **Python**, using the **Django** full stack MVC framework with **Jinja** and **HTML**, **CSS** and **JavaScript** with a small portion of **jQuery** for the **Stripe** payment setup and Django country fields. This project is built using the **Postgres** relational database. In addition to this stack, the **UIkit** framework is used extensively. All of the custom code is written with the **Visual Studio Code** editor on a personal **Mac computer** while the code is hosted on a **Linux** home server during development time. This project uses **Git** for version control and is stored as a public repository on **GitHub**. **Sketch** is used to create the wireframe layout as well as the images in this README file.

[back to top](#table-of-contents)





---

## Testing

---

### Python Syntax Check

All python code has been validated. This test has been conducted with the Python syntax checker [PEP8onlline](http://pep8online.com), as well as with the [Python Checker](https://pythonchecker.com).

```python
user_profile = models.ForeignKey(UserProfile, on_delete = models.SET_NULL, 
    null = True, blank = True, related_name = 'orders')

```

The output of both syntax checkers is very different, though. While the Python Checker gives a 100% signal for the above code, PEP8online raises multiple issues. In other cases, the results were similar or the other way around. Both validators agree on lengthly lines of code, but they do not agree on the number of empty lines above a function and whether to put white space around every operator or not.

[back to top](#table-of-contents)



---

### HTML on W3C Validator

The **HTML** code has been partially validated by the W3C validator. The reason for being partially validated is the mix of languages in the code that is in use, mainly HTML, Jinja, and UIkit. While it is OK for the W3C validator to read through the HTML parts, it makes error messages for the embedded Jinja parts as well as for some UIkit syntax. To validate if the HTML code is OK, I have to manually read through the report and assume that the code is OK as long as the raised errors are not about the HTML code.

In all three cases shown below the HTML validator throughs an error:

Example of UIkit syntax: `<div class="uk-grid-match" uk-grid>`

Example of embedded Jinja: `<link rel="stylesheet" href="{% static 'checkout/css/checkout.css' %}">`

Example of Jinja and UIkit: `<img data-src="{{ MEDIA_URL }}bg1.jpg" alt="img" uk-img>`

[back to top](#table-of-contents)



---

### CSS on W3C Jigsaw Validator

The **CSS** code has been validated by direct input in the [W3C Jigsaw validator](https://jigsaw.w3.org/css-validator/) and the respond of the validator has been positive for all 3 CSS files in this project. Congratulations! No Error Found.

[back to top](#table-of-contents)



---

### JavaScript on JSHint ExtendsClass

The **JavaScript** code has been validated by direct input on [JSHint](https://jshint.com/) as well as on [ExtendsClass](https://extendsclass.com/javascript-fiddle.html) and resulted in the following message for the stripe_elements.js file:

```
line	column	code	details
51	20	var html = `	'template literal syntax' is only available in ES6 (use 'esversion: 6').
133	28	var html = `	'template literal syntax' is only available in ES6 (use 'esversion: 6').
```

The complaints were mainly about the backticks used.

[back to top](#table-of-contents)



---

### Performance Test with Lighthouse

For this test, the hosted version of this application on Heroku.com is being used.




**Google Chrome's Developer Tools** are used extensively for debugging as well as the built-in **Lighthouse** project to test the performance of this application. The responsive design has been tested using **Google Chrome's responsive feature** that emulates the screen sizes of various mobile devices.

When the Lighthouse generated a report for the **desktop** view, it produced the following results in the following categories:

-   Performance: 21
-   Accessibility: 83
-   Best Practices: 80
-   SEO: 90

When the Lighthouse generated a report for the **mobile** view, it produced the following results in the following categories:

-   Performance: 26
-   Accessibility: 80
-   Best Practices: 80
-   SEO: 92

Lighthouse has raised the following two issues as the main factors for low performance:

Properly size images:
(4.6s) The low performance is explained as being due to the non-optimized image size provided, which takes the longest time to load.

Eliminate render-blocking resources:
(1.59s) The next performance issue are the non-optimised JS/CSS framework files.

[back to top](#table-of-contents)



---

## Issues and Bug fixes

Issues, bugs, and things I struggled with during the assignment project.

[back to top](#table-of-contents)



---

### Known Issues

When deleting a product from the products DB, the product will also be deleted in the users order history.

[back to top](#table-of-contents)



---

### Never Do This

*I had to re-install Django in the middle of this project because I deleted the migration files.*

At one point during development, I thought I needed to change the database schema for the products, which I did. And somehow, I thought, I could write the new schema in models.py, delete the old migration files, and migrate the new schema to the database.

And as usual, I would search rather than read the documentation and found this code to delete the old migration files in Django.

Warning, never do this!

```bash
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete 
find . -path "*/migrations/*.pyc"  -delete
```

After deleting the migration files, which I thought are old, I tried too migrate again and was confronted with this response in Terminal:

```bash
    from .migration import Migration, swappable_dependency  # NOQA
ModuleNotFoundError: No module named 'django.db.migrations.migration'
```

After some research I found this article:   https://newbedev.com/updating-django-error-no-module-named-migration

Your script appears to be the problem. It is trying to delete your migrations, but it's actually also deleting the contents of Django's `/django/db/migrations/` file as well. Note that it explicitly doesn't delete the `__init__.py` file but it does delete the others.

To solve this problem I had to re-install Django, migrate the schema, setup super user and upload all the content again. 

Here is how to:

```bash
# DON'T WORRY, REMEMBER YOUR PROJECT FILES ARE ALL THERE, JUST NOT THE MIGRATION FILES(!)

# Check your Django version
python3 -m django --version

# pip install --upgrade --force-reinstall package
pip install --upgrade --force-reinstall  Django==3.2.9

# Then makemigrations and migrate again 
python manage.py makemigrations
python3 manage.py migrate

# Create Super User with your credentials again
python3 manage.py createsuperuser

# Load your fixtures again
python3 manage.py loaddata categories
python3 manage.py loaddata types
python3 manage.py loaddata formats

# Load your other fixtures again
python3 manage.py loaddata products

# Link or upload images again
[...]
```

***A better way of doing this, is just do change whatever you need to change in your models.py file and migrate again. Django will pick up all changes within the migration files and connect to your DB just fine without deleting any migration files.***

[back to top](#table-of-contents)



---

### A Bug Raised by Google Chrome

```bash
(index):246 Uncaught TypeError: Cannot read properties of undefined (reading 'show')
```

This JavaScript code in **base.html** triggers the modal notification that appears in the browser whenever there is a message. As this code is recommended in the UIkit documentation and I could not find another way to trigger the notification or message, I will leave it as it is.

```html
<script>
  // Trigger uikit modal view for notifications
  UIkit.modal('#notification').show();
</script>
```

[back to top](#table-of-contents)



---

## Django Deployment at Heroku

A step by step guide to deploy this Django application on Heroku with Postgres as relational database, AWS S3 for storage, Stripe as payment system and Gmail as SMTP server.

The repository of this project is stored on **GitHub** and the site is deployed at **Heroku**. 
Please visit the project website by clicking [here!](https://codeinstitute-django-shop-ms4.herokuapp.com/)



---

### Heroku Postgres Setup

Create a Heroku app.

1)   Login to your Heroku account.
2)   Create new app by clicking "New" and "Create new app".
3)   Enter a project name, and choose the region closest to you.
4)   Then hit the create button.
5)   After that you will be in the project panel with different menu tabs on the top.
6)   Click on the resources tab.
7)   Then under Add-ons, in the search field, enter "postgres" and choose "Heroku Postgres".
8)   And choose the "Hobby Dev - Free" plan for this project and hit the "submit" or provision button.

[back to top](#table-of-contents)



---

### Heroku Database Address

Get the configuration for the Postgres database at Heroku.com.

1)   In your Heroku panel, go to the Settings tab.
2)   Then find the "Config Vars" section and click on "Show Config Vars" button.
3)   Copy the provided  `DATABASE_URL`  address.

It should look like this:

```bash
postgres://zkniszpedpbpwp:5688ebd0d8749c54b2820d97a21d52ac75a70f0431e47c471c236facf2c1a2f4@ec2-63-32-12-208.eu-west-1.compute.amazonaws.com:5432/d452d01fij3i38

```

[back to top](#table-of-contents)



---

### Django Postgres Packages

To use Postgres database in the Django project, we need to install the following packages:

-   dj_database_url
-   psycopg2-binary

In your Terminal, go to your project root folder and if you're using Python Virtual Environment, activate it. 

```bash
# Activate your Python Virtual Environment if you work in a Linux environment
# You can skip this step if you're using GitPod
source <your-environment>/bin/activate

# Then install the packages
pip3 install dj_database_url
pip3 install psycopg2-binary

# And export requirements.txt so that Heroku knows what to install during deployment
pip3 freeze --local > requirements.txt

```

Your requirements.txt file should have the two packages that we just installed and look similar to this:

```bash
asgiref==3.4.1
certifi==2021.10.8
charset-normalizer==2.0.7
defusedxml==0.7.1
dj-database-url==0.5.0  # <--- database-url package
Django==3.2.8
django-allauth==0.41.0
django-countries==7.2.1
django-crispy-forms==1.13.0
idna==3.3
oauthlib==3.1.1
Pillow==8.4.0
psycopg2-binary==2.9.2  # <--- psycopg2 package
python-dotenv==0.19.2
python3-openid==3.2.0
pytz==2021.3
requests==2.26.0
requests-oauthlib==1.3.0
sqlparse==0.4.2
stripe==2.62.0
urllib3==1.26.7

```

[back to top](#table-of-contents)



---

### Link to Heroku Postgres DB in Django Application

First import Django database url package in **settings.py** that we have installed in above step.

```python
# Import dj_database_url at top of your settings.py file
import dj_database_url

```



Find the "DATABASES" variable in settings.py and make the following changes:

```python
# Comment out the default configuration.
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

```



And set new "DATABASES" variabe using the dj_database_url library.

```bash
# Replace the default database above with a call to dj_database_url.parse
DATABASES = {
    'default': dj_database_url.parse('')
}

```



Then update the Database information with the new DATABASE_URL from previous step:

"Heroku Database Address"

You can paste in the "Heroku Database Address" between the quotes in the parse('') function like this:

```bash
# Paste in the database URL from Heroku that you have saved in previous step.
DATABASES = {
    'default': dj_database_url.parse('postgres://zkniszpedpbpwp:5688ebd0d8749c54b2820d97a21d52ac75a70f0431e47c471c236facf2c1a2f4@ec2-63-32-12-208.eu-west-1.compute.amazonaws.com:5432/d452d01fij3i38')
}

```



Once you save this new setting, your Terminal should output the following message:

```bash
# Output in Terminal
You have 32 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): account, admin, auth, checkout, contenttypes, products, profiles, sessions, sites, socialaccount.
Run 'python manage.py migrate' to apply them.

```

With the steps above you connected to the Postgres database at Heroku from your Django project. As the database is empty we will port our schemas to the new database in the next step.

[back to top](#table-of-contents)



---

### Migrate Schema to Heroku Postgres Database

To see what schemas Django will install in the new database at Heroku, use the `showmigrations` command.

In your Terminal:

```bash
# Show all migrations
python3 manage.py showmigrations

```



The output should look like this:

```bash
# Output
account
 [ ] 0001_initial
 [ ] 0002_email_max_length
 [ ] 0003_auto_20211115_1319
admin
 [ ] 0001_initial
 [ ] 0002_logentry_remove_auto_add
 [ ] 0003_logentry_add_action_flag_choices
auth
 [ ] 0001_initial
 [ ] 0002_alter_permission_name_max_length
 [ ] 0003_alter_user_email_max_length
 [ ] 0004_alter_user_username_opts
 [ ] 0005_alter_user_last_login_null
 [ ] 0006_require_contenttypes_0002
 [ ] 0007_alter_validators_add_error_messages
 [ ] 0008_alter_user_username_max_length
 [ ] 0009_alter_user_last_name_max_length
 [ ] 0010_alter_group_name_max_length
 [ ] 0011_update_proxy_permissions
 [ ] 0012_alter_user_first_name_max_length
bag
 (no migrations)
checkout
 [ ] 0001_initial
 [ ] 0002_auto_20211115_1319
 [ ] 0003_alter_order_country
 [ ] 0004_order_user_profile
contenttypes
 [ ] 0001_initial
 [ ] 0002_remove_content_type_name
home
 (no migrations)
products
 [ ] 0001_initial
 [ ] 0002_auto_20211107_1142
profiles
 [ ] 0001_initial
sessions
 [ ] 0001_initial
sites
 [ ] 0001_initial
 [ ] 0002_alter_domain_unique
socialaccount
 [ ] 0001_initial
 [ ] 0002_token_max_lengths
 [ ] 0003_extra_data_default_dict
 [ ] 0004_auto_20211115_1319
```



Migrate schemas to new Postgres DB at Heroku:

```bash
# Migrate schemas to db
python3 manage.py migrate

```

[back to top](#table-of-contents)



---

### Import Data to Heroku Database

Now that the database structure is in place we can import the actual data. 
I prepared and used fixtures during development and can import them now again to the new database.

In your Terminal:

```bash
# It's important to load them in the following order because the products
# depend on the categories, types and formats already existing.

# Load categories.json file
python3 manage.py loaddata categories

# Output
Installed 8 object(s) from 1 fixture(s)

# Load types.json file
python3 manage.py loaddata types

# Output
Installed 4 object(s) from 1 fixture(s)

# Load formats.json file
python3 manage.py loaddata formats

# Output
Installed 11 object(s) from 1 fixture(s)

# And then do the same for products.json file
python3 manage.py loaddata products

# Output:
Installed 43 object(s) from 1 fixture(s)

```

[back to top](#table-of-contents)



---

### Create Superuser

After importing the data we are ready to setup up a super user for this project.

```bash
# Setup super user to log in with
python3 manage.py createsuperuser

# And enter your credentials
Enter username: <yourusername>
Enter email: <youremail>
Enter password: <yourpassword>
Enter password (again): <yourpassword>

```

[back to top](#table-of-contents)



---

### Setup Database Choice Depending on Project Environment

Setting up Django application to use both databases, depending on the environment of the application such as Heroku or our local environment. For this we can use a simple "if" statement in the **settings.py** file and apply the following logic:

If `'DATABASE_URL'` exist, use the `os.environ.get('DATABASE_URL')` - which is the database at Heroku.

If not use `DATABASES` variable - which is our local database.

```python
# Required import of 'os'
import os


# [...]


# Then find the DATABASES variable that we have modified in previous step
# and make the following changes

if 'DATABASE_URL' in os.environ:
    # Use new Postgres database at Heroku
    # Here we can replace the lengthly address link with (os.environ.get('DATABASE_URL'))
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    # Use local Postgres database
    # Here I'm using variables that are stored in a '.env' file
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'project_ms4',
        'USER': os.getenv('POSTGRES_USER', ''),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', ''),
        'HOST': 'localhost',
        'PORT': '5433',
        }
    }


# [...]
```

The .env file stores all the credentials and is listed in the **.gitignore** file.



If you used sqlite3 before or would like to use sqlite3 in your new setting the new database setting would look like this:

```python
if 'DATABASE_URL' in os.environ:
    # Use new Postgres database at Heroku
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    # Use local sqlite3 database
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

```

Once saved, your application should work as before, using your local database. And when we upload the application to Heroku.com it should use the Heroku provided database that we have setup earlier.

[back to top](#table-of-contents)



---

### Web Server Setup

Install Gunicorn, which will act as our webserver.

In your Terminal and in your project root folder, run the following commands to install Gunicorn and update your requirements.txt file.

```bash
# Install Gunicorn web server
pip3 install gunicorn

# Export requirements.txt
pip3 freeze > requirements.txt
```

[back to top](#table-of-contents)



---

### Procfile

Setup a Procfile to let Gunicorn know which initial file to use to run the Django application.

In your Terminal and in your project root folder, run the following commands:

```bash
# Create Procfile in Django project folder
sudo touch Procfile
```



Tell Heroku to create a web dyno, which will run unicorn and serve our django app.

```bash
# Tell Gunicorn and Heroku which file to use
web: gunicorn <project_main_file>.wsgi:application

# Example
web: gunicorn project_main.wsgi:application
```

[back to top](#table-of-contents)



---

### Heroku Temporary Hosting Settings

As we want to use Amazon ASW S3 storage to serve our static files such as JS/CSS and images, we can prevent Heroku from collecting static files first, and revert back once our ASW S3 storage is ready to go.

To do this we need to disable the 'COLLECTSTATIC' setting in Heroku using the boolean setting 'DISABLE_COLLECTSTATIC = 1' provided by Heroku. 

Before you can go the following steps you need to have the **Heroku CLI** installed.
Here is a link on how to install the Heroku CLI:
https://devcenter.heroku.com/articles/heroku-cli#download-and-install

Once you have Heroku CLI in your system, we can login to Heroku via Terminal:

```bash
# Login to Heroku via Terminal
heroku login -i
# or 
Heroku login

# Enter your Heroku credentials
email:
password:

# Check all available apps on Heroku
heroku apps

# Disable collectstatic for specific app
heroku config:set DISABLE_COLLECTSTATIC=1 --app codeinstitute-django-shop-ms4

# Output:
Setting DISABLE_COLLECTSTATIC and restarting ⬢ codeinstitute-django-shop-ms4... done, v5
DISABLE_COLLECTSTATIC: 1

```

[back to top](#table-of-contents)



---

### Setup Heroku Hostname

To serve the Django application we need to register the ip-address in the Django settings.py file.

You can find your Heroku hostname in Heroku project panel under Settings tab > Domains:

https://codeinstitute-django-shop-ms4.herokuapp.com/

then trim the address to the following:

`codeinstitute-django-shop-ms4.herokuapp.com`



The "ALLOWED_HOSTS" list can have multiple addresses, allowing you to have different hostnames for different environments such as localhost for GitPod.

In the settings.py file of your project find the "ALLOWED_HOSTS" variable and paste in the address you have copied and trimmed above:

```python
ALLOWED_HOSTS = ['codeinstitute-django-shop-ms4.herokuapp.com', '127.0.0.1', 'localhost', '192.168.1.3']

```

[back to top](#table-of-contents)



---

### Git Commit

Having setup all the new settings above, now its a good time to commit your changes to git.

```bash
git add .
git commit -m "New Heroku deployment settings"
git push -u origin master
```

[back to top](#table-of-contents)



---

### Deployment to Heroku with Git

After setting up the new database and having the basic settings for deployment in the Django application we can deploy to Heroku.

Go to your Heroku application panel.

1.   Find the "Deploy" tab in the Heroku project panel.

2.   Find the "Deploy using Heroku Git" section.

3.   And copy command and execute it in your project root folder in Terminal:

```bash
# Login to Heroku via Terminal
heroku login -i

# Enter your Heroku credentials
email:
password:

# Tell Heroku which application to use
heroku git:remote -a codeinstitute-django-shop-ms4

# Output
set git remote heroku to https://git.heroku.com/codeinstitute-django-shop-ms4.git

# Push (deploy) to Heroku project git
git push heroku master
```

So our app is deployed, but **without any static files**, which we are going to setup in the next few steps.

[back to top](#table-of-contents)



---

### Test Heroku Site

After you have deployed the Django project to Heroku, let's test if the site loads.

In the Heroku project panel :

1.   Go to "Settings" tab.

2.   Then find "Domains" section .

3.   Copy the URL address and paste it into your browsers address bar.

https://codeinstitute-django-shop-ms4.herokuapp.com/

[back to top](#table-of-contents)



---

### Heroku Automatic Deploy Settings

We can make use of the Heroku automatic deploy setting, which will automatically deploy all changes that we push to our Git repository.

1)   Go to Heroku project panel.

2.   Then click on "Deploy" tab.

3.   Find the "Deployment method" section and click on "GitHub Connect to GitHub" button.

4.   Then search for the repository name: shop-ado-tutorial.

5.   And click "Connect".

6.   Then under the "Automatic deploys" section, click on "Enable Automatic Deploys".

**And now every time we push to github.**
**Our code will automatically be deployed to Heroku as well.**

You can test it by commiting any changes to GitHub or with the next step below.

[back to top](#table-of-contents)



---

### Create Secret Key

Get and set new secret key for our Heroku deployment.

1.   First we need a secret key and we can find one online that generates a key for us. 
     I'm using the following but you can really use any Django secret key generator: https://djecrety.ir/

The secret key you will get looks similar to this:

```bash
l!o^4t=uv1^$pw(+rfan@szi_*v#l5jts58#&q5)mnftb_cwpq
```

2.   Then go to the "Settings" tab in the Heroku project panel.

3.   Under the "Config Vars" section, click on "Reveal Config Vars".

4.   Then enter this text on the left text field: SECRET_KEY.

5.   and your newly created secret_key on the right text field.

6.   and click on the "Add" button.

This will be the secret-key for the Django application at Heroku. 
To use it in our application we have to setup the key in settings.py.

[back to top](#table-of-contents)



---

### Set Secret Key in Settings

Now we can set the secret-key in the Django **settings.py** file.

Find the 'SECRET_KEY' variable in the Django settings.py file and make the following changes:

```python
# Change this 
SECRET_KEY = 'django-insecure-!tso84risnw0d(h*v)ep#4yq$^0@xiat&@5f5pud@$o7v%qds)'

# to
SECRET_KEY = os.environ.get('SECRET_KEY', '')

```

After this setup the default 'django-insecure' key is no longer used and the 'SECRET_KEY' at Heroku will be used. As for your local environment you can setup another secret-key. I've setup another secret key for the local environment that is stored in a '.env' file which is listed in the **.gitignore** file.

 [back to top](#table-of-contents)



---

### Set Debug in Settings

Instead of having DEBUG set to "True" in the Django **settings.py** file, we're going to set it to 'DEVELOPMENT' so that we don't see all the debug messages in the browser.

```python
# Set DEBUG to 'DEVELOPMENT'
DEBUG = 'DEVELOPMENT' in os.environ

```

[back to top](#table-of-contents)



---

### Git Commit and Automatic Deployment

After setting up the secret key, we can commit our code and push it to the Git repository again. And while doing so, we can check in the Heroku panel under the "Activity" tab that there's a build in progress and our automatic deployments are working.

[back to top](#table-of-contents)



---

## Deployment of Static Files on Amazon

All static files for this project, such as JavaScript, CSS, and media files, are stored and served by Amazon S3, which is a cloud-based storage service by Amazon. To deploy static files to the Amazon Web Services, we need to setup an account and go through several steps to setup policies and permissions that Amazon needs to have in place, before allowing us to use Amazon's infrastructure.

[back to top](#table-of-contents)



---

### Create Account

To setup an account, go to:   https://aws.amazon.com

You will be asked to enter a credit card number which will be used for billing, in case we go above the free usage limits.

[back to top](#table-of-contents)



---

### Find Storage S3 Service in the AWS Management Console

Once you're in the Amazon S3 panel:

1.   Click on the "**Create Bucket**" button.

2.   Give it a Bucket name:   **ci-boutique-ado-bucket**

3.   Then select a region that is closest to you:    EU (Ireland) eu-west-1

4.   The uncheck the "**Block all public access**" checkbox.

5.   And acknowledge that the bucket will be public.
     Since this bucket will need to be public in order to allow public access to our static files.

6.   With that done I'll click "**Create bucket**".

And our bucket is created: **Successfully created bucket "ci-boutique-ado-bucket"**.

[back to top](#table-of-contents)



---

### AWS Bucket Settings

Now click on the **bucket name** in the list of Buckets.



### Properties

1.   Then click on the "**Properties**" tab.

2.   And find the "**Static website hosting**" section (currently at the very bottom of the page).

3.   Then click on "**Edit**".

4.   Once in the static website hosting edit page, click on "**Enable**".

5.   Then leave the selection under "Hosting type" as "**Host a static website**".

6.   In the "Index document" text field enter: **index.html**.

7.   and in the "Error document - optional" text field enter: **error.html**.

8.   then click "**Save changes**".

[back to top](#table-of-contents)



---

### Permission and Policy

Now in the Permission tab need to make a few changes.

1.   Click on the "**Permission**" tab.

2.   Find the **CORS configuration** (currently at the very bottom of the file).

3.   Then click the "**Edit**" button.

4.   and paste in the following info and click the "**Save changes**" button.

```bash
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



5.   Then find the "Bucket policy" section and click the "**Edit**" button.

6.   Then inside the "Bucket policy" page, click on the "**Policy generator**" button.

7.   Once at the AWS Policy Generator page, in Step 1: Select Type of Policy: **S3 Bucket Policy**.

8.   At Step 2, in the Principal text field, enter an ***** (Asterix, star).

9.   And under Actions, choose: **GetObject**.

10.   Then in the previous browser tab (your browser) go to the "**Properties**" tab.

11.   And in the "**Bucket overview**" section find the "**Amazon Resource Name (ARN)**".

12.   That should look like this:   **arn:aws:s3:::ci-django-shop-ms4**.

13.   Copy the ARN and go back to the **AWS Policy Generator** in your browser.

14.   And paste the ARN in the Step 2, Amazon Resource Name (ARN) text field!

15.   Finally click on the "**Add Statement**" button.

16.   Then click on the next "**Generate Policy**" button.

17.   And copy the policy from the pop-up window.

      It should look like the following:

```bash
{
  "Id": "Policy1640069279955",
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "Stmt1640069274694",
      "Action": [
        "s3:GetObject"
      ],
      "Effect": "Allow",
      "Resource": "arn:aws:s3:::ci-django-shop-ms4",
      "Principal": "*"
    }
  ]
}
```



18.   Then go back to the previous browser tab in your browser.

19.   And click on the "**Permission**" tab, then find the "**Bucket policy**" section and click on the "**Edit**" button.

20.   And paste in the copy of the policy (!).

21.   Before clicking Save, because we want to allow access to all resources in this bucket.
      We can add a /* slash star here onto the end of the resource key.

```bash
{
  "Id": "Policy1637684662010",
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "Stmt1637684621288",
      "Action": [
        "s3:GetObject"
      ],
      "Effect": "Allow",
      "Resource": "arn:aws:s3:::ci-django-shop-ms4/*",
      "Principal": "*"
    }
  ]
}
```

22.   Then click "Save changes".

[back to top](#table-of-contents)



---

### Access Control

With the bucket policy in place and the new configuration setup, we now allow full access to all resources in this bucket.
And set the list objects permission for everyone under the Public Access section here.

1.   Go to the **Permission** tab.

2.   Find **Object Ownership**.

3.   Then choose **ACLs enabled**.

4.   And under **Object Ownership**, choose **Object writer** and click "Save changes".



Then we need to configure the access control.

1.   Again under the "Permission" tab, find the "Access control list (ACL)" section.

2.   Here, click the "Edit" button .

3.   Once in the edit page, under the "Everyone (public access)" section, click and activate "List" in the Objects column.

4.   Then check the "I understand the effects of these changes on my objects and buckets".

5.   Then click the "Save changes" button.

With that done our bucket is almost ready to start serving files.

[back to top](#table-of-contents)



---

## IAM - Identity and Access Management

Now we need to create a user to access the bucket we have set up above.
We can do this through another service called IAM which stands for Identity and Access Management.

First create a group for our user to live in.
Then create an access policy giving the group access to the S3 bucket we've created.
And assign the user to the group so that the user can use the policy to access all our files.

[back to top](#table-of-contents)



---

### Create group

Go back to the services menu and find and open IAM.

1.   Once in the IAM panel, in the left side menu, under Access management, click "User groups".

2.   Then click on the "Create group".

3.   And in the "User group name" in the text field, enter a name for the access group: manage-boutique-ado.

4.   Then click "Create group".



### Create policy

5.   Now back on the left side menu click on "Policies" and to add a access policy click on "Create Policy".

6.   Then go to the "JSON" tab, and on the upper right corner click on the "Import managed policy" link.

7.   Then search for "s3" in the search field and choose the "AmazonS3FullAccess" policy and click import.

```bash
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:*",
                "s3-object-lambda:*"
            ],
            "Resource": "*"
        }
    ]
}

```

We actually don't need to allow full access to everything, 
and only want to allow full access to our new bucket and everything within it.



8.   Get the **bucket ARN** from the bucket policy page in s3:   **arn:aws:s3:::ci-django-shop-ms4**
     And paste that in here as a list:

9.   One item is the bucket itself, and the /* adds another rule for all files/folders in the bucket.

```bash
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
                "arn:aws:s3:::ci-django-shop-ms4",
                "arn:aws:s3:::ci-django-shop-ms4/*"
            ]
        }
    ]
}
```

10.   Then click "Next: Tags" and click "Next: Review".

11.   And give it a name:   django-shop-ms4-group-policy.

12.   And description:   Access to S3 bucket for django-shop-ms4 static files.

13.   And click "Create policy".

14.   To confirm you should be able to see the success message: The policy **django-shop-ms4-group-policy** has been created.

[back to top](#table-of-contents)



---

### Attache Policy to Group

1.   On the left side menu, click on "User groups" and click on the group previously created: "manage-boutique-ado".

2.   then under the "Permissions" tab, on the right click on the "Add permissions" button and choose "Attach policies".

3.   Choose the previously created policy, and click "Add permissions".

[back to top](#table-of-contents)



---

### Create User

1.   On the left side menu, click on "Users" and then click on "Add users".

2.   And give it a user name:   boutique-ado-staticfiles-user.

3.   Then check the "Access key - Programmatic access".

4.   Then click the "Next: Permissions" button.

5.   Now, in the list "Add user to group" select the "manage-boutique-ado" group by clicking the checkbox.

6.   And click "Next: Tags" and click "Next: Review" and click "Create user" until you see the Success message.

7.   Now I'll download the CSV file which will contain this users access key and secret access key,
     which we'll use to authenticate them from our Django app.

**It's very important you download and save this CSV**
**Because once going through this process we can't download the CSV file again.**

[back to top](#table-of-contents)



---

## Connect Django with AWS

Now that we've created an S3 bucket and the appropriate user's groups and security policies for it.
We can finally connect Django to use this service.

[back to top](#table-of-contents)



---

### Install Dependencies for Django to Use AWS

We'll need to install two new packages:

-   boto3
-   django-storages

In your Django root directory use the following commands to install the packages:

```bash
# Install boto3
pip3 install boto3

# Install django-storages
pip3 install django-storages

# Freeze requirements
pip3 freeze > requirements.txt
```

[back to top](#table-of-contents)



---

### Register Django Storages in Django

To register the newly installed packages we add "storages" to our installed apps in **settings.py** so that Django knows about it.

Find the "INSTALLED_APPS" variable and add 'storages' as shown below.

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'home',
    'products',
    'bag',
    'checkout',
    'profiles',
    'crispy_forms',
    'storages',  # HERE
]

```



To connect Django to S3 we need to add some settings in **settings.py** to tell Heroku which bucket it should be communicating with.
And we'll only want to do this on Heroku. 

We can use an if statement to check if there's an environment variable called USE_AWS in the environment. 

Add the following code above the Stripe settings:

```python
# AWS bucket access
if 'USE_AWS' in os.environ:
    # Bucket config
    AWS_STORAGE_BUCKET_NAME = 'ci-django-shop-ms4'
    AWS_S3_REGION_NAME = 'eu-west-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    # We need to tell django where our static files will be coming from in production.
    # Which is going to be our bucket name.
    # .s3.amazonaws.com
    # And formatting this as an F string so that the bucket name from above
    # will be interpreted and added to generate the appropriate URL
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

```

>   It's very important you keep these two keys secret. Because if they end up in version control someone could use them to store or move data through your S3 bucket. And Amazon would bill your credit card for it.

[back to top](#table-of-contents)



---

### Add Keys to Heroku

Back at the Heroku project page:

1.   Go to "Settings" tab and then to the "Config Vars" section and click "Reveal Config Vars".

2.   Then add: AWS_ACCESS_KEY_ID, with the value:  show in the downloaded CSV.

3.   And the: AWS_SECRET_ACCESS_KEY, with the value:  show in the downloaded CSV.

4.   And the:  USE_AWS, with the value:  True.

5.   And DELETE the configuration: DISABLE_COLLECTSTATIC, with the value:  1 

Once we save these settings and commit these changes, Django will collectstatic files automatically and upload them to S3.

[back to top](#table-of-contents)



---

### Set Custom Storage File

In this step we set Django to use the S3 storage in production and store the static files whenever someone runs collectstatic.
And any uploaded product images should go the S3 storage as well.
Let's create a file called "custom_storages.py" to declare the above intentions.

```bash
# Create custom_storages.py file
sudo touch custom_storages.py

```

Then edit the file like so:

```python
# 1) Import settings from django.conf
from django.conf import settings
# 2) Import the s3boto3 storage class from django storages which we just installed.
from storages.backends.s3boto3 import S3Boto3Storage


# 3) Create a custom class called StaticStorage.
# Which will inherit the one from django storages. Giving it all its functionality.
# And tell it that we want to store static files in a location 
# from the settings that we'll define in the next step.
class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION

# 4) Create a custom class called MediaStorage.
class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION

```

[back to top](#table-of-contents)



---

### Set Custom Storage in Django Settings

-   Now in the **settings.py** file we can tell Django that for static file storage we want to use our storage class we just created.
-   And that the location it should save static files is a folder called static.
-   And then do the same thing for media files by using the default file storage.
-   And set the media files location.

```python
# AWS bucket access
# *s3) 
if 'USE_AWS' in os.environ:
    # Bucket config
    AWS_STORAGE_BUCKET_NAME = 'ci-django-shop-ms4'
    AWS_S3_REGION_NAME = 'eu-west-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'  # *s1)

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'  # *s2)
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'  # *s2)
    MEDIAFILES_LOCATION = 'media'
    
    # We also need to override and explicitly set the URLs for static and media files.
    # Using our custom domain and the new locations.
 
    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
    
    # SUMMARY
    # When our project is deployed to Heroku,
    # Heroku will run python3 manage.py collectstatic during the build process.
    # Which will search through all apps and project folders looking for static files.
    # And it will use the S3 custom domain setting here *s1) 
    # in conjunction with our custom storage classes that tell it the location at that URL here *s2).
    # Where we'd like to save things.
    # So in effect when the USE_AWS setting is true *s3)
    # And whenever collectstatic is run,
    # static files will be collected into a static folder in the S3 bucket.
    
```

[back to top](#table-of-contents)



---

### Commit to Update to Heroku

Now we can commit and push our changes to update the new settings in our Git repository and automatically update our application on Heroku as well. To see this process in action you can look at the "Activity" tab at Heroku.

And you can see that all the static files were collected successfully.

```bash
# Output of the build log in Heroku
-----> $ python manage.py collectstatic --noinput
       133 static files copied.

https://codeinstitute-django-shop-ms4.herokuapp.com/
```

[back to top](#table-of-contents)



---

### Check AWS S3 Bucket

If we go to the AWS S3 bucket that we have created, we can see we have a static folder in our bucket with all our static files in it.

[back to top](#table-of-contents)



---

### Adding Cache Expire Date

By adding some cache control settings, we can influence how long static files should be held in cache in the browser. For this project, we can set the expire date so that the static files are cached for a very long time, as we don't have much dynamic content that needs to be changed and this will improve performance for our users.

```python
# AWS bucket access
if 'USE_AWS' in os.environ:
  
    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    # Bucket config
    AWS_STORAGE_BUCKET_NAME = 'ci-django-shop-ms4'
    AWS_S3_REGION_NAME = 'eu-west-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

```

After this step, we can commit and push to the Git repository again to update Heroku.

[back to top](#table-of-contents)



---

### Upload Images to AWS S3

As a final step in setting up Django with AWS, we can now upload the images.

1.   Go to S3 "ci-django-shop-ms4" page.

2.   And click on "Create folder" to create a new folder called "media".

```bash
media/
static/
```

3.   Then click on the newly created "media" folder.

4.   Click on the "Upload" button, and then the "Add files" button, then add all images.

5.   Then under Permissions select "Grant public-read access", confirm your understanding and click "Upload".

Now the images are being uploaded which will take some time.

[back to top](#table-of-contents)



---

## Stripe Settings in Heroku



### Adding Stripe Keys to Heroku

In this section we're going to set the public and secret key from Stripe at Heroku.

1.   Log into your Stripe account.

2.   Clicking developers. And then API keys.

-   Get:   Publishable key

-   Get:   Secret key

3.   In Heroku, under the "Settings" tab, add them as **config variables**.

-   STRIPE_PUBLIC_KEY   --> and add the key value.

-   STRIPE_SECRET_KEY   --> and add the key value.

[back to top](#table-of-contents)



---

### Create New Stripe Webhook for Heroku

Now we need to create a new webhook endpoint in the Stripe developer panel, since the current one is sending webhooks to our development workspace.

1.   Go to webhooks in the developer's menu.
2.   Click on the "add endpoint" button.
3.   And add the URL for your Heroku application, followed by /checkout/wh/

```bash
https://codeinstitute-django-shop-ms4.herokuapp.com/checkout/wh/
```

4.   Then selecting receive all events and add endpoint.

5.   We can now reveal our webhooks signing secret in the Developers > Webhooks panel.

6.   Then find "Signing secret" and click the "unveal secret" link:

```bash
# Signing secret should look like this
whsec_Pyuv0AoSkH4hgtHkDaSExJO9ngxBq5VH

```

[back to top](#table-of-contents)



---

### Adding Stripe Signing Secret to Heroku

Now that we have the signing secret key we need to set the key in the Heroku Config Variables.

1.   Go to the "Settings" tab at Heroku.
2.   And click on the "Config Variables" button.
3.   Then add the signing secret with the parameters you retrieved from the Stripe page.

```bash
# And add that to our Heroku config variables.

# Key
STRIPE_WH_SECRET

# Value   
whsec_Pyuv0AoSkH4hgtHkDaSExJO9ngxBq5VH
```

**All these variables need to match what you've got in your settings.py.**
**If you've used different names, make sure to update them accordingly.**

[back to top](#table-of-contents)



---

### Test Stripe Webhook

Send a test webhook from stripe to make sure that our listener is working.

1.   In the Stripe Webhook panel click on "Send test event".

2.   Choose Event type:   account.external_account.created.

3.   Click "Send test webhook".

Response:

```
ResponseTest webhook sent successfully
Unhandled webhook received: account.external_account.created

```

[back to top](#table-of-contents)



---

## Sending Emails

The last step in our deployment efforts is to get the email going.



### Verify Superuser Email in Heroku

We have not yet logged in as super user because we have created a new database for the Django application on Heroku and must first verify the super user's email address. 

1.   Go to the Django admin page that is hosted on Heroku and login with your admin credentials:

https://codeinstitute-django-shop-ms4.herokuapp.com/admin/

2.   Then under Accounts, click on the "Email addresses" link.

3.   If you see your email then just click on it and check the "Verified" and "Primary" button then click "SAVE".

4.   If you do not see your email address, then something went missing along the way and you need to setup the email manually.

5.   In the search field, enter your/user name and find it in the pop up window by clicking on the user.

6.   Then type in the email address in the email field, and check the "Verified" and "Primary" button and click "SAVE".

[back to top](#table-of-contents)



---

### Gmail Configuration

For this project, I'm going to use Gmail as I already have a Gmail account, and Google offers a free SMTP server that we can use to send emails.

Setup Gmail 2-Step Verification:

This will allow us to create an app password specific to our Django app.
That will allow it to authenticate and use our Gmail account to send emails.

If you've already got a Gmail account you can just log in and **go to your settings**.
If you don't have one, just go to gmail.com and create an account before starting this.

1.   Go to Settings > Accounts and Import > Change account settings > Other Google Account settings.

2.   Then on the left side menu, and go to "Security", and find "Signing in to Google" > 2-Step Verification.
3.   To turn it on just click "get started", and enter your password.
4.   Then you'll have to "select" a verification method.

5.   You can choose any method you prefer.
6.   Once you've verified and turned on two-step verification, go back to Security and find "App password".
     Under the 2-Step Verification you see another "App passwords" button.

8.   Click "enter my password" again if needed.

9.   Then on the app password screen, I'll select **mail** for the app.

10.   Then under device type, I'll select **other** and type in **Django**, but you can enter any name here.

With that done we'll be given a 16 character password which we can copy.

```bash
# Now you should get a 16 character long password from Gmail similar to this
jrplrejcpaulwlyq
```

[back to top](#table-of-contents)



---

### Setup Gmail Credentials in Heroku Settings

1.   In the Heroku panel go to the "Settings" tab and click on the "Config Variables" button.
2.   Then enter the credentials that we have retrieved from Gmail.

Here we use the variable EMAIL_HOST_PASS and paste the value in the adjacent field:

```bash
# Key
EMAIL_HOST_PASS

# Value
jrplrejcpaulwlyq

```



We also need another variable here called EMAIL_HOST_USER, which will be set to your email:

```bash
# Key 
EMAIL_HOST_USER

# Value
youremail@email.com

```

[back to top](#table-of-contents)



---

### Django Email Settings

The last step then is just to add email settings to settings.py.

```python
[...]


# 1) Comment out current email setting and copy the code
# EMAIL_BACKEND by and required by allauth
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


[...]


# Then we create our own email logic:
# 2) 
# Check if development is in os.environ.
# Determine which email setup to use.
# If that variable is set, we'll log emails to the console.
# And the only setting we need to specify is the default from email.
# And that will be youremail@example.com

# 3) 
# Otherwise, for production at Heroku we'll need to set several variables.
# EMAIL_BACKEND, which will be set to django.core.mail.backends.smpt.EmailBackend
# EMAIL_USE_TLS, which will be true
# EMAIL_PORT, which will be port 587
# EMAIL_HOST, which will be smtp.gmail.com
# And then the username, password, and DEFAULT_FROM_EMAIL
# All of this will be obtained from Heroku's environment settings.


# 2) 
if 'DEVELOPMENT' in os.environ:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    DEFAULT_FROM_EMAIL = 'youremail@example.com'
# 3)
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
    DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')

```

With this complete, commit and push your code to your Git repository and deploy the settings to Heroku.
That was the last stage in the deployment process, and now we can check to see if everything is working properly.

[back to top](#table-of-contents)



---

## Deployment Summary



### Test Payment

After that, our e-commerce [store](https://codeinstitute-django-shop-ms4.herokuapp.com/) is live and available to anyone on the internet who wants to look at the products, create a profile, and check out with a fake credit card number.

Please use this test credit card number instead of your actual credit card number while testing the checkout:

```
# CARD NO            MM / YY  CVC  ZIP
4242 4242 4242 4242  04 / 24  242  42424
```

[back to top](#table-of-contents)



---

### Test Email

Please use a valid email address to test the email so that you receive a confirmation email in your inbox after signing up and can verify your account to login.

[back to top](#table-of-contents)



---

## Attribution and Credits

This project was started by the [Code Institute](https://codeinstitute.net/) to teach and mentor students on their way to becoming software developers. As this is the final milestone project, I'd like to express my gratitude to the Code Institute and team for providing this course.

A huge thank you to the Stack Overflow community in general, where I found a lot of answers to questions I had while working on this project.

A big thank you as well to the **Unsplash** community, where I got the images that you see on the site to make it bright and colourful.

[back to top](#table-of-contents)




