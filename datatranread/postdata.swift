import Foundation

let address = "http://127.0.0.1:8000/api/data" // Update to the correct endpoint
//let address = "http://127.0.0.1:8000"
let url = URL(string: address)!

var request = URLRequest(url: url)
request.setValue("application/json", forHTTPHeaderField: "Content-Type")
request.httpMethod = "POST"

let encoder = JSONEncoder()
let message = ["calories": "500"] // Replace with your actual data

do {
    let data = try encoder.encode(message)
    request.httpBody = data

    // Log request details
    print("Request URL: \(request.url!)")
    print("HTTP Method: \(request.httpMethod!)")
    print("HTTP Body: \(String(data: request.httpBody!, encoding: .utf8)!)")

    Task {
        do {
            let (responseData, response) = try await URLSession.shared.upload(for: request, from: data)
            print("Response: \(response)")

            // Read the response data
            if let httpResponse = response as? HTTPURLResponse {
                print("Response status code: \(httpResponse.statusCode)")
            }

            if let jsonString = String(data: responseData, encoding: .utf8) {
                print("Response Data: \(jsonString)")
            }
        } catch {
            print("Error: \(error)")
        }
    }
} catch {
    print("Error encoding data: \(error)")
}