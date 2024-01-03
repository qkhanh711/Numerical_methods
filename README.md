# Convergent sequence

<h3> Order of convergence and Rate convergence </h3>

$$ 
\text{A sequence } {X_n} \text{ that converges to } x^* \text{ is said to have order of convergence q >= 1 and rate of convergence } \mu > 0 \text{ (being a constant) if:}
$$

$$ \lim_{n \to \infty} \frac{|X_{n+1} - x^*|}{|X_n - X^*|^q} = \mu $$

$$ \text{for } q = 1 : 0 < \mu < 1 : \text{linear convergence.}$$

$$
\begin{align*}
\mu &= 1 : \text{Sublinear convergence} \\
\mu &= 0 : \text{Superlinear convergence} \\
\mu &= 2 : \text{Quadratic convergence}
\end{align*}
$$

## Examples

$$
x_0 = 1 \\
x_{n+1} = \frac{1}{2} \ln \left( \sqrt{x_n + 1} \right)
$$

## Advantages
- Guaranteed convergence
- Easy to implement
- No need to use derivatives

## Disadvantages

- ...

# Brent's method 

is a hybrid root finding algorithm combine aspect of - bisect and secant

## Advantages
- take advantages of bisect, secant, inverse quadratic interpolation methods
- suitavle for non-smooth func
- fast convegence

## Disavantages
- slower than newton raphson's methodin some cases
- more computational steps

# Recurrence formula

$$
x_n = \frac{x_{n-2} * f(x_{n-1}) - x_{n-1} * f(x_{n-2})}{f(x_{n-1}) - f(x_{n-2})}
$$

=> Methods converges suplinearly with 
$$
q =  \frac{(1 + \sqrt{5} )}{2} = 1.618
$$

## Advantages
- Faster than biection
- Easy to implement
- No need to use derivatives
## Disadvandtages
- Does not always converge

# Newton Raphson

## Recurrence formula:

$$ x_{n+1} = x{n} - \frac{f(x_{n})}{f'{x_{n}}} $$
- $$ \text{Taylor series expansion at } x = a:$$
    
$$f(x) = f(a) = f'(a)(x - a)+...+ \frac{f^ka}{k!}(x-a)^k + \frac{f^{k+1}\xi}{(k+1)!}(x-a)^{k+1}$$ 

$$ \text{for some } \xi \text{ between a and x.}$$

- $$ \text{Since } f{c} = 0 \text{, then} $$

$$ \frac{f(x_n)}{f'(x_n)} + c - x_n = \frac{-f''(\xi_n)}{2*f'(x_n)} (c-x_n)^2 $$

- $$ \text{Since }x_{n+1} = x_{n} - \frac{f(x_{n})}{f'{x_{n}}}, then $$

$$  \frac{|x_{n+1}-c|}{|x_n - c|^2} =  \frac{|f''(\xi_n)|}{2|f'(x_n)|} = \mu$$

## Advantages
- Converges quadrarically
- Work also for multiple root
## Disadvantages
- Derivatives are required
- Depend in initial solution
- No guarantee of convergence
