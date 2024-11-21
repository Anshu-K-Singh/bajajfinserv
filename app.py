from flask import Flask, jsonify, request
import base64
import math
import filetype

app = Flask(__name__)

# POST Endpoint
@app.route('/bfhl', methods=['POST'])
def process_data():
    data = request.get_json()
    
    # Log the incoming data to see what we get
    print(f"Received data: {data}")
    
    if not data or 'data' not in data:
        return jsonify({"is_success": False, "error": "Invalid input."}), 400

    # Extract and categorize the data
    input_data = data['data']
    numbers = [x for x in input_data if x.isdigit()]
    alphabets = [x for x in input_data if x.isalpha()]
    
    # Get the highest lowercase alphabet (if exists)
    lowercase_alphabets = [ch for ch in alphabets if ch.islower()]
    highest_lowercase = [max(lowercase_alphabets, default="")] if lowercase_alphabets else []

    # Prime check function
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, math.isqrt(n) + 1):
            if n % i == 0:
                return False
        return True

    is_prime_found = any(is_prime(int(num)) for num in numbers)

    # File validation
    file_b64 = data.get('file_b64', None)
    file_valid = False
    file_mime_type = "unknown/unknown"
    file_size_kb = 0.0

    if file_b64:
        try:
            # Decode the base64 encoded file
            decoded_file = base64.b64decode(file_b64)
            file_size_kb = len(decoded_file) / 1024  # Convert bytes to KB
            
            # Check if the file is empty
            if len(decoded_file) == 0:
                raise ValueError("Decoded file is empty.")
            
            # Detect MIME type using filetype library
            kind = filetype.guess(decoded_file)
            if kind:
                file_mime_type = kind.mime
            else:
                # If filetype can't detect, manually check for known image signatures
                if decoded_file[:8] == b'\x89PNG\r\n\x1a\n':
                    file_mime_type = "image/png"
                elif decoded_file[:2] == b'\xff\xd8':
                    file_mime_type = "image/jpeg"
                elif decoded_file[:4] == b'GIF8':
                    file_mime_type = "image/gif"
                else:
                    file_mime_type = "unknown/unknown"
            
            file_valid = True  # Mark the file as valid if it passed decoding and MIME detection
        
        except Exception as e:
            print(f"Error processing file: {e}")
            file_valid = False

    # Prepare the response
    response = {
        "is_success": True,
        "user_id": "anshu_singh_17091999",
        "email": "anshu@xyz.com",
        "roll_number": "ABCD123",
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": highest_lowercase,
        "is_prime_found": is_prime_found,
        "file_valid": file_valid,
        "file_mime_type": file_mime_type,
        "file_size_kb": round(file_size_kb, 2)
    }

    return jsonify(response)

# GET Endpoint
@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    app.run(debug=True)
