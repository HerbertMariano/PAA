//método auxiliar: troca os elementos i e j em A
function swap(A, i, j) {
    var temp = A[i];
    A[i] = A[j];
    A[j] = temp;
}
function partition(A, inicio, fim) {
    //procura a mediana entre inicio, meio e fim
    var meio = Math.floor((inicio + fim) / 2);
    var a = A[inicio];
    var b = A[meio];
    var c = A[fim];
    var medianaIndice; //índice da mediana
    //A sequência de if...else a seguir verifica qual é a mediana
    if (a < b) {
        if (b < c) {
            //a < b && b < c
            medianaIndice = meio;
        } else {
            if (a < c) {
                //a < c && c <= b
                medianaIndice = fim;
            } else {
                //c <= a && a < b
                medianaIndice = inicio;
            }
        }
    } else {
        if (c < b) {
            //c < b && b <= a
            medianaIndice = meio;
        } else {
            if (c < a) {
                //b <= c && c < a
                medianaIndice = fim;
            } else {
                //b <= a && a <= c
                medianaIndice = inicio;
            }
        }
    }
    //coloca o elemento da mediana no fim para poder usar o Quicksort de Cormen
    swap(A, medianaIndice, fim);


    //*******************ALGORITMO DE PARTIÇÃO DE CORMEN*********************
    //o pivo é o elemento final
    var pivo = A[fim];
    var i = inicio - 1;
    var j;
    /*
     * Este laço irá varrer os vetores da esquerda para direira
     * procurando os elementos que são menores ou iguais ao pivô.
     * Esses elementos são colocados na partição esquerda.
     */
    for (j = inicio; j <= fim - 1; j++) {

        if (A[j] <= pivo) {
            i = i + 1;
            swap(A, i, j);
        }
    }
    //coloca o pivô na posição de ordenação
    swap(A, i + 1, fim);
    return i + 1; //retorna a posição do pivô
}
//Quicksort mediana de três
var cont_esque = 0;
var cont_dir = 0;
function quicksortMedianaDeTres(A, inicio, fim) {
    if (inicio < fim) {
        //realiza a partição
        var q = partition(A, inicio, fim);
        cont_esque++
        console.log('(' + A.slice(inicio, q - 1) + ') esquerda' + cont_esque)
        //ordena a partição esquerda
        quicksortMedianaDeTres(A, inicio, q - 1);
        //ordena a partição direita
        cont_dir++
        console.log('(' + A.slice(q + 1, fim) + ')direita' + cont_dir)
        quicksortMedianaDeTres(A, q + 1, fim);
    }
}

function maior(A, init, fim) {
    var x = Math.max.apply(Math, A);
    for (i = init; i < fim; i++) {
        if (A[i] == x) {
            return i
        }
    }
}

function menor(A, init, fim) {
    var x = Math.min.apply(Math, A);
    for (i = init; i < fim; i++) {
        if (A[i] == x) {
            return i
        }
    }
}

function selecao(S, p, r, k) {
    if (k == 0) {
        return menor(S, p, r)
    }
    var n = r - p
    if (k == n) {
        return maior(S, p, r)
    }
    var q = quicksortMedianaDeTres(S, p, r)
    if (k <= q - p) {
        return selecao(S, p, q - 1, k)
    }
    return selecao(S, q, r, k - q + p)

}


var A = [35, 17, 31, 29, 9, 23, 2, 29, 22, 64, 11, 2, 70, 43, 81, 55, 90]
var init = 0;
var ffff = A.length;
quicksortMedianaDeTres(A, init, ffff-1);