# Beauty Buys Testing 

## Validators 

**[HTML Validator](https://validator.w3.org/)**

To validate the HTML, the deployed URL was tested. One error returned which is captured below. The error relates to <section> within the base.html. This is the area that contains my flash messages, therefore this error may be ignored in this case.

![HTML validator](readme-and-testing-images/html-validator.png)

**[CSS](https://jigsaw.w3.org/css-validator/)**

To validate CSS, the CSS code was copied and checked using direct input. This didn't result in any errors. 

![CSS validator](readme-and-testing-images/css-validator.png)

**[JavaScript](https://jshint.com/)**

To validate JavaScript, the code was copied and checked using direct input. This didn't result in any errors.

![Js validator](readme-and-testing-images/js-validator.png)

**[Python](https://extendsclass.com/python-tester.html)**

To validate Python code, the code was copied and checked by direct input. No errors were found.

![Python validator](readme-and-testing-images/python-validator.png)

## Database Testing 

## Responsive Design

## Problems Encountered 

* While testing my "Reviews" page on multiple devices I noted while using an Ipad Pro that the edit and delete buttons escaped their card
container. To overcome this I used Google Chrome Developer Tools and inspected which element was causing this. I saw that that the card content had a predetermined padding, this was supplied by Materialize. I targeted the class within my CSS to fix the issue. 

* When testing the site using Google Lighthouse, within accessibility it was noted that the images used in the "Home Page" carousel did not have alt attributes, I added this to improve accessibility.