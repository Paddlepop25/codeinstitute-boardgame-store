# The BoardGameStore

A FullStack Final Project - Code Institute
<br>
By Linda Hsu
<br>
<br>
![Responsive displays of The BoardGameStore]()

<br>

[The BoardGameStore](https://linda-boardgamestore.herokuapp.com/) is a website created for users who are looking to view and purcharse boardgames. A new user could register for a new account, login, change or reset a password, view his/her profile and logout. The user could also search for boardgames by name or category. A logged in superuser has extra game CRUD rights which allow him/her to add a game, edit the game's record and even delete it from the database.

Please register as a new user or use the following accounts to navigate the website:

To log in as a user without game CRUD rights, please use the following:
````
Username: sir_elton_john123@
Password: fishandchips123!
````

To log in as a user with game CRUD rights, please use the following:
````
Username: jane@.
Password: rotiprata123!
````

The deployed website can be found in
[**Heroku**](https://linda-boardgamestore.herokuapp.com/)

### User Stories

- #### As a user, I'd like to see:
    - A professional, modern and clean looking website to attract me to continue clicking on the other features 
    - Easy to understand and clear selections which would point me to the correct pages
    - Buttons which are straightforward in their purpose that allow me to view more information or do an action.
    - Options to have full control on adding, viewing, editing and deleting any game in the collection (as a superuser only)
    - The ability to register an account, login, logout, change password, reset password and view my profile details
    - The ability to select which game I'd like to purchase, change the quantity on it and pay with a (test) credit card

## UX / UI

### User Experience

- Users are welcomed with a refreshing orange color and a large Monopoly picture when they first visit the site. This sets the tone that this website is all about boardgames

- There is an eyecatching icon of a chess knight piece on the navbar and also as the favicon to further enhance the website's purpose 

- On larger screens, there are options on top of the navigation page for easy navigation on this website. On smaller screens, a hamburger on the center of the navigation bar provides a menu of options when it is clicked on 

- A search function is provided on the top center of the page that enable users to search for games and category

- If the user gives an input that is not found, a sad faced kitty cat's face will be shown on the search result page. The user could input a new search to search for other games on the same page 

- An introductory message is given on the main page to explain the functions and purpose of the website 

- Four 'best sellers' games are featured in the homepage below the introductory message and a 'MORE INFO' button suggests a call-for-action from the users if they'd like to view more information. Also, a user could add this to the cart with a click on the 'ADD TO CART' button

- In the 'Cart' page, a display of games is available to the user to add more quantity to it and view the grand total price. The user could remove the game too by clicking on the 'dustbin' icon or the 'X' icone depending what screen size the user is viewing the website on

- If the user clicks on the 'Proceed to Checkout' button, a form is displayed asking for the user to fill in the particulars for shipment. On the click of the 'Submit Payment' button, payment is made and this is verified with a picture of a smilling puppy

- The user could view the entire game catalogue with a visit to the 'Shop' page. The games are sorted in alphabetical order for easy eye-search. The games are also sorted by categories for easy reference 

- For superusers, a form is provided in the 'Add a Game' page where the user could fill up and add the game to the catalogue. The asterisks (*) imply that the fields are required to be filled before form submission 

- After the user fills in all fields and selects a picture to upload, upon clicking on the "ADD A GAME" button,  he/she is brought to the "shop" page where the latest game is added to the selected category. This way they could verify that their form submission is successful 

- To see the full information of the recently added game, the user could click on the "MORE INFO" button 

- Should the user want to edit the game details, they could be brought to the form by clicking on "EDIT GAME" button

- The edit form is pre-filled with the original entries of the user for easy reference. After the user make changes, the form can be saved by clicking on the "UPDATE GAME" button 

- The user could also delete the game by clicking on the 'DELETE GAME' button. I purposely positioned this button deep inside the 'edit game' form to discourage accidental deletion of game 

- If a user is logged in, a 'MY ACCOUNT' link is available on the navbar for the user to check his/her username and email address. There is also options for the user to reset or change his/her password

- If a user is not logged in, he/she could register an account. Thereafter, there is the option to log in or out of the website

- The company make provisions for customers who'd like to view the 'Terms & Conditions' and other policies. These are provided via links in the footer

- If there are any errors along the way, the user would be brought to an error 404 page where a sad cat picture would hopefully shock the users into inputing or clicking on the right things 

### Design Ideas

The website was designed with an orange theme color as it is refreshing and close to warm colours signifying fun and excitment. A clean white background to is prominent to ensure all the texts, cards, images and other elements to 'pop up' to the user.

- #### Fonts

    - The font **'Poppin'** was chosen as the primary font as it's rounded edges creates a warm and comforting feeling to the user
    - The font **'Montserrat'** was chosen as the font for all titles  ```<h4>Titles</h4>``` to give a distint but subtle feel that it's different to make the texts look more interesting to the user

- #### Colours

    - **Main Heading and Footer -** An orange theme colour was chosen for the navigation bar and footer for all pages to set a refreshing and subtle warm connection to the idea of fun, bright and merry because playing games result in such emotions. At the very top of the page, a dark background with orange fonts were chosen for a contrasting look, resulting in the ease of reading
    
    - **Cards -** A white background was chosen for each card containing the games and any borders in the original design of the card was removed to give a smooth flow feeling from the image to the information underneath. Black was chosen for the fonts to contrast against the background for easy reading

    - **SEARCH, ADD TO CART, VIEW CART, SUBMIT and CHECKOUT Buttons -** These buttons are in the theme orange color indicating a call-to-action for the users for these important features
    
    - **MORE INFO, RESET PASSWORD, CHANGE PASSWORD and other Buttons -** These buttons are in a green color to give contrast to the surrounding buttons around them

    - **EDIT, CANCEL & DELETE Buttons -** These buttons are in bright red color because it indicates danger of deleting, or committing changes to the game
    
    - **Forms -** A ligtened orange background was chosen for the 'Add a Game', 'Contact Us', 'Edit Game' and account-related forms to give it a pop-up look on the page with the white background
    
### Wireframes

Wireframes were created initially to help me vsualise the website in different sized screens. They can be viewed via this [link](https://github.com/Paddlepop25/codeinstitute-boardgame-store/tree/master/static/images/wireframes).

Initial planning was done on how to setup the database and the website. I used Microsoft Word to sketch out this ER diagram.
![The BoardGameStore's ER diagram](https://raw.githubusercontent.com/Paddlepop25/codeinstitute-boardgame-store/master/static/images/wireframes/game_erdiagram.png)

 
## Features

### Existing Features

1. #### Home Page (The BoardGameStore)

![Responsive displays of The BoardGameStore Main Page](https://raw.githubusercontent.com/Paddlepop25/codeinstitute-boardgame-store/master/static/images/readmes/homepage1.png)


- When the user first arrives at the page, he/she is welcomed with a large  picture of the familiar Monopoly, signifying that this website is about boardgames

- On top of the page is a bar with a dark background with contrasting orange fonts to entice potential customers to buy more games to get the free shipping. There is a search function for games and category for the user to use

- An orange navigational bar with an icon of a chess knight piece with links to the other pages are provided. For the mobile devices, the links are presented when the user clicks on the 'hamburger' icon of 3 horizontal lines

-  If the user scrolls down the main page, there is a few paragraphs of text describing the purpose and functions of the website. Further down, there are 4 best selling games displayed in the form of cards with pictures with information that they are prize winning games. There is a 'MORE INFO' button should the user would like to view more information and a 'ADD A CART' button in the theme orange color indicating a call to action for the user to add the game to the shopping cart

- At the bottom of the page, there is a footer in the orange color with the chess knight icon which points the user to the top of the page. There are some links to important information pertaining to having legal implications that the user may be in interested in. Also a link to information where the user could contact the company. In the social media section, there are links to my personal social media sites, Github repository and LinkedIn sites for anyone who wishes to contact me. There is also a disclaimer that this website is meant for educational purposes only

2. #### Add a Game page

![Responsive displays of Add a Game Page](https://raw.githubusercontent.com/Paddlepop25/codeinstitute-boardgame-store/master/static/images/readmes/addgame.png)
    
- A form is available for the user to input all fields, which are all required, and an image upload feature as a whole package for this game to be saved

- The user could change his/her mind and click on the 'CANCEL' button which would bring him/her back to the home page


2. #### Edit Game page

![Responsive displays of Edit Game Page](https://raw.githubusercontent.com/Paddlepop25/codeinstitute-boardgame-store/master/static/images/readmes/editgame.png )
   
- The form on this page is pre-filled with the exisiting information about the game from the database. Here the user could change any of the fields, including clearing and changing the image. The new information is saved with a click on the 'UPDATE GAME' button

- There is a bright red 'DELETE GAME' button for the user to delete the game. If the user clicks on it, he/she is asked to confirm deletion of the game

2. #### Shop Page

![Responsive displays of Shop Page](https://raw.githubusercontent.com/Paddlepop25/codeinstitute-boardgame-store/master/static/images/readmes/shop.png)
    
- All the games from the store are displayed here, with each being in one of 3 categories. The games are sorted by alphabetical order for users to easily search for games at a glance

- A click on the 'MORE INFO' button would bring the user to view more information of the game. Alternatively, the user could click on the game image to be brought to the same page

- A click on the 'ADD TO CART' button would add this game to the shopping cart

- On this page too, displays the results of any search the user makes from the top row on every page. A suggested search would be `Star Wars` which would return 3 results. If there aren't any results, a picture of a sad kitty cat is shown

2. #### Game Information Page

![Responsive displays of Game Information Page](https://raw.githubusercontent.com/Paddlepop25/codeinstitute-boardgame-store/master/static/images/readmes/gameinfo.png)
  
- This page lists all the information about the game, specifically the game description and what is inside the box. There are buttons below it for the user to navigate easily to other parts of the website

2. #### Cart Page

![Responsive displays of Cart Page](https://raw.githubusercontent.com/Paddlepop25/codeinstitute-boardgame-store/master/static/images/readmes/cart.png)
  
- All the games the user added to cart would be displayed here. The user could adjust the quantity accordingly. The unit price, subtotal and grand total price are displayed for the user to know how much he/she is spending. The game could be deleted with a click on the 'dustbin' or 'X' icon (depending which screen sizes the site is viewed on)

- Below the table of the games, buttons are provided for the user to make payment or to continue shopping

2. #### Checkout Page

![Responsive displays of Checkout Page](https://raw.githubusercontent.com/Paddlepop25/codeinstitute-boardgame-store/master/static/images/readmes/checkout.png)
  
- A form is provided for the user to provide shipping details. There is also the payment part which would display error messages if the credit card details is wrong. Suggested information to input:
````
Credit card number: 4242424242424242
Security code (CVV): 123
Month: 1
Year: 2025
````
- The user could submit payment with a click on the 'Submit Payment' button and a picture of a winking cat would be displayed  

2. #### Stripe Payment

![Responsive displays of Stripe Payment Page](https://raw.githubusercontent.com/Paddlepop25/codeinstitute-boardgame-store/master/static/images/readmes/stripe%20payment%20success.png )
   
- The users would be making payment with Stripe's payment features

2. #### Contact Us Page

![Responsive displays of Contact Us Page](https://raw.githubusercontent.com/Paddlepop25/codeinstitute-boardgame-store/master/static/images/readmes/contactus.png)
   
- The store's location is displayed with a pin on the google map with information underneath on addresses, store operating hours, etc
- A form is available for the user to contact the company. The user is brought to the home page after clicking on the 'Submit' button

3. #### Registration Page

![Responsive displays of Registration Page](https://raw.githubusercontent.com/Paddlepop25/codeinstitute-boardgame-store/master/static/images/readmes/register.png)
   
- A form is provided for the user to register an account with the store. This is needed for the user to make payment for games selected for the shopping cart. After clicking on the 'register' button, the user is logged in and brought to the home page

3. #### Login Page

![Responsive displays of Login Page](https://raw.githubusercontent.com/Paddlepop25/codeinstitute-boardgame-store/master/static/images/readmes/login.png)
    
- A form is provided for the user to login to their account. A username and password is needed and upon clicking the 'Login' button, the user is logged in and brought to the home page
- The 'FORGET PASSWORD' password when clicked will allow the user to input his/her email for instructions on getting a new paswsword

4. #### Logout Page 

![Responsive displays of Logout Page](https://raw.githubusercontent.com/Paddlepop25/codeinstitute-boardgame-store/master/static/images/readmes/logout.png)

- A user would be brought here on click of the 'LOGOUT button' where he/she is asked confirm logout. On successful logout, the user is brought to the homepage. Of course the user could cancel logging out too and be brought to the 'shop' page

5. #### My Account/ User's profile Page 

![Responsive displays of My Account/ User's profile Page](https://raw.githubusercontent.com/Paddlepop25/codeinstitute-boardgame-store/master/static/images/readmes/profile.png)

- The user could see his/her email and username here. There is the option to reset or change password also

6. #### Password Change/ Password Reset Pages 

![Responsive displays of Password Change/ Password Reset Pages](https://raw.githubusercontent.com/Paddlepop25/codeinstitute-boardgame-store/master/static/images/readmes/reset:changepassword.png)
  
- The user is able to change or reset the password from these pages.

7. #### Terms & Conditions/ Privacy Policy/ Shipping & Returns Pages

![Responsive displays of Terms & Conditions/ Privacy Policy/ Shipping & Returns Pages](https://raw.githubusercontent.com/Paddlepop25/codeinstitute-boardgame-store/master/static/images/readmes/termsconditions.png)
    
- The user could view the company's various policies from these pages

8. #### Error 404 Page

![Responsive displays of The BoardGameStore Error 404 Page](https://raw.githubusercontent.com/Paddlepop25/codeinstitute-boardgame-store/master/static/images/readmes/error404.png)
   
- If the user has inputted an invalid entry on the URL, he/she would be brought to this page which shows that there is an error with a picture of a sad looking kitty cat

- When the user scrolls down, there is a 'home' button which allows them to be brought back to the main page with a click of the button

### Future Features to Implement

2. #### Pagination

    - Pagination on the shop pages would be helpful with organizing the collection as it grows. It also looks neater and helps with loading time

3. #### Video

    - I'd like to include a video on the history of boardgames for better users' experience in gaining more knowledge from this website

4. #### Labels

    - Based on the database records on the games where they are out of stock or discounted, I'd like to display these information on the game cards like having a small tag at the top left hand side

4. #### Premium membership

    - Based on the database records on the users' membership, I'd like to give extra discounts to premium members or have a birthday special gift. These could be reflected in the shopping cart page

## Database

### Postgres SQL

- A [PostgresSQL](https://www.postgresql.org/) database was used to store game images and information deployed to Heroku from the Cloud9 environment

## Technologies Used
Here are a list of programming languages, frameworks, technologies and tools used for this website:

|Technologies                 |Remarks                                                                   |
|-----------------------------|--------------------------------------------------------------------------|
|[HTML5](https://www.w3schools.com/)                          |Testing                                  |
|[CSS3](https://www.w3schools.com/)                           |Testing                                  |
|[JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)                      |Testing|
|[jQuery website](https://code.jquery.com/)                       |Used to simplify DOM manipulation                                |
|[Bootstrap](https://getbootstrap.com/)                    |Testing                            |
|[Fontawesome website](https://fontawesome.com/)                 |Testing                          |
|[Google Colaboratory notebook](https://colab.research.google.com/)                 |used for writing the markdown for this README.md file                  |
|[Django](https://docs.djangoproject.com/en/3.0/)                        |Testing           |
|[Python](https://www.python.org/)              |as the main programming language used to build this project                                                        |
[Jinja](https://palletsprojects.com/p/jinja/)                          |a Python web application framework to display the html pages with entries from the PostgresSQL database                                  |
[Cloud9](https://c9.io)                      |an IDE used to develop the website.                                  |
[Git](https://git-scm.com/)                          |used for version control to regularly commit codes to Github                                  |
[GitHub](https://github.com/)                      |used as a remote backup of code used in this project                                  |
[Heroku](https://www.heroku.com)                          |used as a platform for this project to be deployed to                                  |
[PostgresSQL](https://stripe.com/ie)              |To allow the storage of database in sqlite before it can be used in Heroku as a database.                                                      |
[UploadCare](https://uploadcare.com/)              |A tool that enables images uploading                                  |
[Stripe Payments](https://www.postgresql.org/)              |Testing                                                     |
[Sqlite3](https://www.sqlite.org/index.html)              |SQLite3 was used to store database and retrieve data via the backend.                                                      |

## Testing

A full testing process can be found in a separate [tests.md](https://github.com/Paddlepop25/codeinstitute-boardgame-store/blob/master/tests.md) file.

## Deployment
The project was built using [Cloud9](https://c9.io).

- Please have the following installed on your machine before working on it in your IDE:
    - [PIP](https://pip.pypa.io/en/stable/installing/)
    - [Python 3](https://www.python.org/downloads/)
    - [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)

### Cloning from Github

1. Go to [The BoardGameStore repository](https://github.com/Paddlepop25/codeinstitute-boardgame-store) and click the green 'Clone or download' button and then click 'Download ZIP'

2. Extract the contents to a location of your choice. Otherwise, you can clone the project into your IDE with running the following command in the terminal
```
git clone https://github.com/*username*/*repository*
```

3. In your local IDE ensure you have an opened terminal, cd to the correct location to where you have your ZIP file

4. Run this in your terminal:
````
pip3 install -r requirements.txt
````

5. To open the website, run this in your terminal:
````
python3 manage.py runserver 8080
````

6. A green window will pop up. Click on the link inside it to view the project

### Deploying to Heroku
* I followed the instructions my coding teacher, Paul gave in his google document

- The following steps are to deploy to Heroku in the terminal:

1. Go to [Heroku](https://dashboard.heroku.com/) and register for an account

2. Install Heroku in your system with this command
 `sudo snap install heroku --classic`

3. Install these one by one following using pip3:
````
sudo apt install libpq-dev python3-dev
sudo pip3 install gunicorn 
sudo pip3 install psycopg2
sudo pip3 install Pillow
sudo pip3 install whitenoise 
sudo pip3 install dj_database_url
````

4. In the `settings.py` file, add Whitenoise to the middleware:
````
MIDDLEWARE = [ 
..... 
'whitenoise.middleware.WhiteNoiseMiddleware'
]
````

7. Create a repository in Github

6. Create a hidden file named `.gitignore` and add `.c9` in the file. Also add the following django files to be ignored taken from [here](https://gitignore.io/api/django)

8. In your terminal, type these commands to add the repository origin from Github:
````
git init 
git add . 
git commit -m "First commit" 
git remote add origin https://github.com/Paddlepop25/codeinstitute-boardgame-store
````

9. Login to Heroku from your terminal by using this command `heroku login -i`

6. Create a new app with a unique name with this command `heroku create <app_name>` replacing the <app_name> with a name of your choice

7. To check if the correct github repository and heroku app are connected to this project, use this command 
`git remote -v`

8. In your app in Heroku in the settings tab, click on the 'Reveal Config Vars' button. Copy the following variables from the `.bashrc` in Cloud9 over here.

14. Be in the root directory and run the command `echo web: python app.py > Procfile` which will create a Procfile. Add this line inside the Procfile `web: gunicorn <PROJECT_FOLDER>.wsgi:application` and replace the <PROJECT_FOLDER> with your project's name

15. Inside the `settings.py` add the URL of the heroku app into the ALLOWED_HOST section

11. All sensitive data and links should be placed into the `env.py` with those information linked to the `settings.py` file, for example
````
os.environ.setdefault("STRIPE_PUBLISHABLE", "") os.environ.setdefault("STRIPE_SECRET", "") os.environ.setdefault("DATABASE_URL", "") os.environ.setdefault("SECRET_KEY", "") os.environ.setdefault("AWS_SECRET_KEY_ID", "") os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "")
````

5. Use this command to create a `requirements.txt` file which lists all the required packages needed for this project:
````
pip3 freeze --local > requirements.txt
````

4. At the project directory level, create a `Static` folder, which should  be on the same level as the `manage.py` file. Place some files inside here like images or text files

3. Add the following in the settings.py file for static files and uploads:
````
STATIC_URL = '/static/' STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), ) STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
````

15. Commit all files to Heroku with these commands
````
git add . 
git commit -m "Deploying to Heroku" 
git push heroku master
````

8. To use the PostgresSQL database, type this to your terminal 
````heroku addons:create heroku-postgresql
````

20. To check the URL to the database created, run this command
`heroku config` and copy this URL to be used later

21. In the `.bashrc` file, add the following
`export DATABASE_URL="database_url"` and restart the bash terminal

22. In the `settings.py` add `import dj_database_url` after all the other import statements

23. In the `settings.py` file, comment out the `DATABASES` section and add the URL copied from Heroku here
````
DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}
````

24. Save and restart the terminal

12. Make migrations with this command
````
python3 manage.py migrate
````

15. Commit all files to Heroku with these commands
````
git add . 
git commit -m "Updated settings.py" 
git push heroku master
````

13. Make a superuser with this command
`python manage.py createsuperuser`

15. At the very top of the page in Heroku, click "Open App". You will now be able to view the project in Heroku

## Credits

### Contents

- All game card images and information is take from [Team Board GAME](https://www.teamboardgame.com/)

### Media
- #### Images
    - The main Monopoly image for the website was found in taken from [here](https://www.celebitchy.com/wp-content/uploads/2018/11/activity-board-game-close-up-1314435.jpg)
    - The Favicon was created [here](https://favicon.io/favicon-converter/)
    - Pictures of games were downloaded from [TeamBoardGame](https://www.teamboardgame.com/)
    - Image of [sad cat](http://www.catboxzen.com/wp-content/uploads/2014/10/sad-cat.jpg), [winking cat](https://static.boredpanda.com/blog/wp-content/uploads/2016/04/smiling-animals-8-570e0c1b0703c__605.jpg), [happy dog](http://elelur.com/data_images/articles/happy-dogs-do-you-know-what-makes-them-really-so.jpg) were taken from the respective webpages

### Codes

- Ideas on how to design an error page was from this
[blog](https://neilpatel.com/blog/how-to-create-a-spectacular-404-error-page-with-12-examples/)

### Acknowledgements

A huge thank you to:

- Mr Paul, our teacher at [Trent Global College](trentglobal.edu.sg/diplomainsoftwaredevelopment/)
- Our very helpful teaching assistant John
- My classmates who were helpful in giving tips when I'm stuck
- My friends and family whom were the user testers of this website. They gave valuable feedback on how to improve the project

## Disclaimer

All content on this website are used for educational purposes only.