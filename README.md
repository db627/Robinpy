# Robinpy
Robinpy is a Python application designed to interact with Robinhood, utilize OpenAI's API, and send messages using Twilio.

## Getting Started
Prerequisites
Python 3.x
Installation
1. Clone the repository:
git clone [repository-url]

2. Navigate to the project directory:
cd Robinpy

3. Install the required packages using pip:
pip install -r requirements.txt

## Configuration
Before you can run Robinpy, you need to configure your environment variables. Create a .env file in the root directory of the project and populate it as shown below:

ROBIN_USER=your_robinhood_username
ROBIN_PASSWORD=your_robinhood_password
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_account_auth_token
OPENAI_API_KEY=your_openai_api_key
TO_NUMBER=phone_number_where_you_want_messages_sent
FROM_NUMBER=your_twilio_number

### Replace placeholders (your_robinhood_username, your_twilio_account_sid, etc.) with your actual values.

## Running the App
After setting up your environment variables, you can run the app using:
python public/main.py  # Assuming the main script is named 'main.py' and is located inside the 'public' folder.


License
This project is licensed under the MIT License - see the LICENSE.md file for details.

Acknowledgments
a. The Robinhood team for their trading platform.
b. OpenAI for their API.
c. Twilio for their messaging services.
