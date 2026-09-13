from error_detector import detect_errors


c_code = '''
#include <stdio.h>

int main() {
    printf("Hello World");
    return 0;
}
'''

errors = detect_errors(c_code)

if errors:
    print("Syntax errors detected:\n")

    for error in errors:
        print(f"Line {error['line']}: {error['type']}")
        print(f"Message: {error['message']}\n")
else:
    print("No basic syntax errors detected.")