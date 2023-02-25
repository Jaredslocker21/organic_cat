## This is a Document to display tests such as 
* Navigation Links
* Footer Link 
* Py Linter Validator
* Lighthouse Page Analayzer 
* HTML Validator
* CSS Validator

## Navigation Links
All of these links were tested by myself, friends, close and far and passed. 

 * Home - index.html and base.html
 * About - about.html
 * Register - django template signup.html
 * Login - djangop template login.html
 * Logout - django template logout.html

 ## Footer Links 
 All footer Links were tested and open to another tab with their respective URL 
  * FACEBOOK
  * TWITTER 
  * INSTAGRAM
  * YOUTUBE
  * LINKED IN 
  * GITHUB



## Security Tests are located in the [README.md](README.md) File under the Security Tests Section.

## Testing messages coinside with the displays in the [README.md](README.md) Alert Section.


### Py Linter

All pythone pages were run through the official [Code Institute Python Linter](https://pep8ci.herokuapp.com/) validator to ensure all code was pep8 compliant. Some errors were shown due to blank spacing and lines too long, 1 line instead of 2 expected. All of these errors were resolved and code passed through validators.
 
 * admin.py 

 All passed 

| checkout | [CI Py linter](docs/test_images/checkout-admin-lint.png)

| contact | [CI Py linter](docs/test_images/contact-admin-lint.png)

| offers | [CI Py linter](docs/test_images/offers-admin-lint.png)

| products | [CI Py linter](docs/test_images/products-admin-lint.png)

| reviews | [CI Py linter](docs/test_images/reviews-admin.png)
 
 * apps.py

 All passed 

| checkout | [CI Py linter](docs/test_images/checkout-apps-lint.png)

| contact | [CI Py linter](docs/test_images/contact-apps-lint.png)

| products | [CI Py linter](docs/test_images/product-apps-lint.png)

| profiles |[CI Py linter](docs/test_images/profile-apps-lint.png)

| reviews | [CI Py linter](docs/test_images/reviews-apps-lint.png)

 * forms.py

| checkout | [CI Py linter](docs/test_images/formspy.png)

| contact | [CI Py linter](docs/test_images/checkout-forms-lint.png)

| product | [CI Py linter](docs/test_images/product-forms-lint.png)

| profile | [CI Py linter](docs/test_images/profiles-forms-lint.png)

| reviews | [CI Py linter](docs/test_images/reviews-forms-lint.png)

* urls.py

All passed 
 
| cart | [CI Py linter](docs/test_images/linter-urls-cart.png)

| checkout | [CI Py linter](docs/test_images/checkout-forms-lint.png)

| contact | [CI Py linter](docs/test_images/checkout-urls-lint.png)

| ecom | [CI Py linter](docs/test_images/)

| home | [CI Py linter](docs/test_images/home-urls-lint.png)

| products | [CI Py linter](docs/test_images/products-urls-lint.png)

| profiles |[CI Py linter](docs/test_images/profiles-urls-lint.png)

| reviews | [CI Py linter](docs/test_images/reviews-urls-lint.png)

* models.py 

All passed 
 
| cart | [CI Py linter](docs/test_images/adminpy.png)

| checkout | [CI Py linter](docs/test_images/checkout-models-lint.png)

| contact | [CI Py linter](docs/test_images/checkout-models-lint.png)

| offers | [CI Py linter](docs/test_images/offers-models-lint.png)

| products | [CI Py linter](docs/test_images/products-models-lint.png)

| profiles |[CI Py linter](docs/test_images/profile-models-lint.png)

| reviews | [CI Py linter](docs/test_images/reviews-models-lint.png)

* views.py 

All passed 
 
| cart | [CI Py linter](docs/test_images/views-linter-cart.png)

| checkout | [CI Py linter](docs/test_images/checkout-views-lint.png)

| contact | [CI Py linter](docs/test_images/contact-views-lint.png-views-lint.png)

| home | [CI Py linter](docs/test_images/home-views-lint.png)

| products | [CI Py linter](docs/test_images/products-views-lint.png)

| profiles |[CI Py linter](docs/test_images/profile-views-lint.png)

| reviews | [CI Py linter](docs/test_images/reviews-views-lint.png)


* widgets.py 
| products widgets | [CI Py linter](docs/test_images/products-widgets-lint.png)

* context.py

| cart | [CI Py linter](docs/test_images/contextcart.png)

* test.py

| Home | [CI Py linter](docs/test_images/home-test-lint.png)

* settings.py

| ecom | [CI Py linter](docs/test_images/ecom-settings-lint.png)

* stripe webhooks in checkout

| stripe webhooks | [CI Py linter](docs/test_images/checkout-webhooks-lint.png)




## Lighthouse Performance

![Light House Performance  ](docs/test_images/lighthouse-report.png)

## HTML Validator 

All pages were run through the [w3 HTML Validator](https://validator.w3.org/). Initially there were some errors due to stray script tags, misuse of headings within spans and some unclosed elements. All of these issues were corrected and all pages passed validation.

Due to the django templating language code used in the HTML files, these could not be copy and pasted into the validator and due to the secured views, pages with login required or a secured view cannot be validated by direct URI. To test the validation on the files, open the page to validate, right click and view page source. Paste the raw html code into the validator as this will be only the HTML rendered code.

* base.html and index.html were done at the same time as index.html rests in base.html

![HTML Validator](docs/test_images/base-index.png)


* signup was tested

![HTML Validator](docs/test_images/signinhtml.png)

* Log In was tested

![HTML Validator](docs/test_images/login.png)

* Register

![HTML Validator](docs/test_images/registerhtml.png)

* About 

![HTML Validator](docs/test_images/about-html.png)


## CSS Validator

* CSS Validator

![CSS Validator](docs/test_images/cssval.png)


