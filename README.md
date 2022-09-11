# 💼Automated Job Application Bot using Selenium Webdriver of Python

🌟A program which uses Selenium package from Python to automate the process of saving relevant Jobs listings from LinkedIn for future reference. The Bot uses selenium webriver
to load the job posting url then, using the user credibilities signs in to their LinkedIn profile and then saves all the jobs from the mentioned url.

👉In 'main.py' file first the driver path is defined and the user credibilities are stored. Once, the driver is setup the url for job posting is passed to the drivers
'.get()' method and the selenium driver launches a new chrome window with the url loaded.

![Jobs List from mentioned URL](https://github.com/bellaryyash23/Selenium_Automated_JobBot/blob/master/jobs.jpg?raw=true)

👆Job Listing on LinkedIn from the URL👆

👉Next, to save the jobs for future reference we need to sign in which is automated by the bot. Thus, using the credibilities, the bot signs in.

![Jobs List from mentioned URL](https://github.com/bellaryyash23/Selenium_Automated_JobBot/blob/master/sign_in.JPG?raw=true)

👆Sign Window: Credibilities Filled automatically by Bot👆

👉Once signed in then the Job listing page again opens up and now, the bot can click on the job title and save the job listing for user for future reference.
