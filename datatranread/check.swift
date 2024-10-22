let task = URLSession.shared.dataTask(with: request) { data, response, error in
    // Check for errors
    if let error = error {
        print("Error: \(error.localizedDescription)")
        return
    }

    // Check for a valid response
    if let httpResponse = response as? HTTPURLResponse {
        print("Response status code: \(httpResponse.statusCode)")
        if let headers = httpResponse.allHeaderFields as? [String: String] {
            print("Response headers: \(headers)")
        }
    }

    // Optionally, handle the response data
    if let data = data {
        if let responseString = String(data: data, encoding: .utf8) {
            print("Response data: \(responseString)")
        } else {
            print("Response data could not be converted to String.")
        }
    } else {
        print("No data received.")
    }
}