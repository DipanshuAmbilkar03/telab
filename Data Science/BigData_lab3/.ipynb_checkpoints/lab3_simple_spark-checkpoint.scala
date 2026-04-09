import org.apache.spark.sql.SparkSession

object SimpleSparkProgram {
  def main(args: Array[String]): Unit = {
    val spark = SparkSession.builder()
      .appName("SimpleSparkProgram")
      .master("local[*]")
      .getOrCreate()

    import spark.implicits._

    val data = Seq(
      ("Aarav", 85),
      ("Isha", 92),
      ("Rohan", 76),
      ("Meera", 88),
      ("Kabir", 81)
    )

    val df = data.toDF("name", "score")
    df.createOrReplaceTempView("students")

    val result = spark.sql("SELECT name, score FROM students WHERE score >= 80 ORDER BY score DESC")
    result.show()

    spark.stop()
  }
}
