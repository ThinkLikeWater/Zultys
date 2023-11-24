# Setup
## Step 1.
Create your virtual environment
```
python -m venv venv
```
or 
```
python3 -m venv venv
```
Activate it
```
source venv/bin/activate
```

## Step 2.
  ```
  pip install -r requirements.txt
  ```


---
## Step 3
Go to tests/enterprise_media_exchange/test_buttons.py. 

You can use entrypoint: 
 ```
if __name__ == "__main__":
    unittest.main()
  ```
### You can find the downloaded files here tests/enterprise_media_exchange/downloads 
# NOTE:
### Make sure your chromedriver version and Google Chrome version match.
