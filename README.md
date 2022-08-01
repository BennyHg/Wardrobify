# Wardrobify

Team:

* Benny Huang - Hats microservice
* Yehsun Kang - Shoes microservice

## Design

## Shoes microservice

Explain your models and integration with the wardrobe
microservice, here.
1.  create model.py : Shoes model tracks 
                    its manufacturer, 
                    its model name, 
                    color, 
                    a URL for a picture, 
                    the bin in the wardrobe where it exists.

2. create views.py:  List of the shoes 
                 Detail of the each sheoes

3. crate RESTful APIs to get a list of shoes, create a new shoe, and delete a shoe in insomnia / interact with Bin resources.

4. create poll.py : The existing Wardrobe API can be accessed from my polling service on port 8000. 
                    The service's poller will poll the base URL http://wardrobe-api:8000.

5. create React component(s) to show a list of all shoes and their details.
6. create React component(s) to show a form to create a new shoe.
7. provide a way to delete a shoe.
8. route the existing navigation links to the components.                    



## Hats microservice

I'll probably begin the microservice by first creating the model and encoder that will contain the Hats data.
Detail model -- Each hat/shoe should have its own fabric, style name, picture_url, color, location in the wardrobe
List model -- Hats should have name, picture_url

