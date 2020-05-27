
x <- c(46,40,60,49,43,45,56,48,41,50,61,55,40,47,52,47,44,44,54,63,48,34,51,60,48,65,57,42,55,48)

# histgram of x
hist(x, breaks = seq(20, 80, 2.5))

# mean,standard deviation
m <- mean(x)
s <- sd(x)

# normal distribution
x1 <- seq(20, 80, 0.01)
d <- dnorm(x1, mean = m, sd = s)

plot(x1, d, type = 'l')