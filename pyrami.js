
function firstNonRepeatedCharacter(string) {
  let result_map = new Map();
  for (var i = 0; i < string.length; i++) {
    var c = string.charAt(i);
    if (string.indexOf(c) == i && string.indexOf(c, i + 1) == -1) {
      result_map.set("Non_repeating_char", c)
      return result_map.get("Non_repeating_char")
    }
  }
  return "No Non Repeating character found";
}
console.log(firstNonRepeatedCharacter("nandhadhini"))