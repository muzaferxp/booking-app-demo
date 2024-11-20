# Flask Booking API

This is a simple booking API built using Flask that allows users to request bookings, and drivers to accept them. The API also supports trip verification via OTP.

## Table of Contents
- [Installation](#installation)
- [API Endpoints](#api-endpoints)
- [Usage with cURL](#usage-with-curl)
- [Project Structure](#project-structure)
- [License](#license)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/flask-booking-api.git
    cd flask-booking-api
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

## Usage with cURL

You can use the following `curl` commands to interact with the API.

### 1. Create a Booking Request
```bash
curl --location 'http://localhost:5000/bookingRequest' \
--form 'vehicleType="bike"' \
--form 'start_location="lat1,lon1"' \
--form 'end_location="lat2,lon2"'
