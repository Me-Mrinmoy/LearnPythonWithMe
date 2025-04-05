for i in range(2,21):
    for j in range(1,11): 
        with open(f"tables/Multiplication_table_of_{i}", 'w') as f:
            f.write(f"{i}X{j}={i*j}\n")
        break    