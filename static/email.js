let excerpt1 = ""
let excerpt2 = ""
let excerpt3 = ""
let excerpt4 = ""
let excerpt5 = ""

fetch("/excerpt1")
  .then(excerpt => excerpt.text())
  .then(str => excerpt1 = str)

fetch("/excerpt2")
  .then(excerpt => excerpt.text())
  .then(str => excerpt2 = str)

fetch("/excerpt3")
  .then(excerpt => excerpt.text())
  .then(str => excerpt3 = str)

fetch("/excerpt4)
      .then(excerpt => excerpt.text())
      .then(str => excerpt4 = str)

fetch("/excerpt5)
      .then(excerpt => excerpt.text())
      .then(str => excerpt5 = str)
