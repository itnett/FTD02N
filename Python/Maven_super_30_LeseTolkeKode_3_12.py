python
if __name__ == "__main__":
    while True:
        try:
            print("Enter: commits prs issues stars followers")
            inp = list(map(int, input("Enter: ").split())) 
            grade = calculateRank(True, *inp)
            print("\n[*] Your Github Grade stats:", grade)
        except KeyboardInterrupt:
            break 
        except Exception:
            pass