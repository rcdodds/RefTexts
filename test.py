# Imports
import gcal         # Custom module from PYTHONPATH system environment variable
import twilio_sms   # Custom module from PYTHONPATH system environment variable


# Pull
ref_cal_id = gcal.pick_calendar('test')
print(ref_cal_id)

# Send text
twilio_sms.send_text('testing new twilio pject', '+14847233363')
