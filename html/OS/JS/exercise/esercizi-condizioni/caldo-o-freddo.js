/*
  Caldo o freddo
  Scrivi un programma che dati sette valori relativi alle temperature della settimana
  stabilisca la giornata più calda e quella più fredda.

  Esempio:
    Input: a = 10, b = -2, c = 31, d = 22, e = 15, f = -6, g = 7
    Output: giornata più calda = 31, giornata più fredda = -6

  http://www.imparareaprogrammare.it
*/

var Number = [10, -2, 31, 22, 15, -6, 7]

var L = -50
for (var i in Number) {
  if (i >= L) {
    L = i
  }
}

var Number = L;
console.log()

