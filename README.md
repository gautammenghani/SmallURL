# SmallURL
This project contains the solution for URL shortening service problem.

## Solution
The user enters the URL in the textbox and clicks on submit. The app checks if the URL already exists in cache. It computes the shortened URL and returns it.
### Backend and cache
I have used flask in the backend the memcache for caching.

## Steps to setup
1. Install memcached by following the instructions [here](https://www.cyberciti.biz/faq/install-and-configure-memcached-on-ubuntu-linux18-04/)
2. Clone this repo
3. Run the app
    ```flask run```