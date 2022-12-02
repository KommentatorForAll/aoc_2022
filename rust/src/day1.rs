use std::fs;

pub fn test() {
    println!("Hello world");
    let input = fs::read_to_string("../kotlin/input/day1.txt").unwrap();

    let lines = input.split("\n");

    let mut calories = Vec::new();
    let mut current_cals: u32 = 0;

    for l in lines {
        if l == "" {
            calories.push(current_cals);
            current_cals = 0;
            continue;
        }
        current_cals += l.parse::<u32>().unwrap();
    }
    calories.sort();
    println!("Part A");
    let last_item = calories.last().unwrap();
    println!("{}", last_item);
    let last_three = calories.pop().unwrap() + calories.pop().unwrap() + calories.pop().unwrap();
    println!("Part B");
    println!("{}", last_three);

}