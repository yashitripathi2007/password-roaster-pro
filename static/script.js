function checkPassword() {
  const password = document.getElementById("password").value;
  const style = document.getElementById("style").value;

  // Frontend empty check
  if (!password) {
    document.getElementById("roast").innerText =
      "Bestie… you didn’t even type a password 😭";
    document.getElementById("strength").style.width = "0%";
    document.getElementById("strengthText").innerText = "Very Weak";
    document.getElementById("suggestion").innerText = "";
    return;
  }

  fetch("/check", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ password, style })
  })
    .then(res => res.json())
    .then(data => {
      document.getElementById("roast").innerText = data.roast;
      document.getElementById("suggestion").innerText = data.suggestion;

      const bar = document.getElementById("strength");
      const percent = (data.score / 5) * 100;
      bar.style.width = percent + "%";
      bar.style.background =
        percent < 40 ? "red" : percent < 80 ? "orange" : "lime";

      const levels = ["Very Weak", "Weak", "Okay", "Strong", "God Tier"];
      document.getElementById("strengthText").innerText =
        levels[data.score];
    })
    .catch(err => {
      console.error(err);
      document.getElementById("roast").innerText =
        "Something broke… not your fault 😵";
    });
}

function copyPassword() {
  const text = document.getElementById("suggestion").innerText;
  if (!text) return;

  navigator.clipboard.writeText(text);
  alert("Copied 🔥");
}

function toggleMode() {
  document.body.classList.toggle("dark");
  document.body.classList.toggle("light");
}
