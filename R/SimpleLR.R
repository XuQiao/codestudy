mydata <- read.csv("C:/Users/qiao/Desktop/regression_auto.csv")
attach(mydata)

# Define variables
Y <- cbind(mpg)
X1 <- cbind(weight1)
X <- cbind(weight1, price, foreign)

# Descriptive statistics
summary(Y)
summary(X)

# Correlation among variables
cor(Y, X)

# Plot data
plot(Y ~ X1, data = mydata)

# Simple Linear regression
olsreg1 <- lm(Y ~ X1)
summary(olsreg1)
confint(olsreg1, level = 0.95)
anova(olsreg1)

# Plot regession line
abline(olsreg1)

