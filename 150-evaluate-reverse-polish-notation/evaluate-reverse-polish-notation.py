class Solution(object):
    def evalRPN(self, tokens):
        stack = []

        for c in tokens:
            if c == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(b + a)

            elif c == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)

            elif c == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(b * a)

            elif c == '/':
                a = stack.pop()
                b = stack.pop()

                # Division truncated toward zero
                if (a < 0) != (b < 0):
                    stack.append(-(abs(b) // abs(a)))
                else:
                    stack.append(abs(b) // abs(a))

            else:
                stack.append(int(c))

        return stack[-1]