<!-- First -->
# Serverless HealthBooking

Serverless HealthBooking is a graduation project for the AWS course at HTU University.  
This project demonstrates your understanding of AWS Serverless Services by deploying a fully working web-based medical appointment booking system, with all components hosted and managed using AWS-native tools.

## Project Overview
x
You will host a medical clinic appointment website. The system allows users to book appointments and doctors to manage them.

All backend components are built using serverless AWS services such as:
- AWS Lambda
- Amazon DynamoDB
- Amazon API Gateway
- Amazon SNS
- Amazon EventBridge
- AWS CloudWatch
- AWS Amplify (for frontend hosting)

![image](https://github.com/user-attachments/assets/271dec18-db13-4ed5-81a0-36e42dd24065)

## DynamoDB Tables

The backend uses two DynamoDB tables:

### 1. Appointments

| Attribute       | Type    | Description                               |
|----------------|---------|-------------------------------------------|
| appointmentId  | String  | Partition Key (UUID)                      |
| createdAt      | String  | Timestamp of booking                      |
| patientName    | String  | Name of the patient                       |
| slot           | String  | Time slot (e.g., "10 - 11")               |
| status         | String  | One of: Pending, In Progress, Completed   |
| symptoms       | String  | Patient's described symptoms              |

### 2. Slots

| Attribute | Type    | Description             |
|----------|---------|-------------------------|
| slot     | String  | Partition Key           |
| isBooked | Boolean | Whether the slot is taken |

## APIs (5 Lambda Functions)

Each of the following Lambda functions must be connected to API Gateway, and the API paths must be updated in the frontend code accordingly.

### 1. GET Time Slots

- Retrieves all available (unbooked) time slots.
- Used on the homepage to allow patients to select an available slot.

### 2. POST Appointments

- Creates a new appointment.
- Saves it to the Appointments table and marks the slot as booked.
- Sends an email notification via Amazon SNS to your email (assuming you're the doctor).

### 3. GET Appointments

- Returns all appointments from the database.
- Used to display bookings on the admin/doctor panel.

### 4. PATCH Appointment Status

- Allows updating the status of a specific appointment to:
  - Pending
  - In Progress
  - Completed

### 5. Reset Daily Bookings

- Triggered daily at 5 PM UTC via EventBridge.
- Deletes all appointments from the current day.
- Resets all Slots to isBooked = false.
- Sends an email notification via SNS confirming the reset.

## Frontend Setup (Vue.js)

- The website contains two main pages:
  - Book Appointment – Users fill out their name, symptoms, and select an available time slot.
  - Appointments – Doctor/admin panel to view all bookings and update their statuses.

- You should:
  - Fork this repository to your own GitHub account.
  - Replace the API paths in the Vue frontend with your deployed API Gateway endpoints.
  - Connect your GitHub repo to AWS Amplify for automatic deployment.
  - Use CloudWatch for monitoring and logging.

## Technologies Used

- Frontend: Vue.js, Vite, PrimeVue (for UI)
- Backend: AWS Lambda, API Gateway
- Database: Amazon DynamoDB
- Notifications: Amazon SNS
- Scheduled Tasks: Amazon EventBridge
- CI/CD: AWS Amplify
- Monitoring: AWS CloudWatch

## Final Notes

Make sure:
- IAM permissions are correctly configured for each Lambda function.
- All endpoints are tested via API Gateway before connecting to the frontend.
- You follow the structure shown above to pass the course project requirements.
