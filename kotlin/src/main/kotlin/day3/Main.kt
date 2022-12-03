import java.io.File


fun main(args: Array<String>) {

    val f = File("input/day3.txt")


    var score = 0
    f.forEachLine {
        line ->
        val lineLength = line.length
        val setA = line.take(lineLength/2).toSet()
        val setB = line.takeLast(lineLength/2).toSet()

        val doubleChars = setA.intersect(setB)
        println(doubleChars.size)
        println(doubleChars.first() - 0)
        score += doubleChars.first().digitToInt() - 65
    }
    println(score)
}