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

**[Python](https://extendsclass.com/python-tester.html)**

To validate Python code, the code was copied and checked by direct input. No errors were found.

![Python validator](static/testing/python-validator.png)

<br>

## Database Testing 

Database testing here. 

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

## Problems Encountered 

* While testing my "Reviews" page on multiple devices I noted while using an Ipad Pro that the edit and delete buttons escaped their card
container. To overcome this I used Google Chrome Developer Tools and inspected which element was causing this. I saw that that the card content had a predetermined padding, this was supplied by Materialize. I targeted the class within my CSS to fix the issue. 

* When testing the site using Google Lighthouse, within accessibility it was noted that the images used in the "Home Page" carousel did not have alt attributes, I added this to improve accessibility.