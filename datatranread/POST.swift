import Foundation

func uploadData() {
    // Define the data to be sent
    let dataToUpload: [String: Any] = [
        "name": "John Doe",
        "email": "john.doe@example.com"
    ]

    // Convert the dictionary to JSON data
    guard let jsonData = try? JSONSerialization.data(withJSONObject: dataToUpload) else {
        print("Error: Unable to convert data to JSON")
        return
    }

    // Create the URL
    guard let url = URL(string: "http://127.0.0.1:8000") else {
        print("Error: Invalid URL")
        return
    }

    // Create the request
    var request = URLRequest(url: url)
    request.httpMethod = "POST"
    request.setValue("application/json", forHTTPHeaderField: "Content-Type")
    request.httpBody = jsonData

    // Create the URLSession data task
    let task = URLSession.shared.dataTask(with: request) { data, response, error in
        // Check for errors
        if let error = error {
            print("Error: \(error.localizedDescription)")
            return
        }

        // Check for a valid response
        if let httpResponse = response as? HTTPURLResponse {
            print("Response status code: \(httpResponse.statusCode)")
        }

        // Optionally, handle the response data
        if let data = data {
            if let responseString = String(data: data, encoding: .utf8) {
                print("Response data: \(responseString)")
            }else {
            print("Response data could not be converted to String.")
        }
        }
    }

    // Start the task
    task.resume()
}

// Call the function to execute the upload
uploadData()