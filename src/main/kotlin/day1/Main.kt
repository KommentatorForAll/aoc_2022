import java.io.File
import java.lang.Integer.parseInt

fun main(args: Array<String>) {

    val f = File("input/day1.txt")

    var currentSum = 0
    val sums = mutableListOf<Int>()
    f.forEachLine {
        line ->
        if (line == "") {
            sums.add(currentSum)
            currentSum = 0
        }
        else {
            currentSum += parseInt(line)
        }
    }
    sums.sortDescending()
    println("part a: ")
    println(sums[0])
    println()
    println("Part b: ")
    println(sums.slice(0..2).sum())
}