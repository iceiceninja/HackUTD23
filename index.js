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
async function submitForm() {
    // Get form data
    const formData = {
        GrossMonthlyIncome: document.getElementById('GrossMonthlyIncome').value,
        CreditCardPayment: document.getElementById('CreditCardPayment').value,
        CarPayment: document.getElementById('CarPayment').value,
        StudentLoanPayments: document.getElementById('StudentLoanPayments').value,
        AppraisedValue: document.getElementById('AppraisedValue').value,
        DownPayment: document.getElementById('DownPayment').value,
        LoanAmount: document.getElementById('LoanAmount').value,
        MonthlyMortgagePayment: document.getElementById('MonthlyMortgagePayment').value,
        CreditScore: document.getElementById('CreditScore').value
    };
    await fetch("/loan-application", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
    })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            // Handle the response from the API as needed.
        })
        .catch(error => {
            console.error("Error:", error);
        });
    // You can now use the 'formData' object to perform actions, such as sending the data to a server via AJAX or processing it as needed.
    console.log(formData); // For demonstration, this logs the form data to the console.
}