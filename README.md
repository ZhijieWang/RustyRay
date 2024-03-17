# Purpose

This repo is a demonstration of interoperability between Ray's Python Interface and Rust libraries.
This is a demo only, both Rust and Ray code are not optimized.

# Steps
1. Clone the repo
2. Get Rust lang (as of writing recent stable rust release is 1.76. but nothing is fancy, so most should workd)
3. Get Ray  (version 2.9.3)
4. Python 3.8+
5. Follow the commands below to create a new directory containing a new Python virtualenv, and install maturin into the virtualenv using Python's package manager. Also this will install Ray:
```
# (replace string_sum with the desired package name)
$ mkdir string_sum
$ cd string_sum
$ python -m venv .env
$ source .env/bin/activate
$ pip install maturin
$ pip install ray
```
6. Run `maturin dev`, this will compile the Rust lib into a python shared lib
7. Start the python interpreter and verify the `prover` module can be imported. use `import prover`
8. Start Ray head node with `ray start --head`
9.  run ` python3 distributed_proving.py` and see results
10. shutdown ray with `ray stop`