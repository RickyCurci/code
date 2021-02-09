/*
  Azzecca e azzera
  Scrivi un programma che dato un array di 100 elementi, lo riempia con numeri interi casuali da 1 a 50.
  Permetti all'utente di inserire un numero e azzera tutti i gli elementi nell'array principale che sono suoi multipli.
  Richiedi all'utente un altro numero e così via.
  Il programma termina quando tutti gli elementi dell'array principale sono uguali a zero.

  Consigli:
  Se non ricordi come generare un numero random e come convertirlo nel tuo intervallo riguarda l'esercizio sulle condizioni "Chi l'azzecca?".
  Per richiedere un numero all'utente puoi usare il comando prompt(), se vuoi saperne di più puoi controllare nella
  documentazione: https://developer.mozilla.org/it/docs/Web/API/Window/prompt

  http://www.imparareaprogrammare.it
*/
//const prompt = require('prompt-sync')({sigint: true});
function range(start, end) {
    var ans = [];
    for (let i = start; i <= end; i++) {
        ans.push(i);
    }
    return ans;
}

var a = []
for (i in range(0, 100)) {
  a.push(Math.floor(Math.random() * 50 + 1))
}
b = []
function logic() {

  for (i in a) {
    var num = [0,3,4,5,3,6] //prompt('>')
    for (N in num) {
      if ((i % N) == 0) {
        a[i] = 0
      }
    }

    if (i == 0) {
      b.push(0)
      if (b.lenght == a.lenght) {
        break
        console.log(a)
      }
    }

    logic()
  }

}
