// solution problème du 23 septembre 2020

// compilation:
//      rustc -O 23.rs

use std::time::Instant;

fn main() {
    let now = Instant::now();
    let mut reponse = 0;

    for a in 1..=9 {
        let n_max = (0..a).fold(0, |n, _| n * 10 + 1);

        let mut parents = 0;
        let mut nb_diviseurs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0];

        for n in 1..=n_max {
            // vérification ∑chiffres de n = a et chiffres≠O
            let mut somme_chiffres = 0;
            let mut nn = n;
            while nn != 0 {
                let c = nn % 10;
                if c == 0 {
                    somme_chiffres = 0;
                    break;
                }
                somme_chiffres += c;
                nn /= 10;
            }

            if somme_chiffres == a {
                parents += 1;

                // on compte le nombre de fois où <ab> divise <nb>
                // si ce nombre est égal au nombre de parents,
                // le critère de l'énoncé est respecté
                let n_10 = 10 * n; // attention au débordement, int est trop petit
                let a_10 = 10 * a;
                for b in 0..=9 {
                    if (n_10 + b) % (a_10 + b) == 0 {
                        nb_diviseurs[b as usize] += 1;
                    }
                }
            }
        }

        // le nombre de parents de a est nb_parents, celui de ab est 10 fois plus
        print!(
            "a={} n_max={:9} nb_parents={:4} ab=",
            a,
            n_max,
            parents * 10
        );

        // affiche les <ab> qui conviennent
        for b in 0..=9 {
            if nb_diviseurs[b] == parents {
                reponse += 1;
                print!("{}{} ", a, b);
            }
        }
        println!();
    }

    println!("réponse: {}", reponse);
    println!("temps: {} s", (now.elapsed().as_micros() as f64) / 1000000.);
}
