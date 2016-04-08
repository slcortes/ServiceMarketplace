# ServiceMarketplace
Service Marketplace website for ITC


Create account
•	We have a form that lets the user register for an account with a Cross Site Request Forgery (csrf) token for security. We then have a simple line of code that we could put above any url/view/route that we want to require a login for like creating a service, leaving a review, and taking any action, other than viewing, on a service. 
•	We use a function to determine if they are allowed to bid by checking if they are the owner of the service, which means they cannot bid on the service.
•	The creation of a User using the User model in the database is handled by our framework/language.
