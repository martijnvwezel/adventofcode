use std::io;
use std::io::File
use std::io::BufReader;


fn main() {
    let f = File::open("../data.in");

    let mut reader - BufReader::new(f);

    let mut buffer = Vec::new();

    reader.read_to_end(&mut buffer);

    for value in buffer {
        println!("Byte: {}", value);
    }

    ok(());



}
