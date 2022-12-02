package day2

import java.io.File

fun main() {
    val f = File("input/day2.txt")

    val winsA = hashMapOf(
        "A" to hashMapOf("X" to 1+3, "Y" to 2+6, "Z" to 3+0),
        "B" to hashMapOf("X" to 1+0, "Y" to 2+3, "Z" to 3+6),
        "C" to hashMapOf("X" to 1+6, "Y" to 2+0, "Z" to 3+3)
    )

    val winsB = hashMapOf(
        "A" to hashMapOf("X" to 3+0, "Y" to 1+3, "Z" to 2+6),
        "B" to hashMapOf("X" to 1+0, "Y" to 2+3, "Z" to 3+6),
        "C" to hashMapOf("X" to 2+0, "Y" to 3+3, "Z" to 1+6)
    )

    var scoreA = 0
    var scoreB = 0

    f.forEachLine {
        val line = it.split(" ")
        val playerA = line[0]
        val playerB = line[1]

        var inner = winsA[playerA]!!
        scoreA += inner[playerB]!!

        inner = winsB[playerA]!!
        scoreB += inner[playerB]!!
    }
    println("Part A")
    println(scoreA)
    println()
    println("Part B")
    println(scoreB)
}