-- upgrade --
ALTER TABLE "testmodel" ADD "ts2" INT;
-- downgrade --
ALTER TABLE "testmodel" DROP COLUMN "ts2";
