function encrypt() {

    let alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    let key = Number(document.getElementById("e_key").value);
    let text = document.getElementById("encrypt").value;

    let encrypted = ""
    for (let i = 0; i < text.length; i++) {
        if (text.charAt(i) === " ") {
            encrypted += " "
        }
        else if (text.charAt(i) === ".") {
            encrypted += "."
        }
        else if (text.charAt(i) === ",") {
            encrypted += ","
        }
        else if (text.charAt(i) === "!") {
            encrypted += "!"
        }
        else {
            for (let y = 0; y < alphabet.length; y++) {
            if (text.charAt(i).toLowerCase() === alphabet[y]) {
                encrypted += alphabet[y + key]

            }
        }
        }

    }

    document.getElementById("encrypted").innerHTML = encrypted;
}

function decrypt() {

    let alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    let key = Number(document.getElementById("d_key").value);
    let text = document.getElementById("decrypt").value;

    let decrypted = ""
    for (let i = 0; i < text.length; i++) {
        if (text.charAt(i) === " ") {
            decrypted += " "
        }
        else if (text.charAt(i) === ".") {
            decrypted += "."
        }
        else if (text.charAt(i) === ",") {
            decrypted += ","
        }
        else if (text.charAt(i) === "!") {
            decrypted += "!"
        }
        else {
            for (let y = 0; y < alphabet.length; y++) {
            if (text.charAt(i).toLowerCase() === alphabet[y]) {
                decrypted += alphabet[y - key]

            }
        }
        }

    }

    document.getElementById("decrypted").innerHTML = decrypted;
}