DROP TABLE IF EXISTS items;

CREATE TABLE items
(
    id          INT          NOT NULL AUTO_INCREMENT,
    name        VARCHAR(255) NOT NULL,
    description VARCHAR(255) NULL,
    price       INT          NOT NULL,
    created_at  DATETIME     NOT NULL,
    updated_at  DATETIME     NOT NULL,
    PRIMARY KEY (id)
);

insert into items values(1, "Furby", "Furby toy", 45, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP());
insert into items values(2, "Zerg", "Zerg action figure", 55, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP());

