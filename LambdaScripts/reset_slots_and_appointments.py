import boto3
 
dynamodb = boto3.resource('dynamodb')
slots_table = dynamodb.Table('Slots')
appointments_table = dynamodb.Table('Appointments')
sns = boto3.client('sns')
 
SLOTS = ["8 - 9", "9 - 10", "10 - 11", "11 - 12", "12 - 1"]
 
# Replace with your actual SNS Topic ARN
SNS_TOPIC_ARN = "arn:aws:sns:us-east-1:730335665786:doctor-booking"
 
def lambda_handler(event, context):
    try:
        # 1. Scan and delete all current slots
        slots_response = slots_table.scan()
        existing_slots = slots_response.get('Items', [])
 
        with slots_table.batch_writer() as batch:
            for slot in existing_slots:
                batch.delete_item(Key={'slot': slot['slot']})
 
        # 2. Re-insert default slots
        with slots_table.batch_writer() as batch:
            for slot in SLOTS:
                batch.put_item(Item={
                    'slot': slot,
                    'isBooked': False
                })
 
        # 3. Scan and delete all appointments
        appointments_response = appointments_table.scan()
        existing_appointments = appointments_response.get('Items', [])
 
        with appointments_table.batch_writer() as batch:
            for appointment in existing_appointments:
                batch.delete_item(Key={'appointmentId': appointment['appointmentId']})
 
        # 4. Send SNS notification about reset completion
        message = "Daily reset of appointments and slots completed successfully."
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Message=message,
            Subject="Reset Confirmation"
        )
 
        return {
            'statusCode': 200,
            'body': 'Slots and appointments reset successfully, notification sent.'
        }
 
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }