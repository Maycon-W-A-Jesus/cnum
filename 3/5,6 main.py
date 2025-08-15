#Atividade 05
Dado 
x
x e uma tolerância 
τ
τ, encontre o menor 
N
N tal que: 
R
N
+
1
(
x
)
=
∑
n
=
N
+
1
∞
∣
x
∣
n
n
!
<
τ
R 
N+1
​
 (x)=∑ 
n=N+1
∞
​
  
n!
∣x∣ 
n
 
​
 <τ

Gabarito

def min_terms_for_tol(x, tol=1e-12):
    term = 1.0
    n = 0
    while term > tol:
        n += 1
        term *= abs(x) / n
        if n > 100000:
            break
    return n

# Demonstração
for x in [1, 3, 10]:
    n = min_terms_for_tol(x, 1e-12)
    print(f"x={x}: ~{n} termos para atingir tol=1e-12")

if __name__ == "__main__":
    main()

#Atividade 06

  for r in compare_float_vs_highprecision((20, 40, 50), prec=80):
        print(f"x={r[0]}  high-prec={r[1][:18]}...  float64={r[2]}  erro_rel={r[3]}")


if __name__ == "__main__":
    main()