fn reverse_str(input_string: &str) -> String {
    input_string.chars().rev().collect()
}

fn main() {
    let original_string = String::from("Hello World!");
    let reversed_string = reverse_str(&original_string);
    println!("Original: {}", original_string);
    println!("Reversed: {}", reversed_string);
}
