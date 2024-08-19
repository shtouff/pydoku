from textwrap import dedent, indent

if __name__ == "__main__":
    with open("p096_sudoku.txt", mode="r") as _in, open("euler.py", mode="w+") as _out:
        in_lines = [l.rstrip() for l in _in.readlines()]
        _out.write(dedent(
            '''\
            from textwrap import dedent
            
            sudokus = {
            '''
        ))
        for i in range(50):
            _out.write(indent(dedent(
                f'''\
                "{in_lines[i*10]}": (dedent("""\\
                    {in_lines[i*10 + 1]}
                    {in_lines[i*10 + 2]}
                    {in_lines[i*10 + 3]}
                    {in_lines[i*10 + 4]}
                    {in_lines[i*10 + 5]}
                    {in_lines[i*10 + 6]}
                    {in_lines[i*10 + 7]}
                    {in_lines[i*10 + 8]}
                    {in_lines[i*10 + 9]}
                """), dedent("""\\
                    {in_lines[i*10 + 1]}
                    {in_lines[i*10 + 2]}
                    {in_lines[i*10 + 3]}
                    {in_lines[i*10 + 4]}
                    {in_lines[i*10 + 5]}
                    {in_lines[i*10 + 6]}
                    {in_lines[i*10 + 7]}
                    {in_lines[i*10 + 8]}
                    {in_lines[i*10 + 9]}
                """)),
                '''
            ), prefix="    "))

        _out.write(dedent(
            '''\
            }
            '''
        ))
