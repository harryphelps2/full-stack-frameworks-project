# Art Selling Site

## Progress log

Added urls for password reset. Need to read the documentation and add templates to complete the 
registration fuctionality. Target: Have working registration functionality by tomorrow night (4th)

[![Build Status](https://travis-ci.org/harryphelps2/full-stack-frameworks-project.svg?branch=master)](https://travis-ci.org/harryphelps2/full-stack-frameworks-project)

The purpose of the site is to sell the works of a fictional artist, Enrique Filipez. He wants to sell small canvases for a set price and have 
a place for users to place bids in for larger works. There will be a blog on painting technique that you can access if you are logged in
and have voted for Enrique's next work. They'll also be a form to commision Enqrique to paint for you. The user will be able to upload an image to 
be painted, choose a style and add extra comments. The commision page will show a line graph of all projects Enqrique is working on and when, and will give the user an estimated completion date for a type of work. The user will be able to see the estimated completion date on their profile page and be able to get update throughout the day from Enqriue by pictures of the piece in progress. The use will be able to message Enrique to provide feedback. The 
profile page will show the user's gallery/wall showing what works they have purchased and which are in progress and ideas for next pieces to buy.

## Database Statements

As Enrique Filipez (the super user) I want to be able to sell my art prints for a fixed price to get a set level of income.

I want to receive commisions and to set expectations for completion.

I want to recieve feedback from my followers about which piece I should complete next.

I want to promote my artwork.

As a user I want to purchase prints.

As a user I want to bid for original of art.

As a user I want a profile page where I can see the progress of my artworks, my bids and previous purchases.

As a user I want to commission Enrique to paint for me.

I want to upload a photo and example material with comments on the style I want it painted in.

I want to know how long it is going to take.

I want to be able to feedback to Enqriqueon how it is going.

As a user/art-lover I want to read a blog by the artist with critical studies and technique insight.

## Database models

### User

    1. Name

    2. Email address

    3. Address

### Print

    1. Title

    2. Description

    3. Size

    4. Price

    5. Instock

    6. Image

### Original

    1. Title

    2. Description

    3. Size

    4. Price

    5. Instock

    6. Image

    7. Auction start date

    8. Auction end date

    9. Current highest bid

### Commission

    1. Title

    2. Description

    3. Source img

    4. Canvase size

    5. Proposal image

    6. Price

    7. Target end date

    8. Customer approved

    9. Customer approved date

    10. Deposit paid

    11. Deposit paid date

    12. Completed

    13. Completed date

    14. Full amount paid

    15. Full amount paid date

### Feedback

    1. UserId

    2. CommissionId

    3. Image

    4. Date

    5. Comment

## Apps to Build

1. Accounts - login, logout, forget password, register, profile page.

2. Cart - current session cart, add to cart, remove from cart, total, go to checkout.

3. Checkout - enter card details and address details to purchase cart contents.

4. Home - render a homepage.

5. Commission - upload photo, submit, show estimated completion time, pay deposit, feedback to Enrique, timetable of free dates.

6. Bid - choose amount higher than current bid to bid for, time until end of auction.

7. Blog - vote for next work to access.

## Set-up

1. Set up virtual environment

```pip install virtual env```

Go to directory for project and type:

```virtualenv .```

then

```source ./bin/activate```

2. Install django

```pip install django```

Style guide 

We use the BEM naming convention