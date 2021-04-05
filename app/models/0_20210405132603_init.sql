-- upgrade --
CREATE TABLE IF NOT EXISTS "testmodel" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "test" INT NOT NULL,
    "ts" INT NOT NULL
);
COMMENT ON COLUMN "testmodel"."test" IS 'Test value';
COMMENT ON COLUMN "testmodel"."ts" IS 'Epoch time';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(20) NOT NULL,
    "content" JSONB NOT NULL
);
