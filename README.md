# `ropFinder.py`

`ropFinder.py` is a Python script designed to analyze the output of tools like `rp-win-x86.exe` and locate specific **ROP gadgets** useful for building ROP chains. It identifies patterns such as register manipulation, dereferences, and common gadget sequences.  

## How to Use  

1. Generate gadget output using a tool like `rp-win-x86.exe`:  
   ```cmd  
   rp-win-x86.exe -f osed.exe -r 5 > rop.txt  
   ```
2. Run the `ropFinder.py` script on the generated output:
   ```bash 
   python ropFinder.py rop.txt  
   ```
3. The script will print categorized gadgets (e.g., push/pop, mov, add) to the console for review.

This tool helps streamline the process of identifying gadgets essential for building reliable ROP chains.
