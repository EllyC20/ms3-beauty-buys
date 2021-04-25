# Beauty Buys Testing 

## Validators 

**[HTML Validator](https://validator.w3.org/)**

To validate the HTML, the deployed URL for each page was tested. Listed below are any issues encountered, and fixes. There is one reoccuring error message, the error relates to a "section" within the base.html. This is the area that contains my flash messages, therefore this error may be ignored in this case. 

**Home**

![HTML validator](static/testing/html-validator.png)

**Reviews** 

As seen below, errors occured due to two things. The use of "ID" on the review image caused an error, the validator was noting there were multiple elements with the same ID. To fix this I changed the ID to a class. Secondly, the use of a "p" tag within a span was incorrect and affecting the flow of the page. I removed the "p" tag and ensured the span held the same styling as I had intended, this solved the error.

![HTML validator](static/testing/reviews-html-checker.png)

<br>

![HTML validator](static/testing/reviews-html-checker-2.png)

**Log In**

![HTML validator](static/testing/login-validator.png)

**Register**

![HTML validator](static/testing/register-validator.png)

**New Review**

![HTML validator](static/testing/new-review-validator.png)

**Edit Review**

![HTML validator](static/testing/edit-review-validator.png)

**[CSS](https://jigsaw.w3.org/css-validator/)**

To validate CSS, the CSS code was copied and checked using direct input. This didn't result in any errors. 

![CSS validator](static/testing/css-validator.png)

**[JavaScript](https://jshint.com/)**

To validate JavaScript, the code was copied and checked using direct input. This didn't result in any errors.

![Js validator](static/testing/js-validator.png)

**[Python](http://pep8online.com/checkresult)**

To validate Python code, the code was copied and checked by direct input. One error was noted, which can be seen below. I fixed this line error and validated my code for a second time. No errors were noted on the second check.

![Python validator](static/testing/pep-8-one.png)

<br>

![Python validator](static/testing/pep-8-two.png)

<br>

## Database Testing 

 

<br>

## Defensive Design Testing

Detail of form validation, URL input, password, username checks here. 

## Testing User Stories 

Below there are supporting images for each user story to demonstrate how that requirement is fulfilled.

**As a User**

1. 
    - "I want to have the functionality to register an account." 

**A user can register an account using the "Register" page.**

![User Story Testing](static/testing/user-story-test-1.png)

2. 
    - "I want to be able to upload a review for different product categories."

**Within the "New Review" page, a user who has an account can submit the below form to submit a review.**

![User Story Testing](static/testing/form-view-two.png)

3. 
    - "I want to be able to read reviews left by other users."

**On the "Reviews" page any user can read the previous reviews left.**

![User Story Testing](static/testing/user-story-test-3.png)

4. 
    - "I want to be able to delete or edit a review I have made."

**Once signed in, a user can see an edit button on a review they have made. When they click edit they can change any of the information previously provided.**

![User Story Testing](static/testing/edit-function-one.png)

<br>

![User Story Testing](static/testing/edit-function-two.png)

5. 
    - "I don't want other users to be able to edit or delete a review I have made."

**As mentioned above, only when a user signs in do they get access to edit or delete. They may only edit or delete their own reviews.**

![User Story Testing](static/testing/user-story-test-5.png)

6. 
    - "I want to be able to search for particular products."

**A search bar provides the option to search by keyword. If there is a result it will be shown, otherwise a flash message is shown.**

![User Story Testing](static/testing/user-story-test-6.png)

<br>

**As a Site Owner**

1. 
    - "I want to provide a way for users to register an account."

**The "Registration" page provides this function**

![User Story Testing](static/testing/user-story-test-1.png)

2.  
    - "I want the users to have an easy and clear way of submitting a product review."

**The form is simple and explains what information is expected.**

![User Story Testing](static/testing/form-view-two.png)

3. 
    - "I want to provide a functionality where users can provide an image of the product being reviewed."

**Within the form, there's an input section which allows the user to upload a URL link**

![User Story Testing](static/testing/site-owner-testing-1.png)

4. 
    - "I want to have an admin account, this will ensure I can regulate reviews and remove any inappropiate content." 

**There's an admin account which has access to all reviews. The navigation menu option "Manage Reviews" shows only for the admin user, the admin can then visit this page and edit or delete reviews.**

![User Story Testing](static/testing/site-owner-testing-2.png)

<br>

![User Story Testing](static/testing/site-owner-testing-3.png)

<br>

## Responsive Design

**Browser Compatibility** 

| Browser        | Google Chrome | Safari | Firefox | Microsoft Edge | Opera |
|----------------|---------------|--------|---------|----------------|-------|
| Responsiveness | Good          | Good   | Good    | Good           | Good  |
| Appearance     | Good          | Good   | Good    | Good           | Good  |

<br>

**Things To Note**

* On Safari and Firefox, the font is heavier within "Reviews" which makes it appear that the text colour is darker. On Firefox only, the colour palette of the navigation bar and the "Register" and "Log In" buttons, appears lighter.

<br>

**Responsiveness** 

* To test the below sizes, a combination of Google Chrome Developler Tools was used along with [Responsive Web Design Checker](https://www.responsivedesignchecker.com/)

**Large Device Sizes**

| Screen Size       | 1920 x 1080 | 1920 x 1200 | 1920 x 1080 | 1600 x 900 | 1440 x 900 |
|----------------|---------------|--------|---------|----------------|-----
| Renders As Expected | Yes | Yes  | Yes   | Yes  | Yes  |
| Images    | Good          | Good   | Good    | Good           | Good  |

<br>

**Medium Device Sizes**

| Screen Size       | 768 x 1024 | 1366 x 1024 | 600 x 960 | 1024 x 768 | 800 x 1280 |
|----------------|---------------|--------|---------|----------------|-----
| Renders As Expected | Yes | Yes   | Yes    | Yes | Yes |
| Images    | Good          | Good   | Good    | Good           | Good  |

<br>

**Small Device Sizes**

| Screen Size       | 320 x 568 | 414 x 736 | 360 x 640 | 411 x 731 | 280 x 653 |
|----------------|---------------|--------|---------|----------------|-----
| Renders As Expected | Yes | Yes   | Yes    | Yes | Yes |
| Images    | Good          | Good   | Good    | Good           | Good  |

<br>

* Testing of all features, nav, footer, links, search function, all pages to be tested here. 

* Lighthouse summary of testing here.

**Features Testing** 

**Home Page**

While testing the Home page I expect the following things to occur;

* The navigation bar should collapse to a mobile side navbar at any screen size below 993 px. 
    - This was tested using Google Chrome Dev Tools, an Iphone 8 and an Ipad Pro. These checks confirmed the expected behaviour. 

* The carousel should on touch screen devices be "finger scrollable" and on desktop or devices without a touch screen function the user can click the image to scroll.
    - This was tested on a Macbook Air, an Ipad Pro and an Iphone 8. These check confirmed the expected behaviour. 

**Reviews**

While testing the Reviews page I expect the following things to occur;

* The search function should accept letters and numbers and not lone spaces. When a product is found from the keyword searched, it should be displayed. If there are no products matching the keyword search the user should be alerted to this. 
    - This was tested by visiting the deployed site and attempting to search for a product, an error occured which is detailed in problems encountered. Once fixed, I searched again and got the expected results. 
* There should be pagination at the bottom of the page displaying page numbers allowing the user to navigate easily. There should be six reviews per page. 
    - This was tested by visiting the deployed site and visually inspecting this. A visual inspection confirmed pagination was there. I added 5 "testing" reviews to ensure pages would be added as the reviews increased and this behaviour was confirmed. 

**Register**

While testing the Register page I expect the following things to occur;

* The user should be asked to provide a username and password. The username and password must match a pattern that accepts letters and numbers and no spaces.
    - This was tested by visiting the deployed site and attempting to invalid usernames. I attempted to register a username with spaces only and this was not allowed.
    - I attempted to register a password with spaces only and this was not allowed.
    - I attempted to register a username and a password containing a space and this was not allowed.
* After a successful registration the user should be directed to their new profile. 
    - This was tested by registering an account on the deployed site and visually inspecting what happened. Once registered the user is taken to their profile with a flash message informing them their registration was successful. 
* A user should not be able to register an account with a username that is already registered. A flash message is expected to inform the user that this username is already in use, and they should be redirected to the register page again.
    - This was tested by visiting the deployed site and attempting to register with a username I already knew was in use. This confirmed the expected behaviour.

**Log Out**

While testing the Log Out function I expect the following things to occur;

* The user once registered or logged in can click log out. Once they click log out I expect the user to be logged out and taken to the "Log In" page with a flash message informing them that they have logged out. 
    - This was tested by visiting the deployed site, signing out and visually inspecting the resulting action. This confirmed the expected behaviour.

**Log In**

While testing the Log In page I expect the following things to occur;

* The user should be asked to input their username and password. If they are successful they should be taken to their profile, or if their username or password is incorrect they should be informed of this and redirected to the log in page. 
    - This was tested by visiting the deployed site and attempting to sign in with a correct username and incorrect password, this resulted in a flash message stating "Incorrect Username And/Or Password". 
    - I then tried an incorrect username with a correct password, and recieved the same flash messsage. This is as expected, the user should not know if it is an incorrect username or password specifically at any point as this could lead to a security risk. 
    - The testing confirmed the expected behaivour. 

**Profile**

While testing the Profile page I expect the following things to occur;

* The user who is logged in should be shown their own reviews within their profile. The displayed reviews should have the option to edit or delete. 
    - This was tested by visiting the deployed site, signing in and visually inspecting the results. This confirmed the expected behaviors.
* By clicking the edit button the user should be taken to edit their review. 
    - This was tested by visiting the deployed site, signing in and visually inspecting the results. This confirmed the expected behaviors.
* By clicking the delete button the user should be asked do they want to delete the review. The user should be able to confirm or cancel the request. 
    - This was tested by visiting the deployed site, signing in and visually inspecting the results. This confirmed the expected behaviors.

## Problems Encountered 

* While testing my "Reviews" page on multiple devices I noted while using an Ipad Pro that the edit and delete buttons escaped their card
container. To overcome this I used Google Chrome Developer Tools and inspected which element was causing this. I saw that that the card content had a predetermined padding, this was supplied by Materialize. I targeted the class within my CSS to fix the issue. 

* When testing the site using Google Lighthouse, within accessibility it was noted that the images used in the "Home Page" carousel did not have alt attributes, I added this to improve accessibility.

* When testing the search function of the review page I had not correctly implemented pagination within the search function. This resulted in an error when attempting to search for a product. The error was resolved by correctly updating the search function.