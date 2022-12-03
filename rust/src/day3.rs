use std::collections::HashSet;
use std::fs;

pub fn run() {
    let binding = fs::read_to_string("../kotlin/input/day3.txt").unwrap();
    let input = binding.split("\r\n").filter( |ln| *ln != "");

    let mut last_set: HashSet<char> = HashSet::new();
    let mut score_a = 0;
    let mut score_b = 0;
    for (i, line) in input.enumerate() {
        let line_length = line.len() /2;
        let current_set: HashSet<char> = line.chars().collect();
        if i % 3 == 0 {
            score_b += get_score(last_set);
            last_set = current_set
        }
        else {
            last_set = last_set.intersection(&current_set).copied().collect();
        }

        let (str_a, str_b) = line.split_at(line_length);
        let set_a: HashSet<char> = str_a.chars().collect();
        let set_b: HashSet<char> = str_b.chars().collect();
        let intersection = set_a.intersection(&set_b).copied().collect();
        score_a += get_score(intersection);
    }
    score_b += get_score(last_set);
    println!("part a");
    println!("{}", score_a);
    println!("part b");
    println!("{}", score_b);
}

fn get_score(s: HashSet<char>) -> i32 {
    for c in &s {
        let dig = *c as u16;
        return if dig > 90 {
            dig - 96
        } else {
            dig - 64 + 26
        } as i32
    }
    return 0;
}