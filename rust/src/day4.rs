use std::fs;

pub fn run() {
    let input = fs::read_to_string("../kotlin/input/day4.txt").unwrap();

    let mut score_a = 0;
    let mut score_b = 0;
    for line in input.lines().filter(|ln| *ln != "") {
        let (elf1, elf2) = line.split_once(",").unwrap();
        let (r1s, r1e) = elf1.split_once("-").unwrap();
        let (r2s, r2e) = elf2.split_once("-").unwrap();

    }
}

fn in_a(r1s: i64, r2s: i64, r1e: i64, r2e: i64) -> bool {
    return (r1s >= r2s && r1e <= r2e) || (r2s >= r1s && r2e <= r1e);
}

fn in_b(r1s: i64, r2s: i64, r1e: i64, r2e: i64) -> bool {
    return 
}