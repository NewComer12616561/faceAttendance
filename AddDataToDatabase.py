import firebase_admin
from firebase_admin import credentials
from firebase_admin import db



cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':""
})

ref = db.reference('Students')

data = {
    "123456":
        {
            "name": "Le Gia Khanh",
            "major": "IT",
            "starting_year": 2020,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "123":
        {
            "name": "Elon Musk",
            "major": "Economics",
            "starting_year": 2020,
            "total_attendance": 12,
            "standing": "B",
            "year": 4,
            "last_attendance_time": " 2024-11-7 00:30:00"
        },
    "456":
        {
            "name": "Jeff Bezos",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },

         "852741":
        {
            "name": "Girl",
            "major": "Economics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)