data = {
    "response": {
        "status": "success",
        "payload": {
            "function_code": 4,
            "registers": [
                100,
                101,
                102,
                103,
                104,
                105,
                106,
                107,
                108,
                109
            ],
            "address": 10
        },
        "operation": "ReadInputRegistersRequest",
        "device": 1
    },
    "id": "10001:1:10"
}

response = payload.get('response', {})
registers = response.get('payload', {}).get('registers', {})