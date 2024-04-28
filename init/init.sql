CREATE TABLE basic_text_message(
    id SERIAL PRIMARY KEY,
    content VARCHAR (250),
    recipient VARCHAR (50),
    time timestamp,
    message_type VARCHAR (30)
);

CREATE TABLE basic_audio_message(
    id SERIAL PRIMARY KEY,
    content VARCHAR (250),
    recipient VARCHAR (50),
    time timestamp,
    message_type VARCHAR (30),
    duration int,
    format VARCHAR (20)

);

CREATE TABLE basic_video_message(
    id SERIAL PRIMARY KEY,
    content VARCHAR (250),
    recipient VARCHAR (50),
    time timestamp,
    message_type VARCHAR (30),
    duration int,
    format VARCHAR (20),
    quality VARCHAR (20)
);