fn main() {
    println!(
        "{:?}",
        (1..=100)
            .filter(|n| (n + 4) * (n + 2) % 7 == 0)
            .collect::<Vec<_>>()
    );

    println!(
        "{}",
        (1..=100).filter(|n| (n + 4) * (n + 2) % 7 == 0).count()
    );
}
