# Plant Plates

## Milestone Project 3 - Backend Development

(This is spacing for the main image once project is complete)

- The recipe website is aimed at age 12 onwards to enjoy to cook. The website should bring inspiration and enjoyment through cooking. It should also entice the visitor to prepare something that they did not intend. We want this to be a hub of activity and a place where users will store there recipes and allow other people to view them.
- This is my Milestone Project 3 submission for Code Institutes Diploma in Web Application Development Course. My website uses both relational and non-relational databases, features full CRUD functionality and is built using technologies that I have learnt including HTML, CSS, JavaScript, Python, Flask and PostgreSQL.

## Project Link

(Link to the project)

## Repository

(Link to repo)

## Project Goals

This website is dedicated for people who love food and want to share there love for food. This also has a heavy influence from myself and my girlfriend as this is a dream we've always wanted, a website where we can express our creativity with food for everyone to enjoy. There will be a lot of recipes from ourselves but also recipes from other people who have uploaded them. There are also articles about food which people can read and create themselves.

There is an account page which will be the hub for the return user so they can store all their recipes and have somewhere to go back to.

# Table of Contents

## Contents

1. User Stories
   - [First-time Users](#first-time-users)
   - [Returning Users](#returning-users)
   - [Website Owners](#website-owners)
2. [Design](#design)
   - [Typography](#typograhy)
   - [Images](#images)
   - [Colour Scheme](#color-scheme)
   - [Wireframes](#wireframes)

### First time Users

- As a first-time user, I want the website to be accessible on any device.
- As a first-time user, I want the website to be easy to navigate.
- As a first-time user, I want to sign-up quickly and easily.
- As a first-time user, I want find what recipe I want quickly and easily.

### Returning Users

- As a returning user, I want to be able to login easily on the homepage.
- As a returning user, I want to be able to create / read / edit / delete my own recipes.
- As a returning user, I want to be able to search for recipes with keyword criteria, as well as specific recipe criteria e.g. difficulty, cuisine, ingredients, how to cook.
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

### Navigation Bar

![Before use has logged in on desktop and tablet](plantplates/static/images/README/tablet-desktop-navbar.png)

- This is what the nav bar looks like before the user has logged in on a desktop.

![Before user has logged in on mobile](plantplates/static/images/README/mobile-navbar.png)

- This is what the nav bar looks like before the user logs in on a mobile.

![After nav bar desktop-tablet](plantplates/static/images/README/tablet-desktop-after-log-in.png)

![After nav bar mobile](plantplates/static/images/README/mobile-after-log-in.png)

- This is what the user has once logged in.

- I have also made myself an admin which has the ability to manage the catergories (CRUD). This is what the appearence looks:

![Mobile Admin](plantplates/static/images/README/mobile-admin-categories.png)
![Desktop Admin](plantplates/static/images/README/admin-categories.png)

### Footer

![Footer](plantplates/static/images/README/footer.png)

- The footer is present through the website and stays the same with the social media icons.

### Modal Messages

![Logged In Modal](plantplates/static/images/README/logged-in-modal.png)

- User sees this when logged in for 2 seconds.

![Logged Out Modal](plantplates/static/images/README/logged-out-modal.png)

- User sees this when logging out for 2 seconds

## Home Page

### Hero Image

![Homepage Hero Image](plantplates/static/images/README/home-hero-image.png)

- This is situated right underneath the nav-bar with the title of the website within it and an indication of what the website is about.

### Website Values

![Website Values](plantplates/static/images/README/home-what-the-site-is.png)

- These are the values of the website.

### Recently Added

![Recently Added](plantplates/static/images/README/latest-greatest.png)

- These are the most recently added recipes to the website. Everyone can see these, the user doesn't have to be logged in. Maximum of 4 will be shown.

### Plant Plates Logo

![Plant Plates Image](plantplates/static/images/README/home-parrallex.png)

- This is the parallex which utilises Materilezes JavaScript Parallex feature.

### The story behind the website

![Our Story](plantplates/static/images/README/home-story.png)

- This section is about the website owners and there aim through the website.

## Login Page

![Login Page](plantplates/static/images/README/login-page.png)

- This is the login page

## Sign Up

![Sign Up](plantplates/static/images/README/sign-up-page.png)

- This is the sign up pge which has a link to the login page incase the user already has an account.

## Account Page

![Account Page](plantplates/static/images/README/account-page.png)

- Once the user has logged in, they are transport to their account page.

## Create a New Recipe Page

![Create Page](plantplates/static/images/README/create-recipe-page.png)

- The create a new recipe page has 9 input fields, one being an upload image section which uses AWS for image upload.

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

- Only myself can see these pages

![Admin Categories](plantplates/static/images/README/admin-manage-categories.png)

- This how the admin can edit or delete categories

![Confirm Detele Cateogry](plantplates/static/images/README/confirm-delete-category.png)

- Defensive programming, making sure there is a confirmation delete modal.

![Edit Category](plantplates/static/images/README/edit-category.png)

- This how it looks to edit a category.

![Add Category](plantplates/static/images/README/add-category.png)

# Future Features

### Articles

- I have made the modules for users to create Articles and discuss about food topics

### Leaving Reviews

- Another future feature would be to leave reviews on other users recipes and give feedback.

### Ratings

- Leave users a star rating.

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

- [Unsplash](https://unsplash.com/)

  - Unsplash was used to source the hero image.

- [VS Code](https://code.visualstudio.com/)

  - VS Code was my IDE throughout this project.

- [Figma](https://www.figma.com/)

  - I learned how to use Figma for the wireframes but also for future prospects.

- [DrawSQL](https://drawsql.app/)
  - I used DrawSQL for creating my database schema.

# Testing

- Please refer [here](TESTING.md) for more information on testing of the Gather website
