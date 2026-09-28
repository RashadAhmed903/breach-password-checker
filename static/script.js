const button = document.getElementById("checkButton");
const input = document.getElementById("passwordInput");
const result = document.getElementById("result");

button.addEventListener("click", async () => {
  const password = input.value;

  const response = await fetch("/check-password", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ password: password }),
  });

  const data = await response.json();

  result.style.display = "block";
  result.className = data.breached ? "unsafe" : "safe";
  result.innerHTML = `
    <p>Breached: ${data.breached} (${data.breach_count} time(s))</p>
    <p>Rating: ${data.rating}</p>
    <p>Entropy: ${data.entropy_bits} bits</p>
  `;
});