function sendMessage() {
    const input = document.getElementById("userInput");
    const message = input.value.trim();
    if (!message) return;

    const chatbox = document.getElementById("chatbox");

    chatbox.innerHTML += `<div class='user-msg'>${message}</div>`;

    fetch("/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({prompt: message})
    })
    .then(res => res.json())
    .then(data => {
        chatbox.innerHTML += `<div class='bot-msg'>${data.response}</div>`;
        chatbox.scrollTop = chatbox.scrollHeight;
    });

    input.value = "";
    chatbox.scrollTop = chatbox.scrollHeight;
}