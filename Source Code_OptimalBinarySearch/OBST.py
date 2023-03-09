def optimal_bst(kunci, frekuensi, nilai):
    # Membuat tabel DP yang berukuran n+2 x n+2
    dp = [[0 for i in range(nilai+2)] for j in range(nilai+2)]

    # Mengisi diagonal tabel dengan frekuensi
    for i in range(1, nilai+1):
        dp[i][i] = frekuensi[i-1]

    # Mengisi tabel dengan nilai minimum
    for L in range(2, nilai+2):
        for i in range(1, nilai-L+3):
            j = i+L-1
            dp[i][j] = float('inf')
            # Memilih kunci root dengan minimum cost
            for r in range(i, j+1):
                c = dp[i][r-1] if r > i else 0
                c += dp[r+1][j] if r < j else 0
                c += sum(frekuensi[i-1:j])
                if c < dp[i][j]:
                    dp[i][j] = c
    
    # Mengembalikan cost minimum
    return dp[1][nilai]

# Contoh penggunaan
kunci = [22, 20, 30, 40, 50]
frekuensi = [4, 2, 6, 3, 1]
nilai = len(kunci)
print("Biaya optimal BST: ", optimal_bst(kunci, frekuensi, nilai))

