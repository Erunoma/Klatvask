CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username Text not null ,
    password Text not null ,
    phone_number Text not null ,
    has_a_booking bit not nulL,
    is_admin bit
)
