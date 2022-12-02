use std::fs;
use std::collections::HashMap;

pub fn run() {
    let input = fs::read_to_string("../kotlin/input/day2.txt").unwrap();

    let scores: HashMap<(&str, &str), i32> = HashMap::from_iter([
        (("A", "X"), 4),
        (("A", "Y"), 8),
        (("A", "Z"), 3),
        (("B", "X"), 1),
        (("B", "Y"), 5),
        (("B", "Z"), 9),
        (("C", "X"), 7),
        (("C", "Y"), 2),
        (("C", "Z"), 6)
    ]);

    let scores_b: HashMap<(&str, &str), i32> = HashMap::from_iter([
        (("A", "X"), 3),
        (("A", "Y"), 4),
        (("A", "Z"), 8),
        (("B", "X"), 1),
        (("B", "Y"), 5),
        (("B", "Z"), 9),
        (("C", "X"), 2),
        (("C", "Y"), 6),
        (("C", "Z"), 7)
    ]);

    let mut score_a = 0;
    let mut score_b = 0;

    for l in input.split("\n").filter( |it| *it != "") {
        let (p1, p2) = l.split_once(" ").unwrap();
        score_a += scores.get(&(p1, p2)).unwrap();
        score_b += scores_b.get(&(p1, p2)).unwrap();
    }
    println!("Part A");
    println!("{}", score_a);
    println!("Part B");
    println!("{}", score_b);
}