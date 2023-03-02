# Backend for AQI-Heatwave-Forecaster

>Basic Flask application to make model prediction of AQI and Heatwaves for the Tier-2 cites in Telangana.

<br>

## Run the Application

```
set FLASK_APP=run.py
set FLASK_ENV=development
flask run
```


**API-Endpoints**
----

* **URL**

  https://aqi-heatwave-app.azurewebsites.net/api/aqi/getMonthlyAQIPredictions

* **Method:**

  `POST`  
  
*  **URL Params**
   
   None
   
* **Data Params**

   **Required:**
   
   ```

    {
        "City":"city_name"
      
    }
    ```

* **Success Response:**
  
  * **Code:** 200 <br />
    **Content:** 
    ```json
      [{"Date":"2023-03-01","Predictions":86.5634307861},{"Date":"2023-04-01","Predictions":75.4241104126},{"Date":"2023-05-01","Predictions":70.9274902344},      {"Date":"2023-06-01","Predictions":69.1306838989},{"Date":"2023-07-01","Predictions":68.4158325195},{"Date":"2023-08-01","Predictions":68.1319503784},{"Date":"2023-09-01","Predictions":68.01927948},{"Date":"2023-10-01","Predictions":67.9745864868},{"Date":"2023-11-01","Predictions":67.9568557739},{"Date":"2023-12-01","Predictions":67.9498214722},{"Date":"2024-01-01","Predictions":67.9470291138},{"Date":"2024-02-01","Predictions":67.945930481},{"Date":"2024-03-01","Predictions":67.9454879761},{"Date":"2024-04-01","Predictions":67.9453125},{"Date":"2024-05-01","Predictions":67.9452514648}]

    ```



* **URL**

  https://aqi-heatwave-app.azurewebsites.net/api/aqi/getDailyAQIPredictions

* **Method:**

  `POST`  
  
*  **URL Params**

   None
   
* **Data Params**
  
  ```

    {
        "City":"city_name"
      
    }
    ```

* **Success Response:**
  
  * **Code:** 200 <br />
    **Content:** 
    ```json
    [{"Date":"2023-03-03","Predictions":152.5825500488},{"Date":"2023-03-04","Predictions":139.2323303223},{"Date":"2023-03-05","Predictions":134.1151885986},{"Date":"2023-03-06","Predictions":132.167678833},{"Date":"2023-03-07","Predictions":131.4286193848},{"Date":"2023-03-08","Predictions":131.1484375},{"Date":"2023-03-09","Predictions":131.0422821045},{"Date":"2023-03-10","Predictions":131.0020751953},{"Date":"2023-03-11","Predictions":130.9868469238},{"Date":"2023-03-12","Predictions":130.9810638428},{"Date":"2023-03-13","Predictions":130.9788818359},{"Date":"2023-03-14","Predictions":130.9780578613},{"Date":"2023-03-15","Predictions":130.9777374268},{"Date":"2023-03-16","Predictions":130.9776153564},{"Date":"2023-03-17","Predictions":130.9775848389}]
    ```

 

