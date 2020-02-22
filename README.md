# The BoardGameStore

A FullStack Final Project - Code Institute
<br>
By Linda Hsu
<br>
<br>
![Responsive displays of InstaRamen]()

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