#assert is manily for debugging purposes if a condition is true then the assert statement will be skipped
# otherwise assert message will be displayed assertIon error 

x=10
y=20
assert x==y,"x and y are not equal"
assert x>y,"x is not greater than y"

# command {python -O python_file.py } is used to run a script skipping asserts -O is optimize
print("hello world")