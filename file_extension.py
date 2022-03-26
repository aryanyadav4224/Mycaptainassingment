this_dict = {
        "py": "python",
        "cpp": "C++",
        "java": "JAVA"
}

fn = input("Enter Filename: ")
f = fn.split(".")

print("Extension of the file is : " + this_dict[f[-1]])