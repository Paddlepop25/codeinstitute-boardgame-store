# The BoardGameStore - Testing #

The deployed project 'InstaRamen' is on [Heroku](https://linda-instaramen.herokuapp.com/)

[**Main README.md file**](https://github.com/Paddlepop25/codeinstitute-boardgame-store/blob/master/README.md)

## Automated Testing

### Validating Code

Validation services were used to ensure that the respective codes were valid used to develop the website.

- [W3C Markup Validation Service](https://validator.w3.org/) was used to test HTML code to ensure it was valid code. Errors were shown where there were Jinja codes and this was expected as the latter are not html codes. Aside from these there were no other errors.

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

#### 1. All Pages
I ensured that:
- All pages extends from the `base.html` page which has the top dark background row with search function, a navbar with links to other parts of the website and a footer with links for policy pages and a section listing my social media sites. Each link was clicked on to ensure the user is directed to the correct page.

- All pages are responsive for mobile, tablet and desktop view. The pages were checked extensively across different devices and browsers.

- All pages has a page title shown on the browser tab. This was achieved by including a `{% block title %} XXX {% endblock %}` where 'XXX' is replaced by the page title.

#### 1. Home Page
I ensured that:
- The business' brand and name is displayed in the center prominently.
- The search function and welcome message is displayed in the center where the user's eyes naturally would focus on.
- Four best seller games chosen were displayed along with buttons directing users to read more information on the game or to add the games directly to the shopping cart.

#### 2. Add a Game page
I ensured that:
- Each field was left intentionally blank to check for form validation.
- The name field was limited to 21 characters and this was checked with inputting more than 21 characters.
- UploadCare works for the image upload option.
- The 'ADD A GAME' button will create a new game and save it to the database. Also, this new game is displayed under the correct category in the `games.template.html` page.
- The 'CANCEL' button will bring the user back to the home page.
- This 'ADD A GAME' link is not visible to non-logged in user and logged-in user without CRUD rights. Only a logged-in superuser have this link appear in their navbar.

#### 3. Shop for Game page
I ensured that:
- The three categories are displayed with the games in alphabetical order. This makes it easy for the user to locate games.
- A click on the game image or the 'MORE INFO' button will bring the user to the 'game information' page.
- The 'ADD TO CART' button will add the game to the cart. If the user adds it again, he/she is directed to the 'cart' page where the quantity is shown as '2' (because the user added it twice). The game quantity could be changed in the 'cart' page.
- A flash message indicating success is shown on top when the user clicks on the 'ADD TO CART' button.
-