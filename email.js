let excerpt1 = ""
let excerpt2 = ""
let excerpt3 = ""

fetch("/excerpt1")
  .then(excerpt => excerpt.text())
  .then(str => excerpt1 = str)

fetch("/excerpt2")
  .then(excerpt => excerpt.text())
  .then(str => excerpt2 = str)

fetch("/excerpt3")
  .then(excerpt => excerpt.text)
  .then(str => excerpt3 = str)
