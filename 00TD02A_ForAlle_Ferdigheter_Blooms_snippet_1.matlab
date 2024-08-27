syms s
X = 1 / (m*s^2 + c*s + k);
x_t = ilaplace(X);
ezplot(x_t, [0, 10])
title('Dempet harmonisk oscillator')