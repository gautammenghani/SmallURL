# SmallURL
This project contains the solution for URL shortening service problem.

## Solution
The user enters the URL in the textbox and clicks on submit. The app checks if the URL already exists in cache. It computes the shortened URL and returns it.
### Backend and cache
I have used flask in the backend the memcache for caching.

## Steps to setup
### Without docker
1. Install memcached by following the instructions [here](https://www.cyberciti.biz/faq/install-and-configure-memcached-on-ubuntu-linux18-04/)
2. Clone this repo
3. Run the app
    ```flask run```

### With docker
1. Run the commands
 ```docker build .```
```docker run -p 5000:5000 -p 11211:11211 <image_id>```

## Run the tests
To run the tests, run the following command from root of the repo
```python3 -m pytest```
