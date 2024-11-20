from flask import Flask, request, render_template, jsonify
import random, datetime

app = Flask(__name__)

#Assuming the current user and currrnt driver to bibass the auth module
current_user = 1
current_driver = 2

#Sampel Data of passengers
usersData = [
    {
        "id" : 1,
        "name" : "Adam",
        "email" : "adam@example.in"
    },
    {
        "id" : 2,
        "name" : "Sam",
        "email" : "sam@example.in"
    },
]

#Sample Data of drivers
driversData = [
     {
        "id" : 1,
        "name" : "d1",
        "email" : "d1@example.in",
        "vehicleType" : "bike",
        "isAvailable" : False,

    },
    {
        "id" : 2,
        "name" : "d2",
        "email" : "d2@example.in",
        "vehicleType" : "car",
        "isAvailable" : False,
    },
]

#This will be used for storing temporary request util the driver accepts
bookingRequestsData = [

]

#Once the driver accept the booking it will be stored in this list along with OTP
bookingsData = [

]

# This is used To Get available drivers
def getAvailableDrivers(vehicleType, start_location, end_location):

    #query the data from database
    availableDrivers = []
    for d in driversData:
        if d['isAvailable'] == True and d['vehicleType'] == vehicleType:
            availableDrivers.append(d)

    return availableDrivers


# This is used To get the user by Id    
def getUserById(id):
    for details in usersData:
        if details['id'] == id:
            return details

    return None

# This is used To get driver details by Id
def getDriverById(id):
    for details in driversData:
        if details['id'] == id:
            return details

    return None


#User Apis
@app.route("/user/app")
def userApp():
    return render_template("userapp.html")

# 1. Create a new booking request by user
@app.route("/bookingRequest", methods=["POST"])
def bookingRequest():

    vehicleType = request.form["vehicleType"]
    start_location = request.form["start_location"]
    end_location = request.form['end_location']

    bookingRequestsData.append({
        "id" : len(bookingRequestsData) + 1,
        "vehicleType" : vehicleType,
        "start_location" : start_location,
        "end_location" : end_location,
        "userid" : current_user
    })

    return jsonify({
        "status" : 200,
        "message" : "Booking request sent!"
    })
    
# 2. Get booking requsts by driver by matching vehichleType
@app.route("/booking-requests", methods=['GET'])
def getBookingRequests():
    bookingsMatches = []
    current_driver_details = getDriverById(current_driver)

    #Filter the bookings based on vehicleType
    for details in bookingRequestsData:
        if current_driver_details['vehicleType'] == details['vehicleType']:
            bookingsMatches.append(details)

    #TODO: nearest match calculation

    return jsonify({
        "status" : 200,
        "message" : "Requests fetched!",
        "data" : bookingsMatches
    })


# 3. Accept a booking request and create a booking
@app.route("/accept-booking/<bookingRequestId>", methods=["POST"])
def acceptBooking(bookingRequestId):
    bookingRequestDetails = None
    for i in bookingRequestsData:
        if i['id'] == int(bookingRequestId):
            bookingRequestDetails = i
    
    if not bookingRequestDetails:
        return jsonify({
            "status" : 404,
            "message" : "Booking request not found!"
        })

    id = len(bookingsData) + 1
    bookingsData.append({
        "id" : id,
        "userid" : current_user,
        "driver_id" : current_driver,
        "start_location" : bookingRequestDetails['start_location'],
        "end_location" : bookingRequestDetails['end_location'],
        "otp" : random.randint(1000,9999),
        "start_time" : None,
        "isVerified" : False
    })

    return jsonify({
        "status" : 200,
        "message" : f"Booking has been accepted successfully, booking id is {id}"
    })



#Booking Apis
# 4. Fetch booking details by booking ID
@app.route("/booking/details/<bookingId>", methods=['GET'])
def getBookingDetails(bookingId):
    for details in bookingsData:
        if details['id']==int(bookingId):
            return jsonify({
                "status" : 200,
                "message" : "booking details fetched",
                "data" : details
            })
    return jsonify({
        "status" : 400,
        "message" : "Booking does not exists with id"
    })      

# 4. Verify OTP to start the trip
@app.route("/start-trip/<bookingId>", methods=["POST"])
def verifyTrip(bookingId):
    otp = request.form['otp']

    bookingDetails = None
    bookingIndex = None
    for i in range(len(bookingsData)):
        details  = bookingsData[i]
        
        if details['id'] == int(bookingId):
            bookingIndex = i
            bookingDetails = details
    
    if not bookingDetails:
        return jsonify({
            "status" : 404,
            "message" : "Booking not found"
        })
    
    if int(otp) != bookingDetails['otp']:
        return jsonify({
            "status" : 400,
            "message" : "Invalid OTP!"
        })
    
    bookingDetails['start_time'] = datetime.datetime.now()
    bookingDetails['isVerified'] = True

    bookingsData[bookingIndex] = bookingDetails


    return jsonify({
        "status" : 200,
        "message" : "Trip has been started successfully!"
    })


if __name__ == "__main__":
    app.run()