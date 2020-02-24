# The BoardGameStore - Testing #

The deployed project 'The BoardGameStore' is on [**Heroku**](https://linda-boardgamestore.herokuapp.com/)

The repository can be found in
[**Github**](https://github.com/Paddlepop25/codeinstitute-boardgame-store)


[**Main README.md file**](https://github.com/Paddlepop25/codeinstitute-boardgame-store/blob/master/README.md)

![Responsive displays of The BoardGameStore](https://raw.githubusercontent.com/Paddlepop25/codeinstitute-boardgame-store/master/static/images/readmes/boardgamestoremontage.jpg)

## Automated Testing

### Validating Code

Validation services were used to ensure that the respective codes were valid used to develop the website.

- [W3C Markup Validation Service](https://validator.w3.org/) was used to test HTML code to ensure it was valid code. Errors were shown where there were Jinja codes `{% %}` and this was expected as the latter are not html codes. Aside from these there were no other errors.

- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) was used to test CSS code to ensure it was valid code. No errors were found.

## Manual Testing

A number of manual tests were done on each page to confirm that the website functioned well.

This website was tested on different web browsers and on different devices. I also requested friends and co-workers for feedback on what they liked and didn't like about this website. Adjustments were made accordingly until the final product upon project submission.

Devices and browesers:
* iPad 3
    * Safari
* MacBook Air
    * Google Chrome
    * Firefox
    * Safari
* MacBook Pro
    * Google Chrome
    * Firefox
    * Safari
* MacPro
    * Google Chrome
    * Firefox
* Windows 10 Enterprise
    * Google Chrome
    * Mircosoft Edge
* Samsung Galaxy 8
    * Google Chrome
    * Samsung web browser

Additionally, Google Chrome Devtools was used throughout the project to view this website on a number of stimulated mobile, tablet, laptop and desktop devices to ensure compatibility and responsiveness. Devices include Galaxy S5, Pixel 2, Pixel 2 XL, iPhone 5 / SE, iPhone 6/7/8, iPhone 6/7/8 plus, iPhone X, iPad, and iPad Pro.

I tested all features as a non-logged in user, a logged-in user without CRUD rights as well as a logged-in superuser. 

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

#### 1. All Pages
I ensured that:
- All pages extends from the `base.html` page which has the top dark background row with search function, a navbar with links to other parts of the website and a footer with links for policy pages and a section listing my social media sites. Each link was clicked on to ensure the user is directed to the correct page in a a new tab

- All pages are responsive for mobile, tablet and desktop view. The pages were checked extensively across different devices and browsers

- All pages has a page title shown on the browser tab. This was achieved by including a `{% block title %} XXX {% endblock %}` where 'XXX' is replaced by the page title

#### 2. Home Page (The BoardGameStore)
I ensured that:
- The business' brand and name is displayed in the center prominently
- The search function and welcome message is displayed in the center where the user's eyes naturally would focus on
- Four best seller games chosen were displayed along with buttons directing users to read more information on the game or to add the games directly to the shopping cart

#### 3. Add a Game page
I ensured that:
- Each field was left intentionally blank to check for form validation
- The name field was limited to 21 characters and this was checked with inputting more than 21 characters
- UploadCare works for the image upload option
- The 'ADD A GAME' button will create a new game and save it to the database. Also, this new game is displayed under the correct category in the `games.template.html` page
- The 'CANCEL' button will bring the user back to the home page
- This 'ADD A GAME' link is not visible to non-logged in user and logged-in user without CRUD rights. Only a logged-in superuser have this link appear in their navbar

#### 4. Edit Game page
I ensured that:
- The game's name, description, inside box, price and category fields are filled with content from the database
- The 'Image' field shows the correct file name, it is removable and changeable to a different image
- Upon clicking on the 'UPDATE GAME' button, the user is brought to the 'shop page' with a flash message indicating success of the game being updated 
- Upon clicking on the 'DELETE GAME' button, the user is brought to a 'Confirm Delete?' page

#### 5. Confirm Delete? page
I ensured that:
-  A text asking if the user is sure about deleting the game is displayed
- Upon clicking on the 'NO, I CHANGED MY MIND' button, the user is brought to the 'Shop' page
- Upon clicking on the 'YES, DELETE GAME' button, the game is deleted from database and the user is brought the the 'Shop' page with a flash message on top indicating deleting the game was successful

#### 6. Shop page
I ensured that:
- The three categories (Card, Party, Board Games) are displayed with the games in alphabetical order. This makes it easy for the user to locate games
- A click on the game image or the 'MORE INFO' button will bring the user to the 'game information' page
- The 'ADD TO CART' button will add the game to the cart. If the user adds it again, he/she is directed to the 'cart' page where the quantity is shown as '2' (because the user added it twice). The game quantity could be changed in the 'cart' page
- A flash message indicating success is shown on top when the user clicks on the 'ADD TO CART' button

#### 7. Game Information page
I ensured that:
- The correct game is displayed on this page along with the game's description and what is inside the box
- The 'EDIT GAME' button when clicked would take the user to the 'Edit Game' page
- The 'ADD TO CART' button when clicked would add the game to the cart. The user is brought to the 'Shop page' and a flash message would appear on top of the page indicating success of it being added the cart. The cart would show the number being incremented
- The 'VIEW CART' button when clicked would bring the user to the 'cart page'
' The 'BACK TO SHOP' button when clicked would bring the user to the 'shop page'

#### 8. Cart page
I ensured that:
- All the games added to cart are displayed here
- The cart displays the correct number of games added. This is indicated by the number in the brackets () beside the cart
- The least number of quantity is one and for each click on the '+' or '-' button, the quantity is incremented or decremented by one
- Upon clicking on the dustin icon (medium screens and above) or the 'x' icon (mobile screens), the game is removed from the cart
- The 'Subtotal' math is correct; it reflects the quantity of game multiply by the item price
- The 'delivery' charges are /$8 for orders $300 and below. It turns /$0 for orders above /$300
- The 'Grand Total' reflects the adding of all 'Subtotal' price together
- The 'Proceed to checkout' button brings the user to the 'Checkout' page
- The 'Continue shopping' button brings the user to the 'Shop for Game' page

#### 9. Checkout Form page
I ensured that:
- All fields must be filled to be validated
- The 'Credit card number' must be '4242424242424242' to be validated, else a flash error message would be displayed on top of the page
- The 'Security code (CVV)' must be three digits to be validated, else a flash error message would be displayed on top of the page
- The 'Month/Year' must be after this current month, year, else a flash error message would be displayed on top of the page
- Use this information for a success payment:
````
Credit card number: 4242424242424242
Security code (CVV): 456
Month: 4
Year: 2022
````
- I tested some other credit card numbers from the 'Testing for specific responses and errors' from [Stripe](https://stripe.com/docs/testing) to see other kinds of errors being generated. An example would be using these information which would result in a `Your card was declined!` flash message
````
Credit card number: 4000000000009995
Security code (CVV): 123
Month: 1
Year: 2025
````
- Upon clicking on the 'SUBMIT PAYMENT' button, the user is brought to the 'Checkout Success' page
- Upon clicking on the 'BACK TO CART' button, the user is brought to the 'Cart' page
- Upon clicking on the 'BACK TO SHOP' button, the user is brought to the 'Shop' page

#### 10. Stripe Account
I ensured that:
- The payment is reflected in my stripe account and the value is correct
![Stripe account](https://raw.githubusercontent.com/Paddlepop25/codeinstitute-boardgame-store/master/static/images/readmes/tests_md/stripeaccountinfo.png)

#### 11. Checkout Success page
I ensured that:
- A text is displayed thanking the customer for the purchase
- A picture of a winking kitty cat is displayed to put a smile on the user's face
- Upon clicking on the 'BACK TO HOME' button, the user is brought to the home page

#### 12. Contact Us page
![Contact Us email received](https://raw.githubusercontent.com/Paddlepop25/codeinstitute-boardgame-store/master/static/images/readmes/tests_md/email_contact_us.png)

I ensured that:
- Google map API is called and displayed on the game
- The 'Contact Us' form validation works for all fields. I tried empty fields each turn to verify
- Upon clicking on the 'SUBMIT' button, a pseudo email is sent to the user. This is verified from getting an email in the 'sent_emails' folder in the same directory as this django project

#### 13. Register page
![Password Validation](https://raw.githubusercontent.com/Paddlepop25/codeinstitute-boardgame-store/master/static/images/readmes/tests_md/register_account.png)

I ensured that:
- All input fields cannot be empty
- The email address must be a valid email address
- The 'Password' and 'Re-enter password' must match
- Any errors and validation failure will result in error messages shown
- Upon successful registration and on the click of the 'Register' button, the user is brought to the home page where a flash message would indicate that registration was successful

#### 14. Login page
I ensured that:
- The 'register' link would bring the user to the 'Register Account' page
- Both 'username' and 'password' fields cannot be empty, else error messages would be shown
- The 'username' and 'password' fields must match in comparison with records in the database
- If either one field is incorrect, a flash message is shown on top reminding users to input correct case-sensitive username and password
- If both input fields are correct and upon clicking on the 'Login' button, the user is brought to the home page with a flash message indicating success in sigining in as the user
- Upon clicking on the 'Forgot Password' button, the user is brought to the 'Password Reset' page

#### 15. Logout page
I ensured that:
- Upon clicking on the 'LOGOUT' link, the user is brought to a 'Logout' page where the user is given two options
- Upon clicking on the 'LOGOUT' button, the user is brought to the 'Home page' where a flash message is shown indicating the user has successfully logged out
- Upon clicking on the 'CANCEL' button, the user is brought to the 'Shop for Games' page

#### 16. My Account/ User's profile page
I ensured that:
- The username of the logged in user is displayed after 'Hello'
- The 'Reset password' button brings the user to the 'Password Reset' page
- The 'Change password' button brings the user to the 'Change Password' page

#### 17. Password Reset page
![Password Reset email received](https://raw.githubusercontent.com/Paddlepop25/codeinstitute-boardgame-store/master/static/images/readmes/tests_md/email_forgot_password.png)
I ensured that:
- The 'email input' field needed an email for the submit button to work
- Upon clicking on the 'SEND ME INSTRUCTIONS!' button, a pseudo email is sent to the user. This is verified from getting an email in the 'sent_emails' folder in the same directory as this django project. The user is brought to the 'Password Changed Success page' thereafter

#### 18. Password Reset Successful page
I ensured that:
- Upon success submit of form from the 'Password Reset page,' the user is directed to this page where it is stated instructions are emailed to the user

#### 19. Password Change page
![Password Validation](https://raw.githubusercontent.com/Paddlepop25/codeinstitute-boardgame-store/master/static/images/readmes/tests_md/change_password.png)
I ensured that:
- None of the 3 input fields could be empty, if not error messages would be shown
- The 'Old password' must be the exact same one as the user's login password
- The two 'New password' and 'New password confirmation' fields must match
- Upon click on the 'Change my password button,' the user is brought to the 'Password Changed' page

#### 20. Password Changed Successful page
I ensured that:
- The message 'Your password is changed!' is displayed prominently with a picture of a cute puppy
- The 'HOME PAGE' button brings the user back to the home page

#### 21. Terms & Conditions page
I ensured that:
- The user is brought to the 'Terms & Conditions' page where information is displayed

#### 22. Privacy Policy page
I ensured that:
- The user is brought to the 'Privacy Policy' page where information is displayed

#### 23. Shipping and Returns page
I ensured that:
- The user is brought to the 'Shipping and Returns' page where information is displayed

#### 24. 404 Error page
I ensured that:
- Any broken links are directed to this page where a text that says 'Sorry! Something went wrong :(' is displayed along with a picture of a sad kitty cat

## Bugs 

1. I tried adding `\n` or `<br>` to break a long sentence into 2 lines for the flash messages but it didn't work
2. Any email address entered in the 'reset password' page is a success and I tried to validate the form to only the logged in user's email but to no avail
3. The `checkout` button didn't work when I tested this website out on my iphone no matter if I used a `<button>` or `<a>` tag. I read from [here](https://stackoverflow.com/questions/28987034/button-not-working-on-mobile-devices-but-works-on-pc-bootstrap) that the issue could be solved with adding either one of the following in CSS:
````
cursor: pointer;
z-index: 99;
````
I also tried this `onkeypress="return event.keyCode!=13;"` on the html which didn't work.
After a few days of trying, I finally settled on this code which did the trick
````
<input id="checkout_mobile" type="submit" class='btn btn-warning float-right ml-2 mb-2' value="CHECKOUT" />
````

## Further Testing
- In the future, I would like to implement unit testing while building a website of this kind
- I would like to incorporate other fields like booleans and tuples in the forms for testing
- I would like to implement a mail delivery service to further test if emails are delievered when a user request for password change, and also if the auto reply email is generated when a form is submitted from the contact page
- A special acknowledgement and thanks to family and friends for their time to test this website on their device and their invaluable feedback.