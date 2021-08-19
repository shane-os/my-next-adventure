# My Next Adventure

## Contents

### UX (User Experience)
 * Project Goals
 * User Goals
 * User Stories
 * Site Owner Goals
 * User Requirements
 * User Expectations

### Site Layout & Design
 * Wireframes
 * Icons
 * Images
 * Colour Scheme

### Technologies
 * Programming Languages
 * Libraries & Tools
 * User Data Collection, Storage & Retrieval

### Features
 * Developed
 * Future Implementation

### Testing
 * Navigation Bar
 * Contact Form
 * User Account Registration
 * User Account Login
 * Code Validators

### Resolution of Bugs

### Deployment
 * Gitpod
 * Local Deployment
 * MongoDB
 * Heroku

### Accreditation & Gratitude

### References

## UX (User Experience):
#### Project Goals:
 * The aim of this project is to design and build a website allowing users to research tourist attractions in their chosen area.
 * Users will be able to create their own unique accounts and post reviews on featured tourist attractions. This will assist other users in researching potential places to visit on their next vacation.

#### User Goals:
 * Research attractions for their chosen area.
 * Determine the appropriateness of the attraction based on their criteria. (e.g. Free, Suitable for Children, etc.)
 * See reviews posted by other site users.
 * Provide helpful reviews to other users.

#### User Stories:
 * As a user, I would like to find a list of attractions for my chosen area.
 * As a user, I would like to view honest, personal feedback of other users about each site to help make a better informed decision.
 * As a user, I would like to examine which attractions meet my criteria. (e.g. Free, Pre-Booking Required, etc.)
 * As a user, I would like to help other users by providing my own reviews of attractions.

#### Site Owner Goals:
 * As a site owner, I wish to provide information on various attractions in the user's chosen area.
 * As a site owner, I want to allow users to easily filter attractions based on specific criteria to find applicable attractions.
 * As a site owner, I would like to build a site allowing users to give reviews on attractions.

#### User Requirements:
 * Attraction search and filter function delivers correct results promptly.
 * Users are able to create accounts and log into their accounts as required.
 * Accounts created and user details provided are to be secure.
 * Users are able to post reviews on attractions
 * Internal site links direct users as expected.

#### User Expectations:
 * Attraction information and images are appropriate and shown in an ordered fashion.
 * Attraction reviews are easy to publish and view.
 * Users can contact the site owner if an issue occurs.

## Site Layout & Design:
#### Wireframes:
Initially I set out my ideas for the site using pen and paper. Following a few changes, I proceeded to create wireframes using the Balsamiq Wireframe application. The three wireframes have been stored in a PDF format at the following locations:

 * Mobile
 * Desktop
 * Tablet
 
#### Icons:
Icons from the Font Awesome collection were utilised to help users navigate the site. This allows the user to fully explore the site and obtain the best user experience possible.

#### Colour Scheme:
For this project, I have chosen to use striking and varied colours to represent the numerous attractions available. Different colours will be used to indicate the style of the attraction on offer. E.g. Red as a colour of excitement will be used for theme parks and similar venues. The main colours chosen to be used in this project are:

 * #000000 - Black - Text
 * #538D22 - Maximum Green - Attractions involving nature, outdoors events
 * #4F74E3 - Royal Blue Light - Knowledge and sea-life based attractions such as museums, boat tours amd aquariums
 * #F41101 - Red - Energic and exciting attractions including sporting events and theme parks
 * #997748 Metallic Sunburst (Brown) - Historical buildings and landmarks including castles and palaces  

## Technologies:
#### Programming Languages:
 * [HTML](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
 * [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 * [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
 * [Python](https://www.python.org/about/)

#### Libraries & Tools:
 * [Git](https://git-scm.com/)
 * [Github](https://github.com/)
 * [Gitpod](https://www.gitpod.io/)
 * [Heroku](https://www.heroku.com/)
 * [Bootstrap](https://getbootstrap.com/)
 * [Google Fonts](https://fonts.google.com/)
 * [SweetAlert2](https://sweetalert2.github.io/#usage)
 * [Font Awesome](https://fontawesome.com/)
 * [EmailJS](https://www.emailjs.com/)

#### User Data Collection, Storage & Retrieval:
 * [MongoDB](https://www.mongodb.com/)

## Features:
#### Developed:
 * Navigation Bar
 * Login
 * Register
 * Profile
 * Contact Form
 * Attractions Listing

## Testing
#### Navigation Bar:
Each link in the navigation bar was tested to ensure that the correct page was returned. Prior to the user logging into/ registering for account, the navigation bar present will not show the user either the dashboard or the logout options.

#### Contact Form:
A simple contact form was built to allow users to ask for more information, report an error on the site, report a mistake in one of the atttractions listed, etc. The site uses EmailJS to facilitate the sending of the form to an email account. Each of the four fields (first name, last name, email address & message) is required to be filled in for the form to be submitted. Firstly the form was tested by leaving each field blank. If a user attempts to submit a blank form, the form is not sent and they are informed that they have to fill in the missing field. For the email address field, the user is required to fill in a value that contains a string of text followed by an "@" symbol followed by another piece of text. A variety of values were inputed without meeting one or more of the previously mentioned criteria. Finally to confirm the message has been sent, an alert using the "Sweet Alert 2" package would appear on screen.

#### User Account Registration:
When a user registers for the site they are required to enter a unique user name, a password and to confirm that password. To prevent duplicate usernames, a check is completed to ensure that the desired username is unique. The password chosen must also meet certain requirements: not contain blank spaces, minimum length of 3 and a maximum length of 10. Capital letters and numbers are allowed. Duplicate usersnames were used to ensure that only unique usernames are used. The password and confirm password fields were checked using different passwords of varying lengths, letters and numbers to ensure that the checks coded into the site worked as expected.

#### User Account Login:
To access their account users only need to enter their username and password. Checks were conducted to ensure that only usernames and their associated passwords could be used to access the site. If a username entered into the login section was not a registered account, the following message would appear "Username Not Registered. Please create an account!". The python script would check the Mongodb collection to see if the correct values were inputed. To test the password check ability, registered usernames were used alongside incorrect passwords. Each time the correct message appeared: "Incorrect Username/Password. Please try again".

## Deployment:
#### Gitpod:
The entire site was coded using the Gitpod Integrated Development Environment. Using the "git commit" and "git push" methods the files making up the site were updated and saved on a Github depository. In parallel to this, an account was set up on MongoDb to allow for a database to store user and attraction data and a Heroku account was established.
