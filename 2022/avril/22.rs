fn main() {
    println!(
        "{:?}",
        (1..=100)
            .filter(|n| *n == (n / 10) * (n % 10) + 2 * ((n / 10) + (n % 10)))
            .collect::<Vec<_>>()
    );
}
