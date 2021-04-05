-- upgrade --
ALTER TABLE "testmodel" RENAME COLUMN "ts2" TO "ts3";
-- downgrade --
ALTER TABLE "testmodel" RENAME COLUMN "ts3" TO "ts2";
