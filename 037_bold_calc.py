if __name__ == "__main__":
    variables = {}
    while True:
        cmd = input()
        if not cmd or cmd == ".":
            break
        elif cmd[0] == "#":
            continue

        elif cmd.find("==") != -1:
            print(f"invalid assignment '{cmd}'")
        
        elif cmd.find("=") == -1:
            try:
                print(eval(cmd, variables))
            except Exception as e:
                print(e)

        else:
            ident, expr = cmd.split("=")
            if not ident.isidentifier():
                print(f"invalid identifier '{ident}'")
            else:
                try:
                    variables[ident] = eval(expr, variables)
                except Exception as e:
                    print(e)
