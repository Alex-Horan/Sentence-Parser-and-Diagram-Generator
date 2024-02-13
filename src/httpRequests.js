export default async function httpRequest(url, sentence) {
    const response = await fetch(url, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(sentence)
    });
    return response.json();
}