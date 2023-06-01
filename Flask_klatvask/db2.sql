CREATE TABLE machine_booking (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    machine_1_2 bit ,
    machine_3_4 bit ,
    username Text not null ,
    wash_day TEXT ,
    timeslot TEXT,
    sms_enabled bit

)