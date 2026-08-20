# I HAVE ALREADY DEPLOY ON RENDER FOR GENERATED A LIVE LINK THIS IS ONLY TRAIL FACE THERE DTREAMLIT UI IS NOT WORKING   
# import streamlit as st
# import requests


# # ============================================================
# # PAGE CONFIGURATION
# # ============================================================

# st.set_page_config(
#     page_title="Food Delivery Time Predictor",
#     page_icon="🍴",
#     layout="wide",
#     initial_sidebar_state="collapsed"
# )


# # ============================================================
# # CUSTOM CSS
# # ============================================================

# st.markdown(
#     """
#     <style>

#     /* Main application */
#     .stApp {
#         background-color: #0b0f14;
#         color: #f5f7fa;
#     }

#     /* Main container */
#     .block-container {
#         max-width: 1200px;
#         padding-top: 2.5rem;
#         padding-bottom: 3rem;
#     }

#     /* Header */
#     .main-title {
#         font-size: 2.4rem;
#         font-weight: 700;
#         letter-spacing: -0.8px;
#         margin-bottom: 0.3rem;
#         color: #ffffff;
#     }

#     .subtitle {
#         color: #8e98a7;
#         font-size: 1rem;
#         margin-bottom: 2rem;
#     }

#     /* Section title */
#     .section-title {
#         font-size: 1.15rem;
#         font-weight: 600;
#         color: #ffffff;
#         margin-top: 1rem;
#         margin-bottom: 1rem;
#     }

#     /* Prediction card */
#     .prediction-card {
#         background: #111720;
#         border: 1px solid #252d38;
#         border-radius: 14px;
#         padding: 28px;
#         margin-top: 20px;
#         text-align: center;
#     }

#     .prediction-label {
#         color: #8e98a7;
#         font-size: 0.9rem;
#         margin-bottom: 8px;
#     }

#     .prediction-value {
#         color: #ffffff;
#         font-size: 3rem;
#         font-weight: 700;
#         line-height: 1;
#     }

#     .prediction-unit {
#         color: #8e98a7;
#         font-size: 1rem;
#         margin-top: 8px;
#     }

#     /* API status */
#     .status-box {
#         background: #111720;
#         border: 1px solid #252d38;
#         border-radius: 10px;
#         padding: 12px 16px;
#         margin-bottom: 20px;
#     }

#     /* Button */
#     .stButton > button {
#         width: 100%;
#         height: 48px;
#         border-radius: 8px;
#         border: none;
#         font-weight: 600;
#         font-size: 1rem;
#     }

#     /* Remove excessive top spacing */
#     h1, h2, h3 {
#         margin-top: 0;
#     }

#     </style>
#     """,
#     unsafe_allow_html=True
# )


# # ============================================================
# # FASTAPI CONFIGURATION
# # ============================================================

# # Local development:
# # API_URL = "http://127.0.0.1:8000"

# # Render deployment:
# # API_URL = food-delivery-time-prediction-lilac.vercel.app

# API_URL = st.secrets.get(
#     "API_URL",
#     "http://127.0.0.1:8000"
# )

# PREDICT_URL = f"{API_URL}/predict"


# # ============================================================
# # HEADER
# # ============================================================

# st.markdown(
#     '<div class="main-title">Food Delivery Time Predictor</div>',
#     unsafe_allow_html=True
# )

# st.markdown(
#     """
#     <div class="subtitle">
#         Estimate delivery time using order, rider, restaurant,
#         traffic and distance information.
#     </div>
#     """,
#     unsafe_allow_html=True
# )


# # ============================================================
# # API STATUS
# # ============================================================

# try:

#     response = requests.get(
#         f"{API_URL}/health",
#         timeout=5
#     )

#     if response.status_code == 200:

#         st.success(
#             "API connected"
#         )

#     else:

#         st.warning(
#             "API is reachable but returned an unexpected response."
#         )

# except requests.RequestException:

#     st.error(
#         "Unable to connect to the FastAPI server."
#     )


# # ============================================================
# # INPUT FORM
# # ============================================================

# with st.form("prediction_form"):

#     # --------------------------------------------------------
#     # ORDER INFORMATION
#     # --------------------------------------------------------

#     st.markdown(
#         '<div class="section-title">Order Information</div>',
#         unsafe_allow_html=True
#     )

#     col1, col2, col3 = st.columns(3)

#     with col1:

#         order_hour = st.number_input(
#             "Order Hour",
#             min_value=0,
#             max_value=23,
#             value=14,
#             step=1,
#             help="Hour of order in 24-hour format."
#         )

#     with col2:

#         day_of_week = st.selectbox(
#             "Day of Week",
#             [
#                 "Monday",
#                 "Tuesday",
#                 "Wednesday",
#                 "Thursday",
#                 "Friday",
#                 "Saturday",
#                 "Sunday"
#             ]
#         )

#     with col3:

#         is_weekend = st.selectbox(
#             "Weekend",
#             [0, 1],
#             format_func=lambda x: "Yes" if x == 1 else "No"
#         )

#     col1, col2, col3 = st.columns(3)

#     with col1:

#         is_festival = st.selectbox(
#             "Festival",
#             [0, 1],
#             format_func=lambda x: "Yes" if x == 1 else "No"
#         )

#     with col2:

#         order_year = st.number_input(
#             "Order Year",
#             min_value=2000,
#             max_value=2100,
#             value=2026,
#             step=1
#         )

#     with col3:

#         order_month = st.number_input(
#             "Order Month",
#             min_value=1,
#             max_value=12,
#             value=8,
#             step=1
#         )

#     col1, col2 = st.columns(2)

#     with col1:

#         order_day = st.number_input(
#             "Order Day",
#             min_value=1,
#             max_value=31,
#             value=20,
#             step=1
#         )

#     with col2:

#         delivery_priority = st.selectbox(
#             "Delivery Priority",
#             [
#                 "Low",
#                 "Medium",
#                 "High"
#             ]
#         )


#     # --------------------------------------------------------
#     # RESTAURANT INFORMATION
#     # --------------------------------------------------------

#     st.markdown(
#         '<div class="section-title">Restaurant Information</div>',
#         unsafe_allow_html=True
#     )

#     col1, col2, col3 = st.columns(3)

#     with col1:

#         restaurant_rating = st.number_input(
#             "Restaurant Rating",
#             min_value=0.0,
#             max_value=5.0,
#             value=4.0,
#             step=0.1
#         )

#     with col2:

#         cuisine_type = st.selectbox(
#             "Cuisine Type",
#             [
#                 "Indian",
#                 "Chinese",
#                 "Italian",
#                 "Mexican",
#                 "Fast Food",
#                 "South Indian",
#                 "North Indian",
#                 "Other"
#             ]
#         )

#     with col3:

#         restaurant_load = st.selectbox(
#             "Restaurant Load",
#             [
#                 "Low",
#                 "Medium",
#                 "High"
#             ]
#         )

#     col1, col2 = st.columns(2)

#     with col1:

#         preparation_time = st.number_input(
#             "Preparation Time (min)",
#             min_value=0.0,
#             value=20.0,
#             step=1.0
#         )

#     with col2:

#         order_items = st.number_input(
#             "Order Items",
#             min_value=1,
#             value=2,
#             step=1
#         )


#     # --------------------------------------------------------
#     # DELIVERY INFORMATION
#     # --------------------------------------------------------

#     st.markdown(
#         '<div class="section-title">Delivery Information</div>',
#         unsafe_allow_html=True
#     )

#     col1, col2, col3 = st.columns(3)

#     with col1:

#         weather = st.selectbox(
#             "Weather",
#             [
#                 "Clear",
#                 "Cloudy",
#                 "Rainy",
#                 "Stormy",
#                 "Foggy"
#             ]
#         )

#     with col2:

#         traffic_level = st.selectbox(
#             "Traffic Level",
#             [
#                 "Low",
#                 "Medium",
#                 "High",
#                 "Heavy"
#             ]
#         )

#     with col3:

#         vehicle_type = st.selectbox(
#             "Vehicle Type",
#             [
#                 "Bike",
#                 "Scooter",
#                 "Car",
#                 "Bicycle"
#             ]
#         )

#     col1, col2 = st.columns(2)

#     with col1:

#         pickup_zone = st.text_input(
#             "Pickup Zone",
#             value="Zone A"
#         )

#     with col2:

#         dropoff_zone = st.text_input(
#             "Dropoff Zone",
#             value="Zone B"
#         )

#     col1, col2, col3 = st.columns(3)

#     with col1:

#         road_distance = st.number_input(
#             "Road Distance (km)",
#             min_value=0.0,
#             value=5.0,
#             step=0.1
#         )

#     with col2:

#         distance_category = st.selectbox(
#             "Distance Category",
#             [
#                 "Short",
#                 "Medium",
#                 "Long"
#             ]
#         )

#     with col3:

#         number_of_signals = st.number_input(
#             "Number of Signals",
#             min_value=0,
#             value=5,
#             step=1
#         )

#     col1, col2, col3 = st.columns(3)

#     with col1:

#         average_speed = st.number_input(
#             "Average Speed (km/h)",
#             min_value=0.1,
#             value=30.0,
#             step=1.0
#         )

#     with col2:

#         rider_experience = st.number_input(
#             "Rider Experience (years)",
#             min_value=0.0,
#             value=2.0,
#             step=0.5
#         )

#     with col3:

#         rider_rating = st.number_input(
#             "Rider Rating",
#             min_value=0.0,
#             max_value=5.0,
#             value=4.5,
#             step=0.1
#         )


#     # --------------------------------------------------------
#     # PREDICT BUTTON
#     # --------------------------------------------------------

#     st.markdown("<br>", unsafe_allow_html=True)

#     predict_button = st.form_submit_button(
#         "Predict Delivery Time"
#     )


# # ============================================================
# # PREDICTION
# # ============================================================

# if predict_button:

#     # --------------------------------------------------------
#     # Prepare API Payload
#     # --------------------------------------------------------

#     payload = {

#         "Order_Hour": int(order_hour),

#         "Day_of_Week": day_of_week,

#         "Is_Weekend": int(is_weekend),

#         "Is_Festival": int(is_festival),

#         "Weather": weather,

#         "Pickup_Zone": pickup_zone,

#         "Dropoff_Zone": dropoff_zone,

#         "Vehicle_Type": vehicle_type,

#         "Rider_Experience_Years": float(
#             rider_experience
#         ),

#         "Rider_Rating": float(
#             rider_rating
#         ),

#         "Restaurant_Rating": float(
#             restaurant_rating
#         ),

#         "Cuisine_Type": cuisine_type,

#         "Order_Items": int(
#             order_items
#         ),

#         "Restaurant_Load": restaurant_load,

#         "Preparation_Time_Min": float(
#             preparation_time
#         ),

#         "Road_Distance_km": float(
#             road_distance
#         ),

#         "Delivery_Distance_Category": distance_category,

#         "Traffic_Level": traffic_level,

#         "Number_of_Signals": int(
#             number_of_signals
#         ),

#         "Average_Speed_kmph": float(
#             average_speed
#         ),

#         "Delivery_Priority": delivery_priority,

#         "Order_Year": int(
#             order_year
#         ),

#         "Order_Month": int(
#             order_month
#         ),

#         "Order_Day": int(
#             order_day
#         )
#     }


#     # --------------------------------------------------------
#     # Send Request To FastAPI
#     # --------------------------------------------------------

#     with st.spinner("Calculating delivery time..."):

#         try:

#             response = requests.post(
#                 PREDICT_URL,
#                 json=payload,
#                 timeout=30
#             )


#             # ------------------------------------------------
#             # Successful Prediction
#             # ------------------------------------------------

#             if response.status_code == 200:

#                 result = response.json()

#                 prediction = result[
#                     "predicted_delivery_time_minutes"
#                 ]

#                 st.markdown(
#                     f"""
#                     <div class="prediction-card">

#                         <div class="prediction-label">
#                             Estimated Delivery Time
#                         </div>

#                         <div class="prediction-value">
#                             {prediction}
#                         </div>

#                         <div class="prediction-unit">
#                             minutes
#                         </div>

#                     </div>
#                     """,
#                     unsafe_allow_html=True
#                 )


#             # ------------------------------------------------
#             # FastAPI Validation Error
#             # ------------------------------------------------

#             elif response.status_code == 422:

#                 st.error(
#                     "Invalid input data. Please check the entered values."
#                 )

#                 try:

#                     error_data = response.json()

#                     with st.expander(
#                         "View validation details"
#                     ):

#                         st.json(error_data)

#                 except Exception:

#                     pass


#             # ------------------------------------------------
#             # FastAPI Server Error
#             # ------------------------------------------------

#             else:

#                 st.error(
#                     "Prediction request failed."
#                 )

#                 try:

#                     error_data = response.json()

#                     with st.expander(
#                         "View server response"
#                     ):

#                         st.json(error_data)

#                 except Exception:

#                     pass


#         except requests.exceptions.Timeout:

#             st.error(
#                 "Request timed out. Please try again."
#             )


#         except requests.exceptions.ConnectionError:

#             st.error(
#                 "Could not connect to FastAPI. "
#                 "Make sure the backend server is running."
#             )


#         except requests.exceptions.RequestException as e:

#             st.error(
#                 f"API request failed: {str(e)}"
#             )
