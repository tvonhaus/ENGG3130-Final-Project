from numpy import load

data = load('fractal_mandelbrot_data100_iter1500_ovs1.npz')
lst = data.files
for item in lst:
    print(item)
    print(data[item])
