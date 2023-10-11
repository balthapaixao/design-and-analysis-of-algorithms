fn print_n_primes(n: u32) {
    let mut primes = Vec::new();
}

fn main() {
    let mut n = String::new();
    std::io::stdin()
        .read_line(&mut n)
        .expect("Falha ao ler entrada");
    let n: u32 = n.trim().parse().expect("Falha ao converter entrada");

    while n < 1 {
        println!("Entrada inválida. Digite um número maior que 0.");
        let mut n = String::new();
        std::io::stdin()
            .read_line(&mut n)
            .expect("Falha ao ler entrada");
        let n: u32 = n.trim().parse().expect("Falha ao converter entrada");
    }
    print_n_primes(n);
}
