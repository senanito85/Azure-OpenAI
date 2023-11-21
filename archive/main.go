package main

import (
	"bytes"
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
)

func main() {
	// Replace 'YOUR_OPENAI_API_KEY' with your actual API key
	apiKey := "YOUR_OPENAI_API_KEY"

	// Replace 'YOUR_OPENAI_ENDPOINT' with your actual endpoint URL
	endpoint := "YOUR_OPENAI_ENDPOINT"

	// Get input from command line arguments or user input
	var input string
	if len(os.Args) > 1 {
		input = os.Args[1]
	} else {
		fmt.Print("Enter a line of text: ")
		fmt.Scanln(&input)
	}

	// Prepare the request payload
	payload := fmt.Sprintf(`{"prompt": "%s"}`, input)

	// Create an HTTP client
	client := &http.Client{}

	// Create the API request
	req, err := http.NewRequest("POST", endpoint, bytes.NewBuffer([]byte(payload)))
	if err != nil {
		fmt.Println("Error creating request:", err)
		return
	}

	// Set the API key in the request headers
	req.Header.Set("Authorization", "Bearer "+apiKey)
	req.Header.Set("Content-Type", "application/json")

	// Send the request and get the response
	resp, err := client.Do(req)
	if err != nil {
		fmt.Println("Error sending request:", err)
		return
	}
	defer resp.Body.Close()

	// Read the response body
	respBody, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Println("Error reading response body:", err)
		return
	}

	// Print the response
	fmt.Println("Response:")
	fmt.Println(string(respBody))
}
