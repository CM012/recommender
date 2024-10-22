import Foundation

// Define the structure for the data to be sent
struct DataToSend: Codable {
    let message: String
}

// Function to send a POST request
func sendPostRequest() {
    // Update the URL to your server's endpoint
    guard let url = URL(string: "http://10.89.87.122:8000/api/data") else { // Use your local IP
        print("Invalid URL")
        return
    }
    
    // Prepare the data to send
    let dataToSend = DataToSend(message: "hello")
    
    // Encode the data to JSON
    guard let jsonData = try? JSONEncoder().encode(dataToSend) else {
        print("Error encoding data")
        return
    }
    
    // Create the URL request
    var request = URLRequest(url: url)
    request.httpMethod = "POST"
    request.setValue("application/json", forHTTPHeaderField: "Content-Type")
    request.httpBody = jsonData
    
    // Create a URLSession data task
    let task = URLSession.shared.dataTask(with: request) { data, response, error in
        // Check for errors
        if let error = error {
            print("Error: \(error.localizedDescription)")
            return
        }
        
        // Check the response
        if let httpResponse = response as? HTTPURLResponse {
            print("HTTP Status Code: \(httpResponse.statusCode)")
        }
        
        // Check if there's data returned
        if let data = data {
            // Attempt to decode the response (if any)
            if let responseString = String(data: data, encoding: .utf8) {
                print("Response Data: \(responseString)")
            }
        }
    }
    
    // Start the data task
    task.resume()
}

// Call the function to send data
sendPostRequest()