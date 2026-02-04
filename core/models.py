users = """
        CREATE TABLE IF NOT EXISTS users
        (
            id           BIGSERIAL PRIMARY KEY,
            chat_id      BIGINT UNIQUE      NOT NULL,
            username     VARCHAR(255),
            full_name    VARCHAR(255),
            language     VARCHAR(2)         DEFAULT 'uz',
            phone_number VARCHAR(13) UNIQUE ,
            longitude    VARCHAR(64),
            latitude     VARCHAR(64),
            created_at   TIMESTAMP                   DEFAULT CURRENT_TIMESTAMP,
            student_id   BIGINT

        ) \
        """