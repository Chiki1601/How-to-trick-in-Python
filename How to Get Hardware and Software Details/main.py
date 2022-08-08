'''Get Hardware and System information using Python'''
import platform

my_pc = platform.uname()

print("\n")
print(f"Operating System: {my_pc.system}")

print(f"Node Name: {my_pc.node}")

print(f"Release: {my_pc.release}")

print(f"Version: {my_pc.version}")

print(f"Machine: {my_pc.machine}")

print(f"Processor: {my_pc.processor}")

print(f"Architecture: {platform.architecture}")

print("\n")
