import time 

CODE_SECRET = "0123456789"

def brute_force():
    for i in range(10000000000):
        tentative = f"{i:10}"
        print(f"Essai : {tentative}", end="\r")
        time.sleep(0.01)
        if tentative == CODE_SECRET:
            print(f"\n✅ Code trouvé : {tentative}")
            break 

brute_force()
