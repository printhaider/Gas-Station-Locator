# Gas-Station-Locator
This is a script that demonstrates how to use the Google Maps API to search for gas stations near a specific location.

## Prerequisites

Before running the script, you need to have a Google Maps API key. Follow the steps below to obtain one:

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or select an existing one.
3. Enable the "Places API" for your project.
4. Create an API key.
5. Copy the API key.

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/your-repo.git
2. Install The required Python Libraries: pip install -r requirements.txt

## Usage

Open the script main.py in a text editor.

Replace 'YOUR_API_KEY' in the script with your actual Google Maps API key.

Save the changes.

Run the script: python main.py

Follow the prompts to enter your Google Maps API key and see the results.

## Script Explanation

The script does the following:

Takes user input for the Google Maps API key.
Initializes the Google Maps client with the provided API key.
Defines a location to search for gas stations.
Sends a request to the Places API to get a list of gas stations near the specified location.
Defines a method to output the results and prints gas station details including names, vicinity, and price levels.

## Disclaimer
This example is for educational purposes only. Make sure to handle sensitive information (such as API keys) securely and follow best practices when developing applications.




   
