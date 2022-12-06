package day4

import java.io.File
import java.lang.Integer.parseInt

fun main(args: Array<String>) {
    val f = File("input/test.txt")

    var score = 0
    f.forEachLine {
        val elves = it.split(",")
        val elf1 = elves[0].split("-")
        val elf2 = elves[1].split("-")

        val range1 = parseInt(elf1[0])..parseInt(elf1[1])
        val range2 = parseInt(elf2[0])..parseInt(elf2[1])

        if (range1 in range2 || range2 in range1) {
            score++
        }
    }
    println("Part A: ")
    println(score)
}

operator fun IntRange.contains(r: IntRange): Boolean {
    return r.first >= this.first && r.last <= this.last;
}