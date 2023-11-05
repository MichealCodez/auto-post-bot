# Selenium Email Verification Script

This Python script utilizes the Selenium library to automate the process of email verification on a specific website. The script is designed to handle the following tasks:

1. **Accessing a Website**:
   - The script navigates to a target website (`https://milano.bakecaincontrii.com/`) and interacts with elements on the page.

2. **Filling and Submitting Forms**:
   - It fills out various forms, including selecting categories, providing text inputs, and interacting with checkboxes.

3. **Captcha Solving**:
   - The script uses the 2Captcha service to solve captchas encountered during the form submission process.

4. **Email Verification**:
   - The script opens a new browser window and accesses a specified email service (`http://mail.com`) to verify received emails.
   - It logs in to the email account, navigates to the spam folder, opens the verification email, and follows the verification link.

## Prerequisites

Before running the script, ensure you have the following:

- Python installed on your system.
- Selenium library installed (`pip install selenium`).
- Chrome WebDriver downloaded and placed in your system's PATH.
- 2Captcha API key (set as an environment variable or directly in the script).
- Valid email credentials for the email verification process.

## How to Use

1. **Set Environment Variables**:
   - Set the `APIKEY_2CAPTCHA` environment variable to your 2Captcha API key.
   - Set valid email and password credentials in the script for email verification.

2. **Run the Script**:
   - Execute the Python script (`python script_name.py`).
   - The script will automate the process of accessing the website, filling out forms, solving captchas, and verifying emails.

**Note**: Ensure you have proper permissions and comply with the terms of service of the websites you are interacting with using this script. Automated interactions should be performed responsibly and ethically.
