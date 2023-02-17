import module_imports as module

functions = {
    1: module.passwd_gen.run,
    0: module.commands.exit,
}

while True:
    module.art.logo()
    module.options.menu()
    try:
        choice_input = int(input("Input : "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        continue
    functions.get(choice_input, lambda: None)()