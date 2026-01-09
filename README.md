# FPGA CI Tools 🛠️

A centralized testing framework for FPGA and SystemVerilog development.

This repository hosts a **Reusable GitHub Workflow** and a custom **Python Test Runner**. It allows you to decouple testing logic from your individual project repositories, ensuring that all your assignments and projects are tested against the exact same environment (latest Verilator) with zero configuration overhead.

## 🚀 Features

* **Zero-Config Setup:** Add one small YAML file to any new project to enable full CI/CD.
* **Always Fresh:** Runs inside the official `verilator/verilator:latest` Docker container, ensuring you are always using the newest toolchain.
* **Automatic Discovery:** The Python runner automatically finds test subdirectories and executes them independently.
* **Standardized Output:** Enforces a clean separation between source code and test benches.

## ⚙️ How it Works

This repository acts as the "Hub." Your individual project repositories (the "Spokes") call the workflow defined here.

1.  **The Runner:** A Python script scans your `tests/` folder for subdirectories.
2.  **The Environment:** It spins up a Docker container with Verilator, Make, and G++ pre-installed.
3.  **The Execution:** It compiles your `dut.sv` and `sim_main.cpp` into an executable and runs it.

## 📦 Usage Guide

### 1. Organize your Project Repository
To make your project compatible with this runner, structure your folders like this:

```text
my-class-project/
├── src/                  # Your design modules (e.g., alu.sv)
└── tests/                # Your test directory
    ├── test_case_1/      # A specific test case
    │   ├── dut.sv        # Testbench wrapper
    │   └── sim_main.cpp  # Verilator C++ harness
    └── test_case_2/
        ├── dut.sv
        └── sim_main.cpp
