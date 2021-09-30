# Productivity Tracker
I was inspired to visualize the data that I've been collecting for the past month with my Habit Tracker in Notion. I use Notion daily to track deadlines, plan out obligations, manage finances and spending, and more. I recently started logging personal habits using Notion's tables and checkboxes function. Though Notion's interface is very powerful, I wanted to graphically view the data that I'd been collecting without having to stare at a table full of checkboxes. 

> **Note**: The code for this project was based on how my Notion page was set up [(see here)](https://ibb.co/jfZS8zb). Results may vary based on how each user configures their pages within Notion. 

## Project Conception
Notion's API is the primary driver behind this. Thanks to their easy access with databases and integration tokens, I could gather and visualize the data quite easily. After connecting to the Notion Page, the dates, subjects/topics, and checkbox info were all taken from the table. Next, the data was organized, and eventually plotted. Finally, the results were made accessible in a simple web app using Streamlit's open-source app framework. 

## Customizing Setup 
### Find Your Notion API Token
Go to Notion's API page [here](https://www.notion.so/my-integrations) and follow the step-by-step instructions to create a new integration and find the secret API key. Store this! 

### Connect the Integration to Your Notion Page
First, go to your Notion Page. Then, click on the "Share" button, and invite the integration that you've created with your account so that it has access to the page where your table/board is located. 

### Setting the Correct Variables
Since each Notion Page is different, you'll have to set your database's ID and integration tokens within the code. 

`integrationtoken = .......`

`DATABASE_ID = .......`

Information on finding the database ID can be found [here](https://developers.notion.com/docs/working-with-databases). 

### Git Clone
To clone this repository, run the following line in your command line or Terminal. 

`git clone https://github.com/reeteshsudhakar/productivity-tracker`

Once the integration token and database ID are changed and the code is run, a locally hosted web app will open with the visualized data. 

## To-Do List
* [ ] Exceptions and Error Handling - errors, warnings, etc. 
* [ ] Plotly figure generation
* [ ] Streamlit integration 
