fn main() {
    fn u_n(n: u64) -> u64 {
        match n {
            0 => 1,
            1 => 2,
            _ => (0..n).fold(0, |acc, i| acc + u_n(i)),
        }
    }
    println!("{}", u_n(19)); // = 3 × 2ⁿ⁻²
}
