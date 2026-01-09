import os
import subprocess
import sys

def run_test(test_dir):
    print(f"--> Testing {test_dir}")
    
    # Convention: Look for standard filenames
    sv_file = os.path.join(test_dir, "dut.sv")
    cpp_file = os.path.join(test_dir, "sim_main.cpp")
    
    if not os.path.exists(sv_file) or not os.path.exists(cpp_file):
        print(f"Skipping {test_dir}: dut.sv or sim_main.cpp missing")
        return True

    # 1. Verilate
    # --build automatically calls make
    # --cc specifies C++ output
    # --exe links the executable
    cmd = ["verilator", "--cc", "--exe", "--build", "-j", "0", "dut.sv", "sim_main.cpp"]
    
    try:
        subprocess.check_call(cmd, cwd=test_dir)
        
        # 2. Run the Simulation
        # The executable is built in obj_dir/Vtop
        exe_path = os.path.join(test_dir, "obj_dir", "Vdut")
        subprocess.check_call([exe_path], cwd=test_dir)
        
        print(f"PASS: {test_dir}")
        return True
    except subprocess.CalledProcessError:
        print(f"FAIL: {test_dir}")
        return False

def main():
    root_dir = sys.argv[1] if len(sys.argv) > 1 else "tests"
    failed = False
    
    # Walk through the "tests" directory looking for subfolders
    for item in os.listdir(root_dir):
        path = os.path.join(root_dir, item)
        if os.path.isdir(path):
            if not run_test(path):
                failed = True
                
    if failed:
        sys.exit(1)

if __name__ == "__main__":
    main()