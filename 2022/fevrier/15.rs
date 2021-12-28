fn main() {
    (1..=1011)
        .filter(|i| (i + 1011) % i == 0)
        .for_each(|i| println!("{:4} * {:4} = {:4}", i, (i + 1011) / i, i + 1011))
}
