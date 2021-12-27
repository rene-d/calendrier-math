// solution problème du 23 septembre 2020

// compilation:
//      cc -o 23 -O3 -Wall -Werror 23.c

#include <stdio.h>
#include <inttypes.h>
#include <sys/time.h>

int main()
{
    struct timeval now, elapsed;
    int a, b;
    int n, n_max;
    int reponse = 0;

    gettimeofday(&now, NULL);

    for (a = 1; a <= 9; ++a)
    {
        n_max = 0;
        for (int i = 0; i < a; ++i)
            n_max = n_max * 10 + 1;

        int parents = 0;
        int nb_diviseurs[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

        for (n = 1; n <= n_max; ++n)
        {
            // vérification ∑chiffres de n = a et chiffres≠O
            int somme_chiffres = 0;
            for (int nn = n; nn != 0; nn /= 10)
            {
                int c = nn % 10;
                if (c == 0)
                {
                    somme_chiffres = 0;
                    break;
                }
                somme_chiffres += c;
            }

            if (somme_chiffres == a)
            {
                ++parents;

                // on compte le nombre de fois où <ab> divise <nb>
                // si ce nombre est égal au nombre de parents,
                // le critère de l'énoncé est respecté
                uint64_t n_10 = 10 * n; // attention au débordement, int est trop petit
                int a_10 = 10 * a;
                for (b = 0; b <= 9; ++b)
                {
                    if ((n_10 + b) % (a_10 + b) == 0)
                        ++nb_diviseurs[b];
                }
            }
        }

        // le nombre de parents de a est nb_parents, celui de ab est 10 fois plus
        printf("a=%d n_max=%9d nb_parents=%4d ab=", a, n_max, parents * 10);

        // affiche les <ab> qui conviennent
        for (b = 0; b <= 9; ++b)
        {
            if (nb_diviseurs[b] == parents)
            {
                ++reponse;
                printf("%d%d ", a, b);
            }
        }
        printf("\n");
    }

    printf("réponse: %d\n", reponse);
    gettimeofday(&elapsed, NULL);

    if (now.tv_usec > elapsed.tv_usec)
    {
        elapsed.tv_usec += 1000000;
        elapsed.tv_sec -= 1;
    }

    printf("temps: %ld.%06d s\n", elapsed.tv_sec - now.tv_sec, elapsed.tv_usec - now.tv_usec);
    return 0;
}
