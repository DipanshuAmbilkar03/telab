import org.apache.spark.sql.SparkSession

object WordCountExample {
    def main(args: Array[String]): Unit = {

        val spark = SparkSession.builder()
        .appName("Word Count Example")
        .master("local[*]")
        .getOrCreate()

        import spark.implicits._

        val data = List("dipanshu kinjal", "Onyx dipanshu", "Pranjal kinjal")

        val ds = spark.createDataset(data)

        val wordCount = ds
        .flatMap(line => line.split(" "))
        .groupBy("value")
        .count()

        wordCount.show()

        spark.stop()
    }
}

WordCountExample.main(Array())

-- output
-- +--------+-----+
-- |value   |count|
-- +--------+-----+
-- |kinjal  |    2|
-- |dipanshu|    2|
-- |Onyx    |    1|
-- |Pranjal |    1|
-- +--------+-----+