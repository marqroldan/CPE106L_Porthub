# Porthub
 
 
XML Legal Document Utility
Software Design Document
 
Version <1.0>
 
### Ang, Mark Christian
### Deveraturda, Gabriel Q.
### Ligsay, Angel Mikaela P.
### Perez, John Jacob C.
### Reyes, Jarold Rendell F.
### Taguibao, Karl Richmond C.
### Umotoy, Allan Paul A.
 
### 2020-04-25

 
# Software Design Document
## 1 Introduction
Computer parts and accessories are a niche in today’s ever evolving online markets. Even with online sellers such as shoppee, Lazada, and Amazon, many of the major online retailers house a variety of products that include all sorts of things with gadgets only being one of many aspects they have and most gadgets consists of the newest phone and other hand held accessories that majority of the population are interested in and they seldomly sell highly specific computers parts of the tech savvy and this project would like to address that problem of not having a niche online market that houses everything related to computer parts and accessories that major online sellers deem too niche to include in their inventories. This program is essentially a store program similar to that of Lazada and Shoppee but for computer enthusiasts alike as its listing would only comprise of various computer components. 
.
### 1.1         Purpose
The purpose of the Porthub software is for providing an effective design and system to allow the user to proceed with understanding of Graphical User Interface (GUI), data handling, database access and structure and make a sample store program using python. The program will also provide some understanding and importance of computer components which is essential in the Computer Engineering program and visualize it in a familiar tone of visuals.
 
### 1.2         Scope
The scope of this software is limited to the six products available in the program which will serve as a prototype and fundamentals in a non-physical, online-store as well as having the availability to only five stocks of each product. During the checkout, they do not ask for the credit card detail nor address nor how it will be delivered as this is a program to show the GUI side of the online store.
 

### 1.3         Definitions, Acronyms, and Abbreviations
·         Online Store – These are platforms which aim to provide goods and services to customers using the internet.
·         Graphical User Interface – It is a type of user interface where instead of using text-based inputs for interaction, for example, commands, there are graphical methods for interaction like using the mouse cursor and images.
·         Computer Engineering – A branch of engineering which deals with computer systems and the development of hardware and software by combining computer science and electronic engineering.
·         Cart – It is where the products that the customer is planning to buy, is stored. It shows the names of the products and their respective prices and the total balance to pay.
 
### 1.4 Reference
Bike Store and Blog Project <https://tinyurl.com/vuf8k5h>
### 1.5         Overview
The Software Design Document is divided into 5 sections with various subsections. The
sections of the Software Design Document are:
#### 1 Introduction
#### 2 Glossary
#### 3 Use Cases
#### 4 Design Overview
#### 5 System Object Model
## 	2  	Use Cases
### 2.1         Actors
#### 2.1.1	Customer User
#### 2.1.1.1        Information: The customer will be the users of this application. This is an abstraction of the users that perform similar action such as (1) logging in into the platform, (2) signing into the platform by signing up with their details, (3) view the six products available, (4) going to individual pages of the product to have an enhanced inspection on the product, (5) adding a product to the cart in a ready state to be purchased, (6) executing purchase of a product.
### 2.2         List of Use Cases
#### 2.2.1	Customer User Cases
#### 2.2.1.1        Sign-up/ Register user
#### 2.2.1.1.1           Enter first name for registration
#### 2.2.1.1.2           Enter last name for registration
#### 2.2.1.1.3           Enter address for registration
#### 2.2.1.1.4           Enter username for registration
#### 2.2.1.1.5           Enter contact number for registration
#### 2.2.1.1.6           Enter email for registration
#### 2.2.1.1.7           Enter password for registration
#### 2.2.1.2        Login user using password and username
#### 2.2.1.3        Show the products
#### 2.2.1.3.1           Enter the individual product pages
#### 2.2.1.3.2           Add product to cart
#### 2.2.1.3.3           Make a comment on a product
#### 2.2.1.4        Enter the cart
#### 2.2.1.4.1           Checkout the products
#### 2.2.1.4.2           Show the total amount
#### 2.2.1.5        Log out user
 
#### 2.3         Use Case Diagram
  

#### 2.4         Use Cases

### 3  	Design overview
#### 3.1         Introduction
 	The section will show the brief overview of the designer. The system architecture will show the application that has a Graphical User Interface (GUI) using Pyqt, various interactions acting as the Facade and text files to store the current user, and a connection to a database using SQLite. The GUI is the main access point for the application where the user can interact with the online-store. The store is very dependent on the database because that is where all the data is kept of the store’s products, product’s comment and users of the shop.
#### 3.2         System Architecture
##### 3.2.1 Overall structure for the PortHub system 

#### 3.3         System Interfaces
##### 3.3.1 External User Interface Requirements
##### 3.3.1.1 User Interfaces
	The user interface for the system will allow the user to easily access the login and sign-up page before entering into the Homepage of the product. Here the user is presented with the main functions which is the store itself, where the user can view all the available products and make purchases. The interface has buttons with respect to their function (such as backing or adding to cart), this will allow the user for easy navigation in the store and will only need a mouse to travel through pages, but also type in comments if they choose to do so.
##### 3.3.1.2 Software Interfaces
	The software will interface with the system’s database to pull data from it and push data to update it, the connection will be an sqlite3 to an SQLite database as well as keeping the user to a file to understand who is currently using the app on that computer and the cart to save the current unpushed data.
#### 3.4         Constraints and Assumptions
#### 3.4.1 List Assumption
#### 3.4.1.1 It is assumed that the database is currently an Sqlite database which means everything is for local uses and uploads. This is of course because it’s a simulation of an online store.
#### 3.4.2 List of Dependencies
#### 3.4.2.1 This application requires the standard python libraries as well as sqlite3.

## 4  	System object Model
### 4.1         Introduction
 	The System object model will describe the subsystems used in the project. This will overall show the manner and relationship of each class, specifically the pages that the pyqt will provide as each class contains a window.
#### 4.2         Subsystems
	
##### 4.2.1 Relationships

#### 4.3         Subsystem Interfaces
##### 4.3.1 loginCheck : The loginCheck function reads the input from both the username line edit and the password line edit then checks the porthub database, specifically the users table, to see if the username and password matches the records. If there is one result, it opens the main window but if there is no match, it shows the user a message box. 
##### 4.3.2 signupCheck : This function opens the signup window for the user to enter new data into the users table. 
##### 4.3.3 signUpClick : This function reads all the entries of the user in each separate line edit and stores them into the user table of the porthub database. In doing so, the user may now be able to login using their newly created account.
##### 4.3.4 showMessageBox: This function shows a message box. This function is usually called with parameters including the title of the message box and the message to be displayed as well. 
#### 4.3.5 retranslateUI : The interfacere will start to translate the sequence and the details in the file.
#### 4.3.6 ArticleShow(1-6) : Open the product window of the number fitted in and read from a button input.
#### 4.3.7 addCart : The interface will add the product to the cart file.
#### 4.3.8 COut : This interface is done when the checkout button is pressed, this will start the checkout process in the checkout window.

[Link to diagrams](https://tinyurl.com/yd24qxyf)
