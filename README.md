# Azent-API

--------------------- Insert API ------------------------------------------

Insert API is used to create records

Request URL - http://azent.us-east-2.elasticbeanstalk.com/insert

Method  - POST

Sameple Request - 

{
    "alpha_two_code": "US",
    "country": "United States ",
    "domain": "harvard.edu",
    "name": "Harvard University",
    "web page": "https://www.harvard.edu/"
}

Sample Response - 

{
  "id": "XXXXX",
  "record": "added",
  "success": "true"
}

--------------------- Update API ------------------------------------------

Update API is used to update existing records

Request URL - http://azent.us-east-2.elasticbeanstalk.com/update

Method  - PUT

Sameple Request - 

{
    "alpha_two_code": "US",
    "country": "USA",
    "domain": "harvard.edu",
    "name": "Harvard University",
    "web page": "https://www.harvard.edu/"
}

Sample Response - 

{
  "id": "XXXXX",
  "record": "updated",
  "success": "true"
}

--------------------- Delete API ------------------------------------------

Delete API is used to delete existing records

Request URL - http://azent.us-east-2.elasticbeanstalk.com/delete

Method  - DELETE

Sameple Request - 

{
    "alpha_two_code": "US",
    "country": "USA",
    "domain": "harvard.edu",
    "name": "Harvard University",
    "web page": "https://www.harvard.edu/"
}

Sample Response - 

{
  "id": "XXXXX",
  "record": "deleted",
  "success": "true"
}

--------------------- Read API ------------------------------------------

Read API is used to list all records

Request URL - http://azent.us-east-2.elasticbeanstalk.com/read

Method  - GET

Sample Response - 

  [
  {
    "alpha_two_code": "US",
    "country": "United States ",
    "domain": "harvard.edu",
    "id": "harvarduniversity",
    "name": "Harvard University",
    "webpage": "https://www.harvard.edu/"
  },
  {
    "alpha_two_code": "IN",
    "country": "INDIA ",
    "domain": "iit.edu",
    "id": "iit",
    "name": "IIT",
    "webpage": "https://www.iit.edu/"
  },
  {
    "alpha_two_code": "US",
    "country": "United States of america",
    "domain": "acu.edu",
    "id": "mit",
    "name": "abilene christian university ",
    "webpage": "https://www.acu.edu/"
  }
]


--------------------- Search API ------------------------------------------

Search API is used to search existing records 

Request URL : http://azent.us-east-2.elasticbeanstalk.com/search

Method  : GET

Parameters :

search_term     - name                       - mandatory

country_code    - alpha_two_code             - optional

end_of_domain   - end of domain (.edu or.us) - optional

Note - use country_code or end_of_domain

Sample URL - http://localhost:5000/search?search_term=iit

Sample URL - http://localhost:5000/search?search_term=iit&country_code=in

Sample URL - http://localhost:5000/search?search_term=iit&end_of_domain=.edu


Sample Response- 

[
  {
    "alpha_two_code": "IN",
    "country": "INDIA ",
    "domain": "iit.edu",
    "id": "iit",
    "name": "IIT",
    "webpage": "https://www.iit.edu/"
  }
]

