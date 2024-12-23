import re
import sys

def detect_push_esp_and_pop_to_register(lines):
    """Detects 'push esp' followed by the first 'pop' into specific registers: esi, eax, ecx, and ensures no other pops follow."""
    pattern = r"^\s*0x[0-9a-fA-F]+:\s*push\s+esp(?:\s*;[^;]*)*;\s*pop\s+(esi|eax|ecx)\b(;\s*pop\s+(?!esi|eax|ecx)\w+\s*;)?"
    print("\nDetecting 'push esp' followed by the first 'pop' into registers (esi, eax, ecx) without additional pops:")
    print("Regex: ^\\s*0x[0-9a-fA-F]+:\\s*push\\s+esp(?:\\s*;[^;]*)*;\\s*pop\\s+(esi|eax|ecx)\\b(;\\s*pop\\s+(?!esi|eax|ecx)\\w+\\s*;)?")
    matches = [line.strip() for line in lines if re.search(pattern, line, re.IGNORECASE)]
    for match in matches:
        print(match)

def detect_mov_between_registers(lines):
    """Detects all 'mov' operations between registers: eax, ecx, esi."""
    pattern = r"^\s*0x[0-9a-fA-F]+:\s*mov\s+(eax|ecx|esi),\s*(eax|ecx|esi)\b"
    print("\nDetecting 'mov' operations between registers (eax, ecx, esi):")
    print("Regex: ^\\s*0x[0-9a-fA-F]+:\\s*mov\\s+(eax|ecx|esi),\\s*(eax|ecx|esi)\\b")
    matches = [line.strip() for line in lines if re.search(pattern, line, re.IGNORECASE)]
    for match in matches:
        print(match)

def detect_dereference_mov_eax(lines):
    """Detects all dereference operations and 'mov' into eax (e.g., mov eax, dword [eax])."""
    pattern = r"^\s*0x[0-9a-fA-F]+:\s*mov\s+eax,\s*dword\s+\[eax\]"
    print("\nDetecting dereference operations and 'mov' into eax (e.g., mov eax, dword [eax]):")
    print("Regex: ^\\s*0x[0-9a-fA-F]+:\\s*mov\\s+eax,\\s*dword\\s+\\[eax\\]")
    matches = [line.strip() for line in lines if re.search(pattern, line, re.IGNORECASE)]
    for match in matches:
        print(match)

def detect_dereference_mov_eax_esi(lines):
    """Detects dereference operations and 'mov' between eax and esi (e.g., mov dword [esi], eax)."""
    pattern = r"^\s*0x[0-9a-fA-F]+:\s*mov\s+dword\s+\[esi\],\s*eax"
    print("\nDetecting dereference operations and 'mov' between eax and esi (e.g., mov dword [esi], eax):")
    print("Regex: ^\\s*0x[0-9a-fA-F]+:\\s*mov\\s+dword\\s+\\[esi\\],\\s*eax")
    matches = [line.strip() for line in lines if re.search(pattern, line, re.IGNORECASE)]
    for match in matches:
        print(match)

def detect_add_eax_ecx(lines):
    """Detects 'add' operations between eax and ecx."""
    pattern = r"^\s*0x[0-9a-fA-F]+:\s*add\s+(eax|ecx),\s*(eax|ecx)"
    print("\nDetecting 'add' operations between eax and ecx:")
    print("Regex: ^\\s*0x[0-9a-fA-F]+:\\s*add\\s+(eax|ecx),\\s*(eax|ecx)")
    matches = [line.strip() for line in lines if re.search(pattern, line, re.IGNORECASE)]
    for match in matches:
        print(match)

def detect_pop_eax_ecx_ret(lines):
    """Detects 'pop eax' or 'pop ecx' followed immediately by 'ret'."""
    pattern = r"^\s*0x[0-9a-fA-F]+:\s*pop\s+(eax|ecx)\s*;\s*ret\b"
    print("\nDetecting 'pop eax' or 'pop ecx' followed by 'ret':")
    print("Regex: ^\\s*0x[0-9a-fA-F]+:\\s*pop\\s+(eax|ecx)\\s*;\\s*ret\\b")
    matches = [line.strip() for line in lines if re.search(pattern, line, re.IGNORECASE)]
    for match in matches:
        print(match)

def detect_copy_operations_esp(lines):
    """Detects copy operations involving the ESP register."""
    pattern = r"^\s*0x[0-9a-fA-F]+:\s*(mov|lea)\s+(eax|ecx|esi),\s*\[?esp\]?"
    print("\nDetecting copy operations involving ESP register:")
    print("Regex: ^\\s*0x[0-9a-fA-F]+:\\s*(mov|lea)\\s+(eax|ecx|esi),\\s*\\[?esp\\]?")
    matches = [line.strip() for line in lines if re.search(pattern, line, re.IGNORECASE)]
    for match in matches:
        print(match)

if __name__ == "__main__":
    # Ensure a filename is provided
    if len(sys.argv) != 2:
        print("Usage: python ropFinder.py <filename>")
        sys.exit(1)

    # Read the file and execute all detection functions
    filename = sys.argv[1]
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        # Run all detection functions
        detect_push_esp_and_pop_to_register(lines)
        detect_mov_between_registers(lines)
        detect_dereference_mov_eax(lines)
        detect_dereference_mov_eax_esi(lines)
        detect_add_eax_ecx(lines)
        detect_pop_eax_ecx_ret(lines)
        detect_copy_operations_esp(lines)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
