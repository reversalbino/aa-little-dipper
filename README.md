# Little Dipper

<!-- # <img src="/public/static/images/logo.jpg" alt="profile page for logged-in user wireframe" style="width:50px;"/>   MoOA - *Museum of Online Art*  -->


<!-- ## Table of Contents
  - [Description](#description)
  - [Index](#index)
  - [Link to live site](#link-to-live-site)
  - [Technologies](#technologies)
  - [Getting Started](#getting-started)
  - [Demo](#demo)
 -->
 
## Link to live site

Hosted on Heroku: [Little Dipper](https://little-dipper.herokuapp.com/)

## Description

Little Dipper is a platform where users can share and comment on images. Little Dipper is clone of flickr.

## Index
| [Features List](https://github.com/reversalbino/aa-little-dipper/wiki/Features) | [Database Schema](https://github.com/reversalbino/aa-little-dipper/wiki/DB-Schema) | [User Stories](https://github.com/reversalbino/aa-little-dipper/wiki/User-Stories) | [Wireframes](https://github.com/reversalbino/aa-little-dipper/wiki/Wireframes) |




## Technologies

Little Dipper was built using the following technologies:
<br>
<br>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original-wordmark.svg" style="width:60px;" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original-wordmark.svg" style="width:60px;" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/redux/redux-original.svg" style="width:60px;" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg" style="width:60px;" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original-wordmark.svg" style="width:60px;" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlalchemy/sqlalchemy-original.svg" style="width:60px;" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/amazonwebservices/amazonwebservices-original-wordmark.svg" style="width:60px;" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-plain-wordmark.svg" style="width:60px;" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-plain-wordmark.svg" style="width:60px;" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" style="width:60px;" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original-wordmark.svg" style="width:60px;" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/heroku/heroku-plain-wordmark.svg" style="width:60px;" />



## Getting Started
To see Little Dipper live, please click the link provided above.
To run Little Dipper locally, please follow these steps:
`DISCLAIMER: you must be able to create an AWS S3 bucket in order to properly store images/audio files that are uploaded to the site. Upload functionality will not work without it`
  <li>Clone the repository with  </li> 
  
    git clone https://github.com/reversalbino/aa-little-dipper.git
    
  <li>Create a database and database user. If using psql, the commands would be</li>
  
    psql
    CREATE USER hologram_app WITH PASSWORD <password> CREATEDB;
    CREATE DATABASE little_dipper_dev WITH OWNER little_dipper_app;
    
  <li>Navigate to the backend folder and install python packages </li>
  
    pipenv install
    pipenv shell
  
  <li>Create and seed database with </li>
  
    flask db upgrade
    flask seed all
    
  <li>Start the server with </li>
  
    flask run
    
  <li>Next, navigate to the react-app folder and run </li>
  
    npm install
    
  <li>Start the app with </li>
  
    npm start
    
  <li>You should now have Little Dipper running locally!</li>
  
<img width="1777" alt="Screen Shot 2022-06-13 at 2 29 00 PM" src="https://user-images.githubusercontent.com/64238938/173440074-71560e93-6ed8-4688-822f-701cee6ac8bb.png">
<img width="1773" alt="Screen Shot 2022-06-13 at 2 28 43 PM" src="https://user-images.githubusercontent.com/64238938/173440099-68c4ff3c-6e30-41c1-8a02-2d2242c04be1.png">
<img width="1784" alt="Screen Shot 2022-06-13 at 2 29 51 PM" src="https://user-images.githubusercontent.com/64238938/173440104-e826c4fa-41ff-44ca-ad96-1371e35c0f2b.png">
<img width="1760" alt="Screen Shot 2022-06-13 at 2 29 20 PM" src="https://user-images.githubusercontent.com/64238938/173440109-da216acd-523c-4de7-94e2-ba8ea4beee0b.png">
<img width="1785" alt="Screen Shot 2022-06-13 at 2 29 11 PM" src="https://user-images.githubusercontent.com/64238938/173440112-0e14704a-5b43-410e-86c6-f7b7bfce4be5.png">

## Features
  <li>Upload images</li>
  <li>Comment on images</li>
  <li>Add tags to images</li>
  <li>Search images by tags and/or title</li>
  
# little-dipper-staging
