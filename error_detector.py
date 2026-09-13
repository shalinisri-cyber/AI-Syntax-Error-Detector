def check_brackets(code):
    stack = []
    errors = []

    bracket_pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    opening_brackets = ['(', '{', '[']

    lines = code.splitlines()

    for line_number, line in enumerate(lines, start=1):
        for character in line:
            if character in opening_brackets:
                stack.append((character, line_number))

            elif character in bracket_pairs:
                if not stack or stack[-1][0] != bracket_pairs[character]:
                    errors.append({
                        "line": line_number,
                        "type": "Unmatched closing bracket",
                        "message": f"Unexpected '{character}'"
                    })
                else:
                    stack.pop()

    while stack:
        character, line_number = stack.pop()

        expected_bracket = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        errors.append({
            "line": line_number,
            "type": "Missing closing bracket",
            "message": f"Expected '{expected_bracket[character]}'"
        })

    return errors


def check_possible_semicolons(code):
    errors = []
    lines = code.splitlines()

    ignored_starts = (
        '#',
        'if',
        'else',
        'for',
        'while',
        'switch',
        'case',
        'default',
        '{',
        '}'
    )

    for line_number, original_line in enumerate(lines, start=1):
        line = original_line.strip()

        if not line:
            continue

        if line.startswith(ignored_starts):
            continue

        if line.endswith((';', '{', '}', ':')):
            continue

        if (
            '=' in line
            or line.startswith('return')
            or line.startswith('printf')
            or line.startswith('scanf')
            or line.startswith('int ')
            or line.startswith('float ')
            or line.startswith('char ')
        ):
            errors.append({
                "line": line_number,
                "type": "Possible missing semicolon",
                "message": "This statement may require a semicolon (;)."
            })

    return errors


def detect_errors(code):
    errors = []

    errors.extend(check_brackets(code))
    errors.extend(check_possible_semicolons(code))

    return errors 