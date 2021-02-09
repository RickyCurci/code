/*
  Invertimi
  Scrivi un programma che dato un numero N, generi un array di N numeri casuali
  e stampi sia l'array ottenuto che quello invertito.

  Esempio:
    Input: N = 5
    Output: array ottenuto = [3, 5, 10, 2, 8], array invertito = [8, 2, 10, 5, 3]

  Variante:
  Non utilizzare array/variabili di appoggio per l'inversione.

  Consigli:
  Per la variante ricordati l'uso degli indici del ciclo ;)

  http://www.imparareaprogrammare.it
*/
function range(start, end) {
    var ans = [];
    for (let i = start; i <= end; i++) {
        ans.push(i);
    }
    return ans;
}

var N = Math.floor(Math.random() * 5 + 1)
var a = []

for (i in range(1,N)) {
  a.push(Math.floor(Math.random() * 11))
}

console.log(N)
console.log(a)

for (i in a) {
  a.push(parseInt(a[ a.lenght - 1]))
  //a.pop(a[a.lenght - 1])
}
