# My Next Adventure

![Cliffs_of_Moher](https://github.com/shane-os/my-next-adventure/blob/main/static/images/home-image.jpg)

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
 * Database Structure

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
 * Clone Project
 * Module Requirements
 * MongoDB
 * Heroku

### Accreditation & Gratitude

### References

## UX (User Experience):
#### Project Goals:
 * The aim of this project is to design and build a website allowing users to research tourist attractions in their chosen area.
 * Users will be able to create their own unique accounts and view, create, update and delete attractions. This will assist other users in researching potential places to visit on their next vacation.
 * By engaging users to form an active community, this hopefully will lead to more people visiting less well known attractions and potentially achieving a greater experience.

#### User Goals:
 * Research attractions for their chosen area.
 * Determine the appropriateness of the attraction based on their criteria. (e.g. Free, Suitable for Children, etc.)
 * Add new attractions to the site for the benefit of other users.

#### User Stories:
 * As a user, I would like to find a list of attractions for my chosen area.
 * As a user, I would like to examine which attractions meet my criteria. (e.g. Free, Pre-Booking Required, etc.)
 * As a user, I wish to add information about attractions to make others aware of these places.
 * As a user, I would like to help other users by correcting any errors I notice in descriptions of attractions.

#### Site Owner Goals:
 * As a site owner, I wish to provide information on various attractions in the user's chosen area.
 * As a site owner, I want to allow users to easily search for attractions based on name or location.
 * As a site owner, I would like to build a site allowing users add their own attractions.

#### User Requirements:
 * Attraction search and filter function delivers correct results promptly.
 * Users are able to create accounts and log into their accounts as required.
 * Accounts created and user details provided are to be secure.
 * New attractions are easy and straight forward to add to the site.
 * Internal site links direct users as expected.

#### User Expectations:
 * Attraction information and images are appropriate and shown in an ordered fashion.
 * Attraction information can be updated if incorrect/ incomplete.
 * Site layout is simple and easy to navigate.
 * Users can contact the site owner if an issue occurs.

## Site Layout & Design:
#### Wireframes:
Initially I set out my ideas for the site using pen and paper. Following a few changes, I proceeded to create wireframes using the Balsamiq Wireframe application. The three wireframes have been stored in a PDF format at the following locations:

 * Mobile
 * Desktop
 * Tablet
 
#### Icons:
Icons from the Font Awesome collection were utilised to help users navigate the site. This allows the user to fully explore the site and obtain the best user experience possible. The icons were mainly used for social media icons and the search bar.

#### Colour Scheme:
![Coolor Palette](https://github.com/shane-os/my-next-adventure/blob/main/wireframes/my-next-adventure-colours-summary.png)

For this project, I have chosen to use striking and varied colours to represent the numerous attractions available. Different colours will be used to indicate the style of the attraction on offer. E.g. Red as a colour of excitement will be used for theme parks and similar venues. The main colours chosen to be used in this project are:

 * #000000 - Black - Text and footer
 * #538D22 - Maximum Green - Navigation Bar
 * #4F74E3 - Royal Blue Light - Flash Messages
 * #FFFFFF - White - Used for text and backgrounds

#### Database Structure:
MongoDB was used to create and store user and attraction records. The database was configured on Heroku and MongoDB to automatically update when a new user registers or an attraction record is created, edited or deleted. The following were the collections set up on MongoDB:

Users:
| Key   | Value   |
| ----- | ------- |
| _id   | ObjectId |
| username | String |
| password | String |

Attractions:
| Key   | Value   |
| ----- | ------- |
| attraction_name  | String |
| location | String |
| description | String |
| image | String |
| free | String |
| pre_booking_required | String |
| suitable_for_children | String |


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
 * [Balsamic Wireframes](https://balsamiq.com/)
 * [PyMongo](https://pymongo.readthedocs.io/en/stable/)
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
 * Add Attraction
 * Edit Attraction
 * Delete Attraction

#### Future Implementation:
 * Links to sites to purchase tickets
 * Attraction Reviews
 * Attraction Rating System
 * Attraction location maps
 * Greater search capabilities
 * Videos and multiple images of each attraction

## Testing
#### Navigation Bar:
Each link in the navigation bar was tested to ensure that the correct page was returned. Prior to the user logging into/ registering for account, the navigation bar present will not show the user either the dashboard or the logout options.

#### Contact Form:
A simple contact form was built to allow users to ask for more information, report an error on the site, report a mistake in one of the atttractions listed, etc. The site uses EmailJS to facilitate the sending of the form to an email account. Each of the four fields (first name, last name, email address & message) is required to be filled in for the form to be submitted. Firstly the form was tested by leaving each field blank. If a user attempts to submit a blank form, the form is not sent and they are informed that they have to fill in the missing field. For the email address field, the user is required to fill in a value that contains a string of text followed by an "@" symbol followed by another piece of text. A variety of values were inputed without meeting one or more of the previously mentioned criteria. Finally to confirm the message has been sent, an alert using the "Sweet Alert 2" package would appear on screen.

#### User Account Registration:
When a user registers for the site they are required to enter a unique user name, a password and to confirm that password. To prevent duplicate usernames, a check is completed to ensure that the desired username is unique. The password chosen must also meet certain requirements: not contain blank spaces, minimum length of 3 and a maximum length of 10. Capital letters and numbers are allowed. Duplicate usersnames were used to ensure that only unique usernames are used. The password and confirm password fields were checked using different passwords of varying lengths, letters and numbers to ensure that the checks coded into the site worked as expected.

#### User Account Login:
To access their account users only need to enter their username and password. Checks were conducted to ensure that only usernames and their associated passwords could be used to access the site. If a username entered into the login section was not a registered account, the following message would appear "Username Not Registered. Please create an account!". The python script would check the Mongodb collection to see if the correct values were inputed. To test the password check ability, registered usernames were used alongside incorrect passwords. Each time the correct message appeared: "Incorrect Username/Password. Please try again".

#### Code Validators:
 * The HTML code was passed through the W3C Validator
 * The CSS code was passed through the Jigsaw Validator
 * The JavaScript code was passed through the JSHint Validator


## Deployment:
#### Gitpod:
The entire site was coded using the Gitpod Integrated Development Environment. Using the "git commit" and "git push" methods the files making up the site were updated and saved on a Github depository. In parallel to this, an account was set up on MongoDb to allow for a database to store user and attraction data and a Heroku account was established.

#### Clone Project:
The My Next Attraction site can be run locally by following these steps:

1. In your browser, go to My Next Attraction [repository](https://github.com/shane-os/my-next-adventure) on Github.
2. Click on the Code button with the dropdown arrow.
3. Select the HTTPS option and copy the link shown.
4. Open the Gitpod Integrated Development Environment
5. In the Git terminal, decide where the cloned directory will be located by entering the change working directory command ($ cd filepath) followed by the desired storage location.
6. In the Git terminal, use the git clone command ($ git clone) and enter the repository link copied earlier.

#### Module Requirements:
For the site to run, it requires a set of python modules. An individual module can be installed in the Gitpod terminal using the command:

pip3 install module_name

To install all required modules, please enter the following command:

pip3 install -r requiremnts.txt

#### MongoDB:
A MongoDB account is necessary to safely store user and attraction data essiential to the site. Please sign-up or sign-in to an account [here.](https://www.mongodb.com/)

1. Create a new cluster.
2. Go to the Database Access section and add a new database user. Enter your chosen username and password. Keep these details secure as your database and therefore the site will be compromised if these became public. Make sure that the user has "Read and Write" priviledges. Click add user. 
3. In the Network Analysis section, choose "allow access from anywhere". Enter "0.0.0.0" as the IP Address.
4. Click on the collections button and then the "Add My Own Data" button before creating a new database called "my-next-adventure"
5. Create the ffollowing two collections:
 a. Users
 b. Attractions

6. In the Gitpod IDE, create a file named "env.py" and end enter the following lines and variables:

```
import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "Your Chosen Secret Key")
os.environ.setdefault("MONGO_URI", "Your MongoDB URI")
os.environ.setdefault("MONGO_DBNAME", "my-next-adventure")
os.environ.setdefault("DEBUG", "1")
```

Note 1: For the secret key variable use a site such as [randomkeygen](https://randomkeygen.com/) to create a secure key. In your gitignore file make sure to add env.py to avoid the secret key becoming public.
Note 2: The Mongo URI can be found by clicking the connect button on your MongoDB clusters. Copy the link provided and paste into the Mongo_URI variable space. 

The My Next Adventure application can now be run locally by entering the following command into the Git Terminal:

```
$ python3 app.py
```

#### Heroku:
After logging into your Heroku account, deploy the project to Heroku by following these steps:
1. In the Git Terminal create the Procfile and requirements.txt file:
Requirements:
```
pip3 freeze --local > requirements.txt
```
Procfile:
```
echo web: python app.py > Procfile
```
If successfully executed the Procfile will have the following line of code:
```
web: python app.py
```

2. On heroku, select "Create a New App", input an app name and choose a region and click "Create App".
3. Select Github as the deployment method.
4. Make sure that your username is displayed and enter the repository name. Once the correct repository is shown, click "Connect".
5. As the environment variables are hidden in the env.py file, the environment variables will need to be entered into Heroku. Select settings and click on "Reveal Config Vars".
6. Input the following environment variables:

```
"IP", "0.0.0.0"
"PORT", "5000"
"SECRET_KEY", "Your Chosen Secret Key"
"MONGO_URI", "Your MongoDB URI"
"MONGO_DBNAME", "my-next-adventure"
```

7. Select "Deploy".
8. Select "Automatic Deployment" as our app will update when new commits are pushed to Github. 
9. Click the "Deploy Branch" button and click "View App" to see the site.
