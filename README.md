# Flask Booking API

This is a simple booking API built using Flask that allows users to request bookings, and drivers to accept them. The API also supports trip verification via OTP.

## Table of Contents
- [Installation](#installation)
- [API Endpoints](#api-endpoints)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/muzaferxp/booking-app-demo
    cd booking-app-demo
    ```

2. Set up a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask application:
    ```bash
    python app.py
    ```

5. The application will run on `http://localhost:5000`.

## API Endpoints

### User APIs

- **Booking Request**  
  Request a booking by specifying vehicle type, start, and end locations.
  - **POST** `/bookingRequest`
  - Parameters:
    - `vehicleType`: Type of vehicle (e.g., "bike")
    - `start_location`: Start location coordinates (e.g., "lat1,lon1")
    - `end_location`: End location coordinates (e.g., "lat2,lon2")

### Driver APIs

- **Get Booking Requests**  
  Fetch all booking requests.
  - **GET** `/booking-requests`

- **Accept Booking**  
  Accept a booking request and create a booking.
  - **POST** `/accept-booking/<bookingRequestId>`
  - Parameters:
    - `bookingRequestId`: The ID of the booking request

- **Start Trip**  
  Start the trip after verifying OTP.
  - **POST** `/start-trip/<bookingId>`
  - Parameters:
    - `otp`: OTP for trip verification

### Booking APIs

- **Get Booking Details**  
  Retrieve details of a specific booking.
  - **GET** `/booking/details/<bookingId>`
  - Parameters:
    - `bookingId`: The ID of the booking