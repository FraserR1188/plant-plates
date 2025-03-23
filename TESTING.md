# Testing

Plant Plates recipe website has been tested using the following methods:

- [Code Validation](#code-validation)
  - W3C HTML Validator
  - W3C CSS Validator
  - JSHINT Javascript Code Quality Tool
  - Python Validation using VS Code

# Code Validation

## W3C HTML Validator

![W3C HTML Validator](plantplates/static/images/TESTING/w3c-HTML-validator.png)

Plant plates website has passed using [W3C HTML Validator](https://validator.w3.org/) tool.

### W3C CSS Validator

![W3C CSS Validator](plantplates/static/images/TESTING/W3C-CSS-Validator.png)

Plant plates website has passed using [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) tool.

### JSHint Javascript Code Quality Tool

![JShint](plantplates/static/images/TESTING/jshint.png)

Plant plates website passed using [JSHint](https://jshint.com/) JavaScript Code Quality tool.

### Python Validation using VS Code

![Python Validation](plantplates/static/images/TESTING/python-test.png)

- Plant plates website showed a few errors:
  - See future features for unused imported modules.
  - The secure_filname and s3 errors are used throughout the routes.py.

### WAVE Webaim Accessibility Checker

![WAVE Webaim Accessibility Checker](plantplates/static/images/TESTING/WAVE-test.png)

- The was tested on the home page for accessibility using [WAVE Webaim](https://wave.webaim.org/) an no serious issues found. Contrast error was over the transparent image and the errors were emoty links which had icons in them.

### Lighthouse

I used the Lighthouse reports in Google Developer Tools to examine the pages of the website for the following

- Performace
- Accessibility
- Best Practices
- SEO

![Dekstop Mobile](plantplates/static/images/TESTING/desktop-lighthouse.png)

This is the Plant Plates testing for Desktop. Scored well apart from performance. Due to time constraints I could not improve upon this.

![Mobile Lighthouse](plantplates/static/images/TESTING/mobile-lighthouse.png)

This is the Plant Plates testing for Mobile. Scored well apart from performance. Due to time constraints I could not improve upon this.

## Browser Compatibility

The site was tested on Google Chrome, Opera, Mozilla Firefox and Microsoft Edge on the Desktop.

The site was tested on Safari and Google Chrome on mobile.

The site was tested on Safari on iPad.

Timeout issues arose when testing when user were inactive. This may be an issue with Heroku hosting site as there were no issues present on the logs.

## Responsivenss

Responsivity tests were carried out using Google Chrome DevTools. Device screen sizes covered include:

- iPhone SE
- iPhone XR
- iPhone 12 Pro
- Pixel 5
- Samsung Galaxy S8+
- Samsung Galaxy S20 Ultra
- iPad Mini
- iPad Air
- Surface Pro 7
- Surface Duo
- Galaxy Fold
- Samsung Galaxy A51/71
- Nest Hub
- Nest Hub Max

I also personally tested the website on iPhone 13, iPhone 11 and MSI gaming PC with a dual screen.

## Testing User Stories
