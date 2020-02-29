pub fn reverse(input: &str) -> String {
    let vec = input.as_bytes();
    vec.reverse();
    let reversed = String::from_utf8(vec);
    return reversed.unwrap();
}
