import Foundation

let address = "http://127.0.0.1:8000/api/data" // Update as needed
let url = URL(string: address)!

var request = URLRequest(url: url)
request.httpMethod = "GET"

Task {
    do {
        let (responseData, response) = try await URLSession.shared.data(for: request)
        print("Response: \(response)")
        
        // Read and parse the response data
        if let jsonString = String(data: responseData, encoding: .utf8) {
            print("Response Data: \(jsonString)")
            
            // Optional: Parse the JSON if needed
            if let jsonData = try? JSONSerialization.jsonObject(with: responseData, options: []) {
                print("Parsed JSON: \(jsonData)")
            }
        }
    } catch {
        print("Error: \(error)")
    }
}
