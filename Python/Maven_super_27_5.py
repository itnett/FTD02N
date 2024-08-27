python
    def fakulitet(n):
        if n == 1:
            return 1
        else:
            return n * fakulitet(n-1)