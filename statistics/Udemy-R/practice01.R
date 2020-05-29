d <- read.csv('data01.csv')

hist(d$打率)

hist(d$打率, breaks = seq(0.2,0.34,0.01))

# 正規化　→　偏差値
scale(d$打率) * 10 + 50

# ５つのパラメータを１つの変数にまとめる
# matrix(値,行,列) : 行列をつくる
x <- matrix(0,51,5)

# データを格納
x[,1] <- scale(d$打率) * 10 + 50
x[,2] <- scale(d$本塁打) * 10 + 50
x[,3] <- scale(d$打点) * 10 + 50
x[,4] <- scale(d$盗塁) * 10 + 50
x[,5] <- scale(d$出塁率) * 10 + 50

# 1人目のデータ（四捨五入して）
round(x[1,])

round(x[11,])
