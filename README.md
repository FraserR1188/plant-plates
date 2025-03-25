# Plant Plates

## Milestone Project 3 - Backend Development

![Main Image README](plantplates/static/images/README/main-image-readme.png)

- The recipe website is aimed at age 12 onwards to enjoy to cook. The website should bring inspiration and enjoyment through cooking. It should also entice the visitor to prepare something that they did not intend. We want this to be a hub of activity and a place where users will store there recipes and allow other people to view them.
- This is my Milestone Project 3 submission for Code Institutes Diploma in Web Application Development Course. My website uses both relational and non-relational databases, features full CRUD functionality and is built using technologies that I have learnt including HTML, CSS, JavaScript, Python, Flask and PostgreSQL.

## Project Link

To access my website please click this [link](https://plant-plates-ebe9caba4f16.herokuapp.com/).

## Repository

To access to my repository please click [link](https://github.com/FraserR1188/plant-plates)

## Project Goals

This website is dedicated for people who love food and want to share there love for food. This also has a heavy influence from myself and my girlfriend as this is a dream we've always wanted, a website where we can express our creativity with food for everyone to enjoy. There will be a lot of recipes from ourselves but also recipes from other people who have uploaded them. There are also articles about food which people can read and create themselves.

There is an account page which will be the hub for the return user so they can store all their recipes and have somewhere to go back to.

# Table of Contents

## Contents

- [User Stories](#user-stories)
  - [First-time Users](#first-time-users)
  - [Returning Users](#returning-users)
  - [Website Owners](#website-owners)
- [Design](#design)
  - [Typography](#typograhy)
  - [Images](#images)
  - [Colour Scheme](#color-scheme)
  - [Wireframes](#wireframes)
- [Features](#features)
  - [All Page Features](#all-page-features)
    - [Navigation Bar](#navigation-bar)
    - [Footer](#footer)
    - [Modal Messages](#modal-messages)
  - [Home Page](#home-page)
    - [Hero Image](#hero-image)
    - [Website Values](#website-values)
    - [Recently Added](#recently-added)
    - [Plant Plates Logo](#plant-plates-logo)
    - [Story Behind The Website](#the-story-behind-the-website)
  - [Login Page](#login-page)
  - [Sign Up](#sign-up)
  - [Account Page](#account-page)
  - [Create a New Recipe Page](#create-a-new-recipe-page)
  - [Details of Recipe](#details-of-recipe)
  - [Edit Recipe](#edit-the-recipe)
  - [Delete The Recipe](#delete-the-recipe)
  - [My Recipes](#my-recipes)
  - [All Recipes](#all-recipes)
  - [Categories](#categories)
  - [Category Section](#category-section)
  - [Admin Categories](#admin-categories)
  - [Error Handling](#error-handling)
- [Future Features](#future-features)
- [Data Model](#data-model)
- [Technologies Used](#technologies-used)
  - [Languages Used](#languages-used)
  - [Framework Libraries and Programs](#frameworks-libraries-and-programs)
- [Testing](#testing)
- [Deployment](#deployment)
  - [Forking the GitHub Repository](#forking-the-github-repository)
  - [Making a Local Clone](#making-a-local-clone)
  - [Creating an application with Heroku](#creating-an-application-with-heroku)
- [Credits](#credits)
  - [Code](#code)
  - [Content](#content)
  - [Acknowledgements](#acknowledgements)

## User Stories

### First time Users

- As a first-time user, I want the website to be accessible on any device.
- As a first-time user, I want the website to be easy to navigate.
- As a first-time user, I want to sign-up quickly and easily.
- As a first-time user, I want find what recipe I want quickly and easily.

### Returning Users

- As a returning user, I want to be able to login easily on the homepage.
- As a returning user, I want to be able to create / read / edit / delete my own recipes.
- As a returning user, I want to see featured / trending recipes on the homepage.
- As a returning user, I want the website to be accessible on any device.
- As a returning user, I want the recipe layout to be in an organised list with an image referring to the dish.
- As a returning user, I would like to have access to social media links.
- As a returning user, I want the option to have an e-mail newsletter.
- As a returning user, I want to know more about the owners and their ethos.

### Website Owners

- As a website owner, I want to make the website homely and connected to it's returning users.
- As a website owner, I want to let all visitors know about the ethos behind the website.
- As a website owner, I want to be able to create /read / edit / delete cuisines and also give to
- As a website owner, I want the website to function on all devices and look appealing.

## Design

### Overview

We want the design to homely but modern with very sleek kitchen feel. This is a place for people who can cook and if they are on the site for long we want it to be aesthetically pleasing. The name of the website is "Plant Plates", we are vegan and this represents that. We've look at multiple popular websites to understand the design layout and how they use the space appropriately e.g. not too many images, easy to read writing.

### Colour

![Colour Scheme](plantplates/static/images/README/colour-scheme.png)

### Typography

The fonts which I have picked are Lora and Playfair Display. I will use Lora for main headings and buttons where as I'll use Playfair Display for paragraphing and longer pieces of text. Both of these fonts are different, easy to read and also quite elegant.

### Imagery

Since it is a recipe website, I'm going to keep most of the images centered around the food. Most images will be posted by the users through the creation of recipes. Articles can also have images which will be posted through the same way as recipes.

### Wireframes

#### Mobile Wireframe

![Mobile Wireframe](plantplates/static/images/README/mobile-wireframes.png)

#### Tablet Wireframe

![Tablet Wireframe](plantplates/static/images/README/tablet-wireframes.png)

#### Desktop Wireframe

![Desktop Wireframe](plantplates/static/images/README/desktop-wireframes.png)

# Features

## All Page Features

## Navigation Bar

![Before use has logged in on desktop and tablet](plantplates/static/images/README/tablet-desktop-navbar.png)

- This is what the nav bar looks like before the user has logged in on a desktop.

![Before user has logged in on mobile](plantplates/static/images/README/mobile-navbar.png)

- This is what the nav bar looks like before the user logs in on a mobile.
- This a burger menu which expands when touched.

![After nav bar desktop-tablet](plantplates/static/images/README/tablet-desktop-after-log-in.png)

![After nav bar mobile](plantplates/static/images/README/mobile-after-log-in.png)

- This is what the user has once logged in.

- I have also made myself an admin which has the ability to manage the catergories (CRUD). This is what the appearence looks:

![Mobile Admin](plantplates/static/images/README/mobile-admin-categories.png)
![Desktop Admin](plantplates/static/images/README/admin-categories.png)

- This has been hard coded into the route.py. I can add more admin users as and when but this seemed to be the best option at the moment.

## Footer

![Footer](plantplates/static/images/README/footer.png)

- The footer is present through the website and stays the same with the social media icons.

## Modal Messages

- I felt like the modal messages were a nice interactive touch to the website. This was instant gratification of knowing when the user has logged out or logged in. As mentioned below the message only lasts 2 seconds so it shouldn't interfer with the users fluidity of going through the website.

![Logged In Modal](plantplates/static/images/README/logged-in-modal.png)

- User sees this when logged in for 2 seconds.

![Logged Out Modal](plantplates/static/images/README/logged-out-modal.png)

- User sees this when logging out for 2 seconds

# Home Page

## Hero Image

![Homepage Hero Image](plantplates/static/images/README/home-hero-image.png)

- This is situated right underneath the nav-bar with the title of the website within it and an indication of what the website is about.
- I liked the transparency of the image and allowing the writing to come through.

## Website Values

![Website Values](plantplates/static/images/README/home-what-the-site-is.png)

- These are the values of the website.
- I have different coloured font to increase the contrast ratio to enable easier reading.

## Recently Added

![Recently Added](plantplates/static/images/README/latest-greatest.png)

- These are the most recently added recipes to the website. Everyone can see these, the user doesn't have to be logged in. Maximum of 4 will be shown.

## Plant Plates Logo

![Plant Plates Image](plantplates/static/images/README/home-parrallex.png)

- This is the parallex which utilises Materilezes JavaScript Parallex feature.

## The story behind the website

![Our Story](plantplates/static/images/README/home-story.png)

- This section is about the website owners and their aim through the website.

## Login Page

![Login Page](plantplates/static/images/README/login-page.png)

- This is the login page

## Sign Up

![Sign Up](plantplates/static/images/README/sign-up-page.png)

- This is the sign up pge which has a link to the login page incase the user already has an account.

## Account Page

![Account Page](plantplates/static/images/README/account-page.png)

- Once the user has logged in, they are transport to their account page straight. This is to invigerate the user into posting recipes onto the website.

## Create a New Recipe Page

![Create Page](plantplates/static/images/README/create-recipe-page.png)

- The create a new recipe page has 9 input fields, one being an upload image section which uses AWS for image upload.

- This has been designed to be as user friendly as possible.

- The input fields include:

  - Recipe Title (required max length 255 characters)
  - Image (not required - max length 500 characters)
  - Seasonal (not required)
  - Total Time (not required - number)
  - Yield (not required - number)
  - Ingredients (required - text - new line seperated)
  - Calories (not required - number)
  - Steps To Prepare (required - text - new line seperated)
  - Summary (not required - text)

- I chose the inputting method of having everything seperated by a new line

## Details of Recipe

![Detail Recipe](plantplates/static/images/README/recipe-detail.png)

- This is the what the recipe looks like once created on the users profile.
- Ingrediants are shown in an unordered list.
- Steps are shown in an ordered list.

## Edit the Recipe

![Edit Recipe](plantplates/static/images/README/edit-recipe.png)

- This is the edit/update view of a recipe.

## Delete the Recipe

![Delete Recipe](plantplates/static/images/README/confirm-deletion.png)

- This is the modal in which we can delete a recipe.

## My Recipes

![My Recipe Page](plantplates/static/images/README/my-recipe-page.png)

- This is the where the user stores there own recipes.

## All Recipes

![All recipes](plantplates/static/images/README/all-recipes.png)

- This page is where everyone, including the user, can access all the recipes created.

## Categories

![Home Page Categories](plantplates/static/images/README/categories-page.png)

- This is the main page for all the categories which are present at the moment

## Category Section

![Category Section](plantplates/static/images/README/category-section.png)

- This is how the recipes are presented in the category section

![No Recipes](plantplates/static/images/README/no-category-present.png)

- This is how it looks when no recipes are present.

## Admin Categories

- Only myself can see these pages. I felt that admin having the only rights to accessing categories was safer and maintained the website better.
- I can add more users to be admins but I have hard coded the email into the script.

![Admin Categories](plantplates/static/images/README/admin-manage-categories.png)

- This how the admin can edit or delete categories

![Confirm Detele Cateogry](plantplates/static/images/README/confirm-delete-category.png)

- Defensive programming, making sure there is a confirmation delete modal.

![Edit Category](plantplates/static/images/README/edit-category.png)

- This how it looks to edit a category.

![Add Category](plantplates/static/images/README/add-category.png)

## Error Handling

### Login Error

![Login Error](plantplates/static/images/README/login-error.png)

- This appears if the user inputs invalid information.

![Sign Up Error](plantplates/static/images/README/sign-up-error.png)

- This appears if the user tries to sign up again.

# Future Features

### Articles

- I have made the modules for users to create Articles and discuss about food topics

### Leaving Reviews

- Allow users to comment on recipes, offer cooking tips, suggest ingredient substitutions, or ask questions directly on recipe pages.
- Enable recipe authors to respond to user questions and comments.

### Ratings

- Users can rate recipes using a 5-star rating system.
- Display average ratings prominently to help visitors choose popular or highly-rated recipes.

### Enhanced User Profiles

- Users can add profile pictures, biographies, favorite cuisine types, dietary preferences (e.g., gluten-free, nut-free), and cooking skill level.
- Showcase each user's contributed recipes and articles in their profile.

### Meal Planner and Grocery List Generator

- Users can plan their weekly meals directly on the site by selecting recipes.
- Automatically generate grocery shopping lists based on planned meals, with printable or downloadable PDF options.

### Nutrition Information and Calculators

- Automatically calculate nutritional data for recipes, including calories, macros (protein, carbs, fats), and vitamins, to help health-conscious users.

### Cooking Mode

- A full-screen, step-by-step cooking mode that simplifies recipe viewing and includes timers and interactive checklists for ingredients and steps.

### E-mail Newsletter

- An e-mail to be sent out with the latest recipes.

# Data Model

[View my Database structure here](plantplates/static/images/README/database-management.png)

# Technologies Used

## Languages Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)

- [CSS3](https://en.wikipedia.org/wiki/CSS)

- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)

- [Python](<https://en.wikipedia.org/wiki/Python_(programming_language)>)

## Frameworks Libraries and Programs

- [Heroku](https://id.heroku.com/login)

  - Heroku is the deployment source I used for this project. I'm also using it for the Postgres relational database

- [Flask](https://flask.palletsprojects.com/en/2.2.x/templating/)

  - Templating language I've used with Python to add logic to my html templates.

- [Jinja](https://jinja.palletsprojects.com/en/3.0.x/)

  - Templating language I've used with Python to add logic to my html templates.

- [Materialize CSS](https://materializecss.com/)

  - Front-end library with HTML, CSS and Javascript based componants. I used features including Nav bar, Cards, Buttons and Forms.

- [Google Fonts](https://fonts.google.com/)

  - Two fonts are imported from google fonts.

- [Font awesome](https://fontawesome.com/)

  - I used icons from font awesome on social media icons on the footer.

- [Git](https://git-scm.com/)

  - Git was used as a version control in the terminal.

- [Github](https://github.com/)

  - Github was used to create and store the project repository.

- [WebFormatter](https://webformatter.com/html)

  - WebFormatter was used to help beautify the code.

- [Google Chrome Dev Tools](https://developer.chrome.com/docs/devtools/)

  - Google Chrome's Dev Tools were used while building the project to test responsiveness and for debugging.

- [Pexels](https://www.pexels.com/)

  - Unsplash was used to source the hero image.

- [VS Code](https://code.visualstudio.com/)

  - VS Code was my IDE throughout this project.

- [Figma](https://www.figma.com/)

  - I learned how to use Figma for the wireframes but also for future prospects.

- [DrawSQL](https://drawsql.app/)
  - I used DrawSQL for creating my database schema.

# Testing

- Please refer [here](TESTING.md) for more information on testing of the Gather website

# Deployment

### Forking the GitHub Repository

Forks are used to propose changes to someone else's project or to use someone else's project as a starting point for your own idea. By forking the GitHub Repository you make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository.

To Fork a Github Repository:

1. Log in to GitHub and go to the [GitHub Repository](https://github.com/FraserR1188/plant-plates)
2. Locate the Fork button in the top-right corner of the page, click Fork.
3. You should now have a copy of the original repository in your GitHub account.

## Making a Local Clone

You will now have a fork of the repository, but you don't have the files in that repository locally on your computer.

To make a local clone:

1. Log in to GitHub and go to the [GitHub Repository](https://github.com/FraserR1188/plant-plates)
2. Above the list of files, click Code.
3. To clone the repository using HTTPS, under "Clone with HTTPS", click the 'Copy' icon. To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click Use SSH, then click the 'Copy' icon. To clone a repository using GitHub CLI, click Use GitHub CLI, then click the 'Copy' icon.
4. Open Git Bash.
5. Change the current working directory to the location where you want the cloned directory.
6. Type git clone, and then paste the URL you copied earlier. It will look like this, with your GitHub AE username instead of YOUR-USERNAME:

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

Click [Here](https://docs.github.com/en/github-ae@latest/get-started/quickstart/fork-a-repo) for the GitHub quick start guide with images and more detailed explanations of the above process.

## Creating an application with Heroku

You will need to deploy the application using Heroku.

1. Create a requirements.txt file by typing `pip3 freeze --local > requirements.txt` into the VS Code CLI. Ensure this is added to your .gitignore file.
2. Create a Procfile by typing `touch python app.py > Procfile`. Open it and ensure it doesn't have a new line, as this can create errors. Ensure it starts with a capital P.
3. Add and commit these files to GitHub.
4. Go to [Heroku](https://dashboard.heroku.com/apps). Log in or create an account
5. Click the 'New' button and click 'Create new app'.
6. Enter a unique name for your project with no capital letters or spaces and select your region. Click 'Create App'.
7. Inside your project, go to the Resources tab and create a Heroku Postgres Database
8. Inside your project, go to the 'Settings' tab. Scroll down and click 'Reveal Config Vars'.
9. Add in the following variables

- DATABASE_URL : postgresql:// (this is created and stores on the Code Institute Database)
- IP : 0.0.0.0
- PORT : 5000
- SECRET_KEY : Your secret key

10. Deploy your project by going to the Deploy tab and choose 'Connect to Github'
11. Find your repository name and select Connect.
12. To connect your Heroku database, go to 'More' in the top right and select run console. Enter `python` to access the python intepreter.
13. Then type `from plantplates import db`. Then type `db.create_all()`. You can then exit the console.

# Credits

## Code

- Code Institute: I referred to lessons and source code from Code Institute's Web Application Development course. I sourced the CRUD functionality on how to set up the database using the walkthrough.

- Materalize CSS: I used this library throughout the project. Particularly for the nav bar, cards, forms and buttons.

- Documentation: I referred to the documentation provided by [Flask](https://flask.palletsprojects.com/en/stable/), [SQLAlchemy](https://www.sqlalchemy.org/) and also [Python](https://www.python.org/doc/).

- YouTube: Visiual tutorials on how cloud computing works to understand AWS better for the uploading of images to S3 Buckets. the documentation from Amazon also helped.

## Content

- [Pinch of Yum](https://pinchofyum.com/): I used this website as an inspiration since it had a more personal feel than something more generic like BBC Good Food.

## Media

- Thank you for sharing the main image on my website [Ella Olsson](https://www.pexels.com/@ella-olsson-572949/).

### Acknowledgements

- Many thanks to my mentor Mikto for guiding me the way with heplful feedback and recommended tools.
- Thank you to the tutors and staff at Code Institute for their support.
- I really appreciate the people who I work with as it provided a wide testing base.

Please note this is a personal project. This website is purely for the sake of the developer's portfolio and not for public consumption.

Robbie Fraser, 2024
