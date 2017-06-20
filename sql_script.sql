CREATE TABLE IF NOT EXISTS regions (
    region_id INTEGER PRIMARY KEY,
    region_name TEXT UNIQUE
     );

    CREATE TABLE IF NOT EXISTS cities (
    cities_id INTEGER PRIMARY KEY AUTOINCREMENT,
    region_id INTEGER NOT NULL,
    city TEXT UNIQUE,
    FOREIGN KEY (region_id) REFERENCES regions(region_id)
    ON DELETE RESTRICT
    ON UPDATE CASCADE
    );

    CREATE TABLE IF NOT EXISTS feedback_rows (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    partonymic TEXT,
    region_id INTEGER NOT NULL,
    city_id INTEGER NOT NULL,
    phone_number TEXT,
    email TEXT,
    feedback TEXT NOT NULL,
    FOREIGN KEY (region_id) REFERENCES regions(region_id),
    FOREIGN KEY (city_id) REFERENCES cities(cities_id)
    );

    /*INSERT INTO regions (region_name)VALUES ("Краснодарский край");
    INSERT INTO regions (region_name)VALUES ("Ростовская область");
    INSERT INTO regions (region_name)VALUES ("Ставропольский край");
    INSERT INTO cities (region_id, city)VALUES (1,"Краснодар");
    INSERT INTO cities (region_id, city)VALUES (1,"Кропоткин");
    INSERT INTO cities (region_id, city)VALUES (1,"Славянск");
    INSERT INTO cities (region_id, city)VALUES (2,"Ростов");
    INSERT INTO cities (region_id, city)VALUES (2,"Шахты");
    INSERT INTO cities (region_id, city)VALUES (2,"Батайск");
    INSERT INTO cities (region_id, city)VALUES (3,"Ставрополь");
    INSERT INTO cities (region_id, city)VALUES (3,"Пятигорск");
    INSERT INTO cities (region_id, city)VALUES (3,"Кисловодск");*/