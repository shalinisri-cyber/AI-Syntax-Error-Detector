from ai_helper import ask_gemini

# Sample C code containing a missing semicolon
code = """
#include <stdio.h>

int main() {
    printf("Hello World")
    return 0;
}
"""

# Error detected by our basic syntax detector
errors = [
    {
        "line": 5,
        "type": "Possible missing semicolon",
        "message": "This statement may require a semicolon (;)."
    }
]

# Send the code and error information to Gemini
answer = ask_gemini(code, errors)

print("\n===== GEMINI AI RESPONSE =====\n")
print(answer)