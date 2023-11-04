async function callApi() {
    try {
        console.log("Hello world!!");
        const response = await fetch("http://127.0.0.1:8000");

        if (!response.ok) {
            throw new Error(`Request failed with status: ${response.status}`);
        }

        const data = await response.json();
        console.log(data);
        document.getElementById("apiOutput").innerText = data.message

        return data;
    } catch (error) {
        console.error("An error occurred:", error);
    }
}
async function callApi2() {
    try {
        console.log("Hello world!!");
        const response = await fetch("http://127.0.0.1:8000/hello");

        if (!response.ok) {
            throw new Error(`Request failed with status: ${response.status}`);
        }

        const data = await response.json();
        console.log(data);
        document.getElementById("apiOutput").innerText = data.message
        return data;
    } catch (error) {
        console.error("An error occurred:", error);
    }
}
