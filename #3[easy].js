/*
Welcome to cipher day!
write a program that can encrypt texts with an alphabetical caesar cipher. This cipher can ignore numbers, symbols, and whitespace.
*/

function rot13(str) {
  var final= [];

  for (var i = 0; i < str.length; i++) {
    if (str.charCodeAt(i) < 65 || str.charCodeAt(i) > 90) {
      final.push(str.charAt(i));
    } else if (str.charCodeAt(i) > 77) {
      final.push(String.fromCharCode(str.charCodeAt(i) - 13));
    } else {
      final.push(String.fromCharCode(str.charCodeAt(i) + 13));
    }
  }
  return final.join("");
}
