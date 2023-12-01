use std::collections::HashSet;

fn main() {
    let size = 14;
    let answer = include_bytes!("C:/git/adventofcode/2022/day06/data.in")
        .windows(size)
        .position(|w| HashSet::<u8>::from_iter(w.iter().cloned()).len() == w.len());
    println!("{:?}", answer.unwrap() + size)
}